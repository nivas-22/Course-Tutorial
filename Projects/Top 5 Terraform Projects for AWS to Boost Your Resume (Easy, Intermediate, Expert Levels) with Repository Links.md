
In this blog, I will share some of the projects I have completed during my Terraform learning journey. I hope they will be useful for you as well. You can use the provided repository link for each project to learn about how to deploy the project. Additionally, the Terraform HCL code for every project is available in the repository, making it easy for you to fork and deploy effortlessly.

# 1. AWS S3 Static Website Hosting using Terraform

![](https://miro.medium.com/v2/resize:fit:1400/1*sWFmJFlMxHOtf1bGzFilyA.png)

**Project Level:** Intermediate

**Project Description:**

In this project, We are going to develop a streamlined infrastructure for hosting a static website using Terraform and Amazon Web Services (AWS) S3. The primary goal of this project is to demonstrate the automated provisioning and deployment of a web hosting solution for static websites.

**GitHub Repo Link**: [Click here](https://github.com/mathesh-me/static-website-hosting-1)

# 2. Automatic application deployment in AWS using Terraform

![](https://miro.medium.com/v2/resize:fit:1400/1*kqiW8KDAGYoH08VBeWJShQ.png)

**Project Level:** Easy

**Project Description:**

In this project, We are going to leverage the power of Terraform Provisioners and AWS to create an automated and consistent deployment pipeline for applications on Amazon EC2 instances. This project is an automation solution designed to simplify the deployment of applications on AWS EC2 instances. In this project, I am going to deploy a simple flask application.

**GitHub Repo Link:** [Click here](https://github.com/mathesh-me/application-deployment-in-aws-terraform-provisioner)

# 3. Two-Tier AWS Architecture using Terraform

![](https://miro.medium.com/v2/resize:fit:1400/1*qoLCdDIcRGQwpFjcZGhSNQ.png)

**Project Level:** Intermediate

**Project Description**

This project aims to create a robust highly available web application infrastructure using a two-tier architecture on Amazon Web Services (AWS). The architecture comprises a web tier that handles user requests and a database tier for data storage. I leveraged Terraform for Infrastructure as Code (IaC) to provision and manage AWS resources efficiently.

**GitHub Repo Link**: [Click here](https://github.com/mathesh-me/two-tier-architecture-aws-using-terraform)

# 4. Deploying High-Availability One-Tier AWS Architecture with Terraform and Jenkins

![](https://miro.medium.com/v2/resize:fit:1400/1*UXUiK0rPQ89O2IFT4UXzig.png)

**Project Level:** Between Intermediate and Hard

**Project Description 📄**

This project automates the deployment of a high-availability AWS architecture using Terraform and Jenkins. The architecture consists of an Auto Scaling Group and an Application Load Balancer, all deployed within a separate VPC.

The project is divided into two parts:

- Part 1: Committing Terraform configuration code HCL in GitHub.
- Part 2: Deploying the application to the AWS infrastructure using Jenkins through the HCL code in GitHub.

**GitHub Repo Link:** [Click here](https://github.com/mathesh-me/high-availabilty-deployment-terraform)

# 5. Multi-Tier Architecture on AWS using Terraform

![](https://miro.medium.com/v2/resize:fit:1400/1*qlsHYDgBaYs73Pkb4dFphQ.png)

**Project Level:** Expert

**Project Description:**

Deploy a scalable and resilient multi-tier architecture on AWS using Terraform.

**Project Overview**

This project allows us to deploy a highly available, scalable, and secure multi-tier architecture on Amazon Web Services (AWS) using Terraform. The architecture consists of the following three tiers:

- **Web Tier:** This tier handles incoming user requests and can be horizontally scaled for increased capacity. It typically includes web servers and a load balancer for distributing traffic.
- **Application Tier:** Application servers run our business logic and interact with the database tier. They can also be horizontally scaled to meet demand.
- **Database Tier:** The database stores and manages our application data. In this architecture, we use Amazon RDS for a managed database service.

**GitHub Repo Link:** [Click here](https://github.com/mathesh-me/multi-tier-architecture-using-terraform)