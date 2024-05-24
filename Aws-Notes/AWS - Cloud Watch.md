**Monitoring**
**Alerting**
**Reporting**
**Logging**

## What is AWS CloudWatch?

AWS CloudWatch is a powerful monitoring and observability service provided by Amazon Web Services. It enables you to gain insights into the performance, health, and operational aspects of your AWS resources and applications. CloudWatch collects and tracks metrics, collects and monitors log files, and sets alarms to alert you on certain conditions.

## Advantages of AWS CloudWatch:

    Comprehensive Monitoring: CloudWatch allows you to monitor various AWS resources such as EC2 instances, RDS databases, Lambda functions, and more. You get a unified view of your entire AWS infrastructure.

    Real-Time Metrics: It provides real-time monitoring of metrics, allowing you to respond quickly to any issues or anomalies that might arise.

    Automated Actions: With CloudWatch Alarms, you can set up automated actions like triggering an Auto Scaling group to scale in or out based on certain conditions.

    Log Insights: CloudWatch Insights lets you analyze and search log data from various AWS services, making it easier to troubleshoot problems and identify trends.

    Dashboards and Visualization: Create custom dashboards to visualize your application and infrastructure metrics in one place, making it easier to understand the overall health of your system.

## Problem Solving with AWS CloudWatch:

CloudWatch helps address several critical challenges, including:

    Resource Utilization: Tracking resource utilization and performance metrics to optimize your AWS infrastructure efficiently.
    Proactive Monitoring: Identifying and resolving issues before they impact your applications or users.
    Troubleshooting: Analyzing logs and metrics to troubleshoot problems and reduce downtime.
    Scalability: Automatically scaling resources based on demand to ensure optimal performance and cost efficiency.

Practical Use Cases of AWS CloudWatch:

    Auto Scaling: CloudWatch can trigger Auto Scaling actions based on defined thresholds. For example, you can automatically scale in or out based on CPU utilization or request counts.

    Resource Monitoring: Monitor EC2 instances, RDS databases, DynamoDB tables, and other AWS resources to gain insights into their performance and health.

    Application Insights: Track application-specific metrics to monitor the performance of your applications and identify potential bottlenecks.

    Log Analysis: Use CloudWatch Logs Insights to analyze log data, identify patterns, and troubleshoot issues in real-time.

    Billing and Cost Monitoring: CloudWatch can help you monitor your AWS billing and usage patterns, enabling you to optimize costs.

---



1.  Service that collects and Manages operational data 
2. Operational data is any data that is collected by an environment either detailing how it performs, how it normally runs or any logging data it generates.

## Metrics: 
 - Collects data of AWS products, Apps, On-prem

## CloudWatch Logs:
 - Logs of AWS products, Apps, On-Prem

## Cloud Watch Events:
 - AWS Services & Schedules 
     Ex: It generates Cloud watch events when EC2 stops, starts or anything.

---
## Namespaces:
- Container for monitoring data. It is a way to keep things separate.
- Namespace has got a name, it can be anything as long as it says within the rule set 
- **All AWS data goes to AWS namespace  --> aws/service
EX: AWS/EC2 for EC2 instances.**
- Namespace contains relates metrics

## Metrics:
- It is just a collection of related datapoints in the time ordered structure.
     - Ex: CPU usage, Network IN/OUT, Disk I/O 
## Data Point :
- Let us say we have a metric called CPU utilization, Every time  any server measures its utilization & sends into cloud watch that goes into the CPU utilization metrics and each one of those measurements. So everytime the never reports its CPU that measurement is called "Data Point".

 1. Time Stamp = 2019-12-03 To 8:45:45 
 2. Value = 98.3

CPU Utilization Metric:

- CPU utilization metric could contain data from many server. So how do we separate data for this? was that where dimensions are used

## Dimensions: 
- Dimensions are the name value pairs that separate datapoints for different things or perspective within the same metric
- while sending datapoint to cloud watch, AWS also sends in these two:
            1. Name = Instance ID, value = i-xx
            2. Name = Instance type, value = t2.micro
        This will allow us to view the data point for the particular instance.

## Alarms:
- Cloud watch also allow to take actions based on metrics, which is done using alarms
- Alarms are created and linked to specific metric then based on how you configure the alarm it will take an action
- Two stages :
      1. OK - Everything u working file
      2. ALARM - Something bad has happened 

- If the metric u in ALARM state we can take actions like Coding SNS notifications 
- Insufficient Data means the alarm is like gathering data.


---

# AWS EC2 Monitoring with Cloudwatch | Monitor Memory Utilization using CloudWatch | AWS CloudWatch Demo

## Steps:

### Step 1: Create an IAM and Attach CloudWatch and SSM Full Access - EC2-CloudWatch-Role
### Step 2: Create a parameter in Systems Manger with the name "/alarm/AWS-CWAgentLinConfig" and store the value.
### Step 3: Create an EC2 Instance, Attach the role created in Step 1 and Add the commands in the Userdata Section.


## Commands that needs to be added in Userdata Section:
```bash
#!/bin/bash
wget https://s3.amazonaws.com/amazoncloudwatch-agent/linux/amd64/latest/AmazonCloudWatchAgent.zip
unzip AmazonCloudWatchAgent.zip
sudo ./install.sh
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c ssm:/alarm/AWS-CWAgentLinConfig -s
```
## Check if EC2 Instance has CWAgent Installed or not:
```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status
```

## Value for the SSM Parameter (/alarm/AWS-CWAgentLinConfig):
```bash
{
	"metrics": {
		"append_dimensions": {
			"InstanceId": "${aws:InstanceId}"
		},
		"metrics_collected": {
			"mem": {
				"measurement": [
					"mem_used_percent"
				],
				"metrics_collection_interval": 60
			}
		}
	}
}
```
## Reference/Additional Reading:
1. [aws](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent-New-Instances-CloudFormation.html)
2. [AWS Cloudwatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html)



---
**Cloud Watch** :

- Collect logs, Metrics and custom metrics of AWS services.
- Monitor Metrics, Statistics and alarms in dashboards.
- Act on alarms and events. Implement corrective action
- Analyse metrics with Cloudwatch logs Insights.
- Compliance and Security controlled with IAM and Data encryption at rest in transit.

**Cloud watch metrics**

- Data about the performance of your systems.
- Most AWS services (Not available in all regions)
- Ex: - Billing , Dynamo DB, EC2, EBS, Kinesis etc..

**Alarms** 

- Billing alarms as well as resource alarms
- Integrate with SNS
- Three states : OK, ALARM & INSUFFICIENT DATA
- If a metric is above the alarm threshold for the Number of time periods defined by the evaluation period, an alarm is invoked.

**Cloud watch Logs** 

- Agent is Installed on Instance.
- Monitor, store and access your log files from ec2 instances, CloudTrail or other sources.
- Search and Analyze data with Cloud watch logs Insights.
---

### cpu_spike.py:

```py
import time

def simulate_cpu_spike(duration=30, cpu_percent=80):
    print(f"Simulating CPU spike at {cpu_percent}%...")
    start_time = time.time()

    # Calculate the number of iterations needed to achieve the desired CPU utilization
    target_percent = cpu_percent / 100
    total_iterations = int(target_percent * 5_000_000)  # Adjust the number as needed

    # Perform simple arithmetic operations to spike CPU utilization
    for _ in range(total_iterations):
        result = 0
        for i in range(1, 1001):
            result += i

    # Wait for the rest of the time interval
    elapsed_time = time.time() - start_time
    remaining_time = max(0, duration - elapsed_time)
    time.sleep(remaining_time)

    print("CPU spike simulation completed.")

if __name__ == '__main__':
    # Simulate a CPU spike for 30 seconds with 80% CPU utilization
    simulate_cpu_spike(duration=30, cpu_percent=80)
```

- python3 cpu_spike.py