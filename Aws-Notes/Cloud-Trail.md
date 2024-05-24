
AWS CloudTrail is an application program interface (API) call-recording and log-monitoring Web service offered by Amazon Web Services (AWS).

AWS CloudTrail allows AWS customers to record API calls, storing them in Amazon S3 buckets. API activity data included in the service includes the identity of an API caller, the time of the API call, the source of an API caller’s IP address, parameters of the API request and the response.

**CloudTrail:**

- CloudTrail is a service that provides governance, compliance, and auditing capabilities for your AWS account.

- It records and logs all API activity within your AWS account, including actions taken through the AWS Management Console, AWS CLI, SDKs, and other AWS services.

- CloudTrail tracks who made the API call, when it was made, which resources were affected, and the source IP address of the requester.

- It helps you ensure compliance with security standards, troubleshoot operational issues, and investigate security incidents by providing a detailed history of API actions.

- CloudTrail focuses on providing an audit trail of API activity within your AWS account.

- It records and logs all API actions taken in your AWS account, including actions performed through the AWS Management Console, AWS CLI, SDKs, and other AWS services.

- CloudTrail captures information such as who made the API call when it was made, which resources were involved, and the source IP address of the requester.

- These logs are useful for compliance, security, and troubleshooting purposes.

- CloudTrail logs can be analyzed to understand who accessed or modified resources, to investigate security incidents, and to ensure compliance with regulatory requirements.

- It also integrates with AWS CloudTrail Insights, which uses machine learning algorithms to detect anomalous activity and potential security threats in your AWS account.

# [](https://azizulmaqsud-1684501031000.hashnode.dev/cloudwatch-vs-cloudtrail-two-interactive-watch-dogs-in-the-aws#heading-differences-explained-in-details "Permalink")**Differences Explained in Details**

Two AWS services with very similar names but fulfilling two very different functions in the AWS ecosystem.

## [](https://azizulmaqsud-1684501031000.hashnode.dev/cloudwatch-vs-cloudtrail-two-interactive-watch-dogs-in-the-aws#heading-what-is-amazon-cloudwatch "Permalink")**What is Amazon CloudWatch?**

CloudWatch is an AWS monitoring application and it offers features that allow you to

- collect,
    
- monitor, and
    
- analyze your applications help.
    

These are the three main things that people use Cloud watch for. Now, a lot of folks get confused with Cloud watch is that over time? It is developed with a whole bunch of different features that fit within these three categories. CloudWatch is a kind of an umbrella service because it has so many different functions that are kind of related but in other ways not.

**First, in terms of collection:**

A main function of any application is collecting application logs like when errors are occurring. It is an indicator of something going wrong in our application, or even if there's not anything going wrong, and we just want to analyze the flow of control in our application. Logs are a critical input that allows us to analyze what is going on now and what has gone on in the past in terms of our application. AWS Cloudwatch offers ways to ingest very large volumes of application logs, and it stores them at a relatively cheap cost.

**Second, in terms of monitoring:**

Now, in monitoring, one of the big features that Cloud Watch allows you to do is to create metric graphs for CPU or memory for certain applications like hosting maybe a REST API or a back-end application. Cloudwatch allows you to create these graphs and link them to these different metrics to visualize the counts of certain metrics over times. As a result, many different services in AWS emit their own default set of metrics.

However, you can create your own metrics for instance, maybe for your application, for a certain dependency; maybe you want to know how many times you call that dependency, or what's the latency when you call that dependency. You can create and capture these different types of metrics, plot them on the graph, and then see how the information changes over time.

You can also slice and dice your data by combining different metrics together. Once you're done observing the metrics, another useful feature is to create alarms on those metrics. It allows you to become notified whenever something out of the ordinary happens in your application for a prolonged period of time. An example, if there’s an elevated CPU usage, maybe above 90% for 15 minutes or so that usually indicates that there's something wrong with the application. So you can set up an alarm that triggers a notification that sends an email a text message or even pages to let you know that something is going wrong with your application.

Another big part of monitoring is tracing. It allows you to drill down on certain invocations to see different profile characteristics of those invocations like CPU usage, memory usage, disk space usage, and network throughput. They are related to a particular invocation. You can visualize and deep dive into each of them.

**Third, in terms of analyzing:**

In the Analyzing category, there are CloudWatch log insights. Cloudwatch, log insights allow you to basically perform SQL-style queries on your log information and do some interesting analysis on them from the data analytics perspective.

There’s a Cloud event. It’s basically just a serverless cron job that allows you to invoke a certain function or perform a certain action at a regular interval or a fixed interval. CloudWatch Event Bridge, which is basically just application events that you can integrate into an Event Bus and respond to programmatically.

## [](https://azizulmaqsud-1684501031000.hashnode.dev/cloudwatch-vs-cloudtrail-two-interactive-watch-dogs-in-the-aws#heading-what-is-amazon-cloudtrail "Permalink")**What is Amazon CloudTrail?**

CloudTrail enables auditing, security monitoring, and operational troubleshooting by tracking user activity and API usage. CloudTrail logs continuously monitors, and retains account activity related to actions across your AWS infrastructure, giving you control over storage, analysis, and remediation actions.

CloudTrail allows you to analyze who performed what actions and when on your AWS resources. It follows the trails. You can create a table, update a table, or describe a table. You can see different times in which the things were executed. You can see the user name, the event source, the resource type and the resource [name. In](http://name.in/) this way, CloudTrail allows you to have an audit log of all of the events that are related to your AWS applications.

This is the main purpose of cloud trail, not meant for applications but meant for auditing your AWS accounts. There are three types of events that CloudTrail offers.

1. The first one is Management Events: Management or Control Plane events are just the administrative types of events. So the creation of resources like a DynamoDB table, an S3 bucket or the updating or any other modification event to those resources that are considered a management event. Logins or logouts are relatively low volume, and these Management Events are automatically enabled when an AWS account is created. So if you've never gone to the Cloudtrail section before, you can go and check it out now and you should see a list of different events of all the different things that have been happening in your AWS account over the past.
    
2. The second type is data events: Data events are usually in much higher volume. It includes things like queries on a DynamoDB table or invocations of a lambda function, much more a higher volume or higher throughput. It doesn’t come enabled by default. You have to enable them on a particular AWS service if you want to capture this type of information.
    
3. Thirdly, there are insights: Insights are a special type of trial. It allows you to leverage AWS as a machine learning algorithm to basically detect when anything out of the ordinary is happening in terms of access or usage of your applications. If you have an application that typically only receives 100 calls per hour, and all of a sudden it's receiving 100,000 calls per hour! That can raise an insight event that you can capture and potentially create an alarm on in cloud watch if you want to. Another useful trait of Cloud Trail is that there are export tools that allow you to archive data to cold storage. You may have a compliance use case in your organization and you need to maintain all access to your AWS account over one year two years or 10 years. Cloudtrail gives you some very easy mechanisms to export that data into S3. From S3, you can put it into Glacier in a very low cost, retention for a very long timeframe.
    

With these three different types of events management data and insights, you can create separate trails that include different portions. You can have a trail that includes management data, another can include management and insights. And each of the different trails can have a different delivery destination, so you can get copies of the same data if you want to replicate it. It's meant for auditing access to your AWS accounts.

## [](https://azizulmaqsud-1684501031000.hashnode.dev/cloudwatch-vs-cloudtrail-two-interactive-watch-dogs-in-the-aws#heading-a-quick-summary-of-the-two "Permalink")**A quick summary of the two**

CloudWatch is a monitoring service for AWS applications to use primarily for log or metric analysis and also for the creation of alarms. And, for application health, Cloudtrail is a monitoring service for users and resources. It's useful for auditing or compliance purposes, and trails allow you to capture activity and deliver it rapidly to cold storage

Lastly, CloudWatch is primarily used for monitoring and managing the performance of your AWS resources, while CloudTrail focuses on providing an audit trail of API activity within your AWS account for governance, compliance, and security purposes.
# How CloudTrail works?

Your AWS account is automatically enabled for CloudTrail once it is created. CloudTrail events are created when activities occur in your AWS account. On the CloudTrail console, click on Event history to view events.

In your AWS account, you can view, search, and download the past 90 days of activity. To archive, analyze, and react to changes in AWS resources, you can create a CloudTrail trail. Using an Amazon S3 trail, you can send events to a bucket that you specify.

## You can create two types of trails for an AWS account:

## · A trail that applies to all regions

The CloudTrail event log files for all regions are delivered to an S3 bucket that you specify, when a trail is created that applies to all regions. If a region is added after you create a trail that applies to all regions, that new region is automatically included in the trail, and events in that region are logged. An all-regions trail is the default option when you create a trail in the CloudTrail console because it is a recommended best practice for capturing activity across all regions in your account. The AWS CLI is the only way to update a single-region trail to log all regions. For more information, see Creating a trail in the console (basic event selectors).

## · A trail that applies to one region:

If you create a trail that applies to a specific region, CloudTrail records the events only in that region. It then uploads the CloudTrail event logs to an Amazon S3 bucket that you specify. A single trail can only be created using the AWS CLI. If you create additional trails, the CloudTrail event logs will be delivered to the same Amazon S3 bucket or to separate buckets. Create, update, and manage trails with AWS CLI and CloudTrail API. For more information, see Creating, updating, and managing trails with AWS CLI and CloudTrail API.

## Difference between CloudWatch and CloudTrail :

CloudWatch monitors the health and performance of AWS services and resources.

CloudTrail keeps track of all actions that occur within your AWS environment.

## AWS CloudWatch :

AWS CloudWatch is a monitoring service for AWS cloud resources and applications. Amazon CloudWatch helps you collect and track metrics, collect and monitor log files, set alarms, and react automatically to changes in your AWS resources.

![](https://miro.medium.com/v2/resize:fit:875/1*mDOi5D3wTpNf21SVhniVZw.png)

AWS CloudWatch

## AWS CloudTrail :

CloudTrail is an AWS service for governance, compliance, operational auditing, and risk auditing. CloudTrail enables you to log, continuously monitor, and retain account activity across your AWS infrastructure. It provides an event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services.

![](https://miro.medium.com/v2/resize:fit:875/1*t3yLbGasKe74NohBmldSWw.png)

AWS CloudTrail

## Security in AWS CloudTrail?

AWS prioritizes cloud security above all else. Customers of AWS benefit from a data center and network architecture that is built to meet the needs of the most security-sensitive organizations.

Security is a shared responsibility between you and AWS. In the shared responsibility model, this is called security of the cloud and security in the cloud:

Cloud security — AWS is responsible for protecting the infrastructure that runs AWS services on the AWS Cloud. You can also use AWS services in a secure manner. The AWS compliance program regularly tests and verifies the effectiveness of our security through third-party auditors. See AWS Services in Scope by Compliance Program for information about compliance programs that apply to AWS CloudTrail.

Security in the cloud — Your responsibility depends on which AWS service you use. The sensitivity of your data, your company’s requirements, and applicable laws and regulations are also factors to consider.


---
# What is CloudTrail?

**_Records user’s activity in AWS accounts_**

![](https://miro.medium.com/v2/resize:fit:875/1*MFIMVRhpSg8Q3A-48Ilp9Q.png)

Screenshot from AWS

CloudTrail is a service that logs all API calls made to an AWS account and supports a wide range of AWS services.

It’s important to note that while CloudTrail captures activity from the console, SDK, or CLI, it does not log SSH/RDP activities since they communicate directly with the OS rather than the server.

## ✍️ Key points —

- **Enabled by default** when you create an AWS account
- **Records events** related to the creation, modification or deletion of resources ( IAM users, s3 buckets, EC2 instance)
- By default CloudTrail store the logs for **90 days**
- If the user wants to store for more than 90 days — Create a custom CloudTrail, the logs are saved indefinitely to an S3 bucket but the user will be charged
- Logs are secure by default, encrypted using **Server-side Encryption**
- **Log integrity validation** is also on by default -logs are digitally signed so the user can be detected if a log was changed or deleted
- **All Regions** — Trail created will apply to all regions
- **Not a real-time** — Logs the activity every 15 min and takes 5 min for logs to reach to s3 bucket

# Use Case 👨🏻‍💻

- Incident Investigation — After the fact investigation of incidents in your AWS accounts
- Security Analysis — Near real-time security analysis of user activity
- Compliance — Used to help meet industry, regulatory compliance, and audit requirements
- Audit trail — “When” , “Where” , “Who”, “What”, source IP, request parameters, and responses can be tracked.

## With CloudTrail now on our radar, let’s tackle each question one by one 🛰️

## 🔴 Question 1️⃣

What is AWS CloudTrail, and what types of events can it log?

**🟢 Answer**

AWS CloudTrail is a logging service that captures all API calls made to an AWS account, supporting a range of AWS services.

CloudTrail can send log files to Amazon S3 buckets for long-term storage and analysis. It enables monitoring, logging, and security analysis of AWS account activity, aiding in troubleshooting, compliance, and security monitoring.

_Types of events CloudTrail can log —_

1. **Amazon S3**: Bucket creation, deletion, or modification; object creation, deletion, or modification; access control changes; and changes to lifecycle policies.
2. **Amazon EC2**: Instance launches, stops, and terminations; changes to security groups and network interfaces; and modifications to Elastic Block Store (EBS) volumes.
3. **AWS Lambda**: Function creation, modification, or deletion; invocation of functions; and updates to function versions or aliases.
4. **Amazon RDS**: Instance creation, deletion, or modification; changes to security groups and parameter groups; and modifications to database instances and backups.
5. A**WS Identity and Access Management (IAM)**: Changes to user, group, and role policies; changes to permissions and access keys; and user and role sign-in events to the AWS Management Console.

## 🔴 Question 2️⃣

How can you ensure that CloudTrail logs are tamper-proof and secure?

**🟢 Answer**

There are five crucial steps that can be taken to make CloudTrail Logs tamper-proof and secure.

1. Restrict access to your CloudTrail logs using **AWS S3 bucket policies** and IAM roles. **Encrypt your logs** using server-side encryption (SSE).
2. Use AWS KMS to manage and **protect your encryption keys**. Periodically change your encryption keys with AWS KMS key rotation.
3. Enable AWS CloudTrail **log file integrity validation** to detect any unauthorized changes to your logs.
4. Set up **Amazon SNS notifications** to receive alerts when someone modifies, deletes, or reads your CloudTrail logs without authorization.
5. Enable CloudTrail **multi-region logging** to store your logs in multiple AWS regions, providing additional redundancy and resilience to your logging infrastructure.

## 🔴 Question 3️⃣

What is the difference between S3 and CloudWatch log storage options for CloudTrail?

**🟢 Answer**

- S3 is used for the long-term retention of log files, while CloudWatch is used for real-time monitoring and alerting of events.
- S3 is good for audit purposes, and CloudWatch is better for immediate analysis and response to events.
- The decision to use S3 or CloudWatch for CloudTrail logs will depend on your specific use case and requirements.

## 🔴 Question 4️⃣

Can you integrate CloudTrail with other AWS services, such as AWS Config or AWS Security Hub?

**🟢 Answer**

- Yes, CloudTrail can be integrated with other AWS services such as AWS Config or AWS Security Hub.
- By integrating with AWS Config, you can track changes to your resources and see how those changes were made.
- With AWS Security Hub, you can aggregate and prioritize security alerts and findings across multiple AWS accounts.

## 🔴 Question 5️⃣

How can you set up notifications or alerts based on specific events in CloudTrail logs?

**🟢 Answer**

In general, it is a 5-step process

1. Create an SNS topic.
2. Enable CloudTrail in your AWS account and select the types of events to log.
3. Create an Amazon CloudWatch log group and stream to collect CloudTrail logs.
4. Create a CloudWatch metric filter to extract the desired event from the CloudTrail logs.
5. Create a CloudWatch alarm to monitor the metric filter and trigger the SNS topic when a threshold is exceeded.

_You can customize the specific event, threshold, and notification settings based on your requirements in the metric filter._

## 🔴 Question 6️⃣

How can you use CloudTrail to track changes to AWS resource configurations over time?

**🟢 Answer**

- CloudTrail can be used to track changes to AWS resource configurations over time through its logging functionality.
- CloudTrail logs all AWS API calls made within an AWS account.
- To track changes to AWS resource configurations over time, you can use the CloudTrail console or API to search for specific events related to resource configuration changes.
- You can filter your search results by resource type, date range, or event type to quickly find the events based on your requirements.
- The results will provide details such as the user who made the change, the time it was made, and the new and old values of the resource’s configuration.
- By tracking changes to AWS resource configurations over time, you can identify when and how changes were made detect unauthorized modifications.

## 🔴 Question 7️⃣

What is the process for enabling CloudTrail for a new AWS account?

**🟢 Answer**

Enabling CloudTrail in an AWS Account is a 5-step process.

1. In CloudTrail, Click on the “Create trail”
2. Name the trail and select the AWS S3 bucket where you want the log files to be stored.
3. Specify the regions you want to monitor for API events by selecting them from the drop-down menu.
4. Choose whether to log data events, management events, or both.
5. Configure any additional settings, such as encryption or advanced event selectors, based on the use case and hit Create

_Once the trail is created, it will start logging API events for the specified regions and services._

## 🔴 Question 8️⃣

How can you troubleshoot issues with CloudTrail logging or delivery?

**🟢 Answer**

To troubleshoot any issues related to CloudTrail logging or delivery, you can follow these steps to rule out each possible factor that might be causing the issue.

1. Verify that CloudTrail is enabled for the AWS account and that the appropriate regions and monitored.
2. Check the CloudTrail log files in the S3 bucket to ensure that they are being delivered and are not empty.
3. Confirm that the IAM user or role being used to access the AWS resources has the necessary permissions to write to the S3 bucket and publish to any other services being used.
4. Check the CloudTrail event history in the AWS Management Console to see if any errors or warnings have been reported.
5. Use the AWS CloudTrail Insights feature to quickly identify and investigate event delivery or abnormal activity issues.
6. Review the AWS CloudTrail API activity history to check for any potential errors or anomalies in API calls.

## 🔴 Question 9️⃣

Can you use CloudTrail to audit user activity within an AWS account? If so, how?

**🟢 Answer**

**Yes**, you can use CloudTrail to audit user activity within an AWS account. CloudTrail records API calls made to AWS services.

By analyzing CloudTrail logs, you can identify which user or service made a particular change, when it was made, and from which IP address or other source the request was made.

To audit user activity using CloudTrail, you can start by creating a trail that logs all the API activity within your account. You can then use tools like **Amazon Athena** or **Amazon QuickSight** to analyze and visualize the data collected by CloudTrail.

CloudTrail can be integrated with **AWS Config** and can help you assess compliance with internal policies by detecting configuration changes made to AWS resources.

AWS CloudWatch can be used to monitor CloudTrail logs in real time and alert you to any suspicious activity.

## 🔴 Question 🔟

How can you use CloudTrail to identify potential security risks or compliance issues within an AWS environment?

**🟢 Answer**

By reviewing CloudTrail logs, you can track and analyze user activity and resource changes within the account.

To identify potential _security risks_, you can look for unusual or suspicious activity in the CloudTrail logs, such as **unexpected API calls** or **changes to critical resources**. You can also use CloudTrail to **monitor and alert** you on specific events or patterns of activity that may indicate a security threat.

To identify _compliance issues_, you can use CloudTrail to monitor whether certain **compliance controls are being enforced**, such as **access controls**, **encryption**, or **resource configurations**. You can also use CloudTrail to **audit user activity** and ensure that it aligns with compliance requirements.







