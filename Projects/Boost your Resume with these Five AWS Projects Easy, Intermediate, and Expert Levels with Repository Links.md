
In this blog, I will share some of the projects I have completed during my AWS learning journey. I hope they will be useful for you as well. You can use the provided repository link for each project to learn about how to deploy the project. Additionally, the code for every project is available in the repository, making it easy for you to fork and deploy effortlessly.

I am an AWS Certified Solutions Architect, AWS Certified Developer Associate, and AWS Certified Cloud Practitioner. So you can trust that these projects will also aid in your learning journey.

# 1. Automated Image Resizing and Transfer System Using AWS Services

![](https://miro.medium.com/v2/resize:fit:1400/1*lE4v7YnLst-7FewSYDKevQ.png)

**Project Level**: Intermediate

**Project Description:**

This project focuses on building an automated system for image processing and management within the AWS ecosystem. The goal is to streamline the handling of images by automatically resizing them and transferring them to a designated storage location while keeping stakeholders informed through notifications. Key AWS services, such as Lambda, S3, and SNS, are used to orchestrate this workflow.

**GitHub Repo Link:** [Click here](https://github.com/mathesh-me/image-resizing-using-s3-lambda-sns)

# 2. Efficient AWS Cost Management through Stale Resource Detection

![](https://miro.medium.com/v2/resize:fit:598/1*2uhEC0wiOtXNUd9ucDaK2w.png)

Certainly, including this project on your resume would be advantageous. In Below Descriptions You can find What is the Problem and its Corresponding Solution.

**Project Level:** Intermediate

**Problem :**

Sometimes, developers create EC2 instances with volumes attached to them by default. For backup purposes, these developers also create snapshots. However, when they no longer need the EC2 instance and decide to terminate it, they sometimes forget to delete the snapshots created for backup. As a result, they continue to incur costs for these unused snapshots, even though they are not actively using them.

**Solution :**

We’re using AWS to save money on storage costs. We made a Smart Lambda function that looks at our snapshots and our EC2 instances. If Lambda finds a snapshot that isn’t connected to any active EC2 instances, it deletes it to save us money. This helps us keep our AWS costs down.

**Note :**

There are many similar problems like this. For instance, we might attach an Elastic IP to our EC2 instance but forget to delete the Elastic IP after terminating the EC2 instance. In such a case, the Elastic IP continues to incur costs for us. This Project is One of the use case. You can Easily Develop this Project by Forking the Below Repo.

GitHub Repo Link: [Click here](https://github.com/mathesh-me/aws-cost-optimization)

# 3. Serverless EC2 Instance Scheduler for Company Working Hours

![](https://miro.medium.com/v2/resize:fit:1400/1*H24pNYnn1_SILutOeAQc0A.png)

**Project Level:** Easy

This Project is Simple, But it is Based on Real life Scenario.

**Scenario :**

In some companies, there is no need to run their EC2 instances 24/7; they require instances to operate during specific time periods, such as company working hours, from 8:00 AM in the morning to 5:00 PM in the evening. To address this scenario, I will implement two Lambda functions responsible for starting and stopping instances. These Lambda functions will be triggered by two CloudWatch Events in the morning and evening. This solution is fully serverless.

**GitHub Repo Link:** [https://github.com/mathesh-me/serverless-ec2-scheduler](https://github.com/mathesh-me/serverless-ec2-scheduler)

# 4. Secure VPC Architecture with Public and Private Subnets for Production Environment

![](https://miro.medium.com/v2/resize:fit:1222/1*HQQhqniNM-8Oor72ZxeLlw.png)

**Project Level:** Intermediate

**Project Overview :**

This project’s overview is depicted in the diagram below. The setup revolves around a Virtual Private Cloud (VPC) featuring both public and private subnets, thoughtfully distributed across two Availability Zones to ensure reliability.

Within each public subnet, there’s a NAT gateway to facilitate outbound internet connectivity and a load balancer node for effective traffic distribution.

On the other hand, the project’s servers reside in the private subnets. Their deployment and termination are automated through an Auto Scaling group, allowing them to dynamically adapt to workload changes. These servers play a pivotal role in receiving traffic from the load balancer and can access the internet through the NAT gateway when necessary

GitHub Repo Link: [Click here](https://github.com/mathesh-me/aws-public-private-subnet-architecture)

# 5. Multi-Tier Architecture on AWS using Terraform

![](https://miro.medium.com/v2/resize:fit:1400/0*hBmivFqfwQ1Ykrd_.png)

**Project Level:** Expert

**Note:** Actually I deployed this Multi-tier Architecture using Terraform which is little bit Advanced than doing it in AWS Console. If you need help in Console then Comment below or You can also Message me on LinkedIn.

**Project Description:**

Deploy a scalable and resilient multi-tier architecture on AWS using Terraform.

**Project Overview**

This project allows us to deploy a highly available, scalable, and secure multi-tier architecture on Amazon Web Services (AWS) using Terraform. The architecture consists of the following three tiers:

- **Web Tier:** This tier handles incoming user requests and can be horizontally scaled for increased capacity. It typically includes web servers and a load balancer for distributing traffic.
- **Application Tier:** Application servers run our business logic and interact with the database tier. They can also be horizontally scaled to meet demand.
- **Database Tier:** The database stores and manages our application data. In this architecture, we use Amazon RDS for a managed database service.

**GitHub Repo Link:** [Click here](https://github.com/mathesh-me/multi-tier-architecture-using-terraform)