
Amazon CloudWatch is a monitoring and management service provided by Amazon Web Services (AWS). CloudWatch allows you to collect and track metrics, collect and monitor log files, and set alarms. When it comes to Amazon Elastic Compute Cloud (EC2) instances, installing the CloudWatch agent is one way to enhance monitoring capabilities.

Here are some reasons why we need to install the CloudWatch agent on your EC2 instances:

- **Custom Metrics**: The CloudWatch agent allows you to collect custom metrics from your EC2 instances. These could be application-specific metrics that are important for monitoring the health and performance of your applications.

- **Detailed System Metrics:** While basic metrics (like CPU utilization, disk I/O, and network utilization) are automatically collected for EC2 instances, the CloudWatch agent enables the collection of more detailed system-level metrics, giving you a more granular view of your instance’s performance.

- **Log Collection:** CloudWatch agent also facilitates the collection and forwarding of log files from your EC2 instances to CloudWatch Logs. This is useful for centralizing logs for analysis, monitoring, and troubleshooting.

- **Unified Monitoring:** By using CloudWatch, you can have a unified monitoring solution for your AWS resources, including EC2 instances. This allows you to visualize and set alarms based on metrics collected from different AWS services in one central location.

- **Custom Alarms and Notifications:** With CloudWatch, you can set up custom alarms based on metrics collected from your EC2 instances. This enables you to receive notifications or take automated actions when certain thresholds are breached, helping you proactively manage your infrastructure.

- **Integration with Other AWS Services:** CloudWatch integrates with other AWS services, such as AWS Lambda, to enable automated responses based on monitoring data. For example, you could set up a Lambda function to automatically scale your EC2 instances based on CloudWatch metrics.

**Architecture:**

![](https://miro.medium.com/v2/resize:fit:875/1*WkIjlAFUiytTrjl42Mkohg.png)

**Prerequisites:**

1. We need an EC2 Instance on which we need to install CloudWatch agent.

![](https://miro.medium.com/v2/resize:fit:875/1*c7Bse3SUz9TSqq7kthJRuA.png)

2. Create IAM Role with **CloudWatchAgentServerPolicy** and attach it to above EC2.

![](https://miro.medium.com/v2/resize:fit:875/1*fhyoA0o7044nOIk7HOlUww.png)

**Steps to install CloudWatch Agent on EC2 Instance:**

1. Navigate to EC2 Console.

2. Connect to EC2 instance on which we need to install the agent.

3. To install CloudWatch agent on EC2, execute below command:

- sudo yum install amazon-cloudwatch-agent -y

![](https://miro.medium.com/v2/resize:fit:875/1*ZSfEOwNZ_gmoDL_DmvCzYA.png)

4. Configuration file is used to launch the CloudWatch agent.We must run the following command in order to start the CloudWatch agent and answer the following questions

- sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard

![](https://miro.medium.com/v2/resize:fit:875/1*Ky_ERDW0PJPT_OwQmmcsVA.png)

5. If we need to modify any field, we can modify config.json file which is located in below location:

- Cd /opt/aws/amazon-cloudwatch-agent/bin/

6. Start the agent by executing below command:

- sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json -s

7. Execute below command to check the status of the agent.

- sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status

Output:

- A new log group will be created and you can see /var/log/app.log logs in that log group.

- In the metric group, we can see all metrics about our EC2 instance(e.g. CPU usage, disk_used_percent, mem_used_percent, swap_used_percent, etc.).