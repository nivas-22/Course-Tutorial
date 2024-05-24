
AWS Identity and Access Management (or IAM) is a service that offers secure access control mechanisms for all of your AWS services and in some cases resources. AWS IAM is at the heart of AWS security because it empowers you to control access by creating users and groups, assigning specific permissions and policies to specific users, setting up multi-factor authentication for additional security, and so much more. And the cherry on top, IAM is free to use!

In this article, we will demystify the fundamentals of AWS IAM to offer you a complete overview of IAM, help you identify its unique benefits, and learn how to start empowering users to safeguard your AWS accounts. We will walk through key features, latest updates, and how to configure simple and important features such as MFA, and other best practices. Let’s get started!

# AWS IAM in a Nutshell

Security in the Cloud remains one of the biggest barriers to Cloud adoption. For SecOps and SysOps teams, it becomes paramount to follow security best practices to ensure a smooth transition with a strong foundation. With all the scrutiny and public attention surrounding major Cloud platforms, it’s admirable that **AWS IAM follows an incredibly granular approach** in providing permissions and access control within your environments. IAM lets you control who can use your resources (authentication) and in which ways (authorization). This is why it’s possible to create exceedingly secure environments using AWS.

![](https://miro.medium.com/v2/resize:fit:160/0*lFvEzlyhBAIL3x4W)

## AWS IAM — Key Features

We should think of IAM as the first step towards securing all your AWS services and resources. Let’s look at some of the key features that make IAM so versatile and powerful:

- **Authentication:** AWS IAM lets you create and manage identities such as users, groups, and roles, meaning you can issue and enable authentication for resources, people, services, and apps within your AWS account. In the next section, we’ll look at authentication in detail.
- **Authorization:** Access management or authorization in IAM is made of two primary components: **Policies** and **Permissions**. In the next section, we’ll also look at each of these.
- **Fine-grained permissions:** Consider this — you want to provide the sales team in your organization access to billing information, but also need to allow the developer team full access to the EC2 service, and the marketing team access to selected S3 buckets. Using IAM, you can configure and tune these permissions as per the needs of your users.
- **Shared access to AWS accounts:** Most organizations have more than one AWS account, and at times need to delegate access between them. IAM lets you do this without sharing your credentials, and more recently, AWS released [ControlTower](https://aws.amazon.com/controltower/) to further simplify multi-account configurations. We also published a quick, hands-on tutorial on [Securing Multi-Account Access on AWS](https://blog.runpanther.io/secure-multi-account-aws-access/).
- **AWS Organizations:** For fine-grained control for multiple AWS accounts, you can use [AWS Organizations](https://aws.amazon.com/organizations/) to segment accounts into groups and assign permission boundaries.
- **Identity Federation:** Many times, your organization will need to federate access from other identity providers such as Okta, G Suite, or Active Directory. IAM enables you to do this with a feature called [Identity Federation](https://aws.amazon.com/about-aws/whats-new/2011/08/03/Announcing-IAM-Identity-Federation/).

# Authentication in IAM

Authentication or identity management in AWS IAM consists of the following identities:

1. **Users:** An IAM user is a person that needs to interact with your AWS resources or services either from the AWS Console or with the AWS CLI. When you create a new user, no credentials are assigned, and the user does not have any permission to access your AWS resources.
2. **Groups:** An IAM group is a collection of users and permissions assigned to those users. Groups provide a convenient way to manage permissions for users with similar needs by categorizing them according to their job function/role, department, or any other requirement. Then, permissions for all those users can be managed at once through the group.
3. **Roles:** An IAM role is an entity within AWS which defines a set of permissions the role can perform, and what entities can assume the role. A role is not directly linked to a person or a service, rather it can be assumed by any resource that the role grants permission to. Role credentials are always temporary and rotated periodically by the AWS Session Token Service (STS). For this reason, it is recommended to use roles over directly granting user or group permissions. Additionally, Roles allow you to grant multi-account access to your AWS resources from users, services, and apps that aren’t part of your business. The concepts of users and groups will be familiar to most system administrators, but IAM Roles can often be unfamiliar. Let’s dive into more details below.

IAM roles fulfill a unique and powerful niche in the identity and access management landscape. Instead of assigning permissions to an entity directly, roles allow an entity to be granted permissions temporarily (on an as-needed basis) to perform tasks. This enforces the least privilege principle which is based on both identity and time, as you can restrict entities to both the minimum amount of access needed as well as the minimum amount of time needed to complete a task.

Consider this: an administrator in your organization accidentally issues a command to delete a production resource. In an environment where permissions are controlled entirely with users and groups, this command would go through. On the contrary, in an environment controlled with roles, this command would only go through if the administrator had recently assumed the **DeleteProductionResources** role, or something similar. This allows services and users to have the capability to do everything their tasks require while minimizing the risk of compromised credentials and systems.

# Authorization in IAM

Authorization or access management in IAM is controlled by **Policies** that grant **Permissions**.

## What is a Policy?

A policy is a document with a set of rules, having one or more statements. Each policy grants a specific set of permissions and can be attached to any of the IAM identities we covered earlier — users, groups, and roles. Policies are always written in JSON or YAML format and each policy has a name.

There are two types of policies you should know about:

1. **Managed policies:** Managed policies can be created and attached to multiple entities. AWS has built-in managed policies that cover a wide variety of use cases. Managed policies can also be mixed and matched to provide generalized access to roles, users, or groups. AWS customers can also create their own managed policies.
2. **Inline policies:** These policies are directly applied to IAM entities, and do not have distinctive ARNs. You use inline policies for a specific objective, which makes them non-reusable.

AWS recommends the use of managed policies instead of inline policies so that permissions are more standardized and can be reused.

## What are Permissions?

Permissions enable you to perform actions on AWS resources. When a new user or group is created, it has no permissions and a policy must be attached to allow actions to be taken on AWS resources.

You can assign permissions to all AWS identities (users, groups, and roles). Permissions are assigned in the following two ways:

- **Identity-based**: Policies attached directly to users, groups, or roles
- **Resource-based**: Policies attached to AWS resources, such as S3 Buckets, ECR Repositories, and more

When writing new policies, the following resources can be helpful:

- [Manage IAM Permissions](https://aws.amazon.com/iam/features/manage-permissions/): This page offers quick reference to help you assign and manage IAM permission
- [Actions, Resources, and Condition Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html): A comprehensive reference to all possible actions that can be taken on various AWS services
- [AWS Policy Simulator](https://policysim.aws.amazon.com/home/index.jsp?#): Validate that newly created policies work end-to-end by creating access simulations

Generally, policies should follow the principle of least privilege, which means only the absolute minimum set of access should be granted to get the job done. Policies can be extremely specific — consider the following code block, for example:

```copy
{  
  "Version": "2012-10-17",  
  "Statement": [  
    {  
      "Action": [  
        "iam:ChangePassword",  
        "iam:CreateLoginProfile",  
        "iam:DeleteLoginProfile",  
        "iam:GetLoginProfile",  
        "iam:GetUser",  
        "iam:UpdateLoginProfile"  
      ],  
      "Resource": "arn:aws:iam::*:user\/${aws:username}",  
      "Effect": "Allow",  
      "Sid": "AllowManageOwnPasswords"  
    }  
  ]  
}
```

Or policies can be broadly defined, such as in the following code block:

```copy
{  
  "Version": "2012-10-17",  
  "Statement": [  
    {  
      "Action": [  
        "iam:*"  
      ],  
      "Resource": "*",  
      "Effect": "Allow",  
      "Sid": "IAMAdmin"  
    }  
  ]  
}
```

Finding the right balance is important, as overly granular policies lead to undue overhead, and overly broad policies can lead to inappropriate access, which is a major factor in security breaches. Following the principle of least privilege can go a long way in ensuring that only a minimal amount of damage occurs during unexpected security events.

# Hands-On Examples

The threat landscape changes rapidly, which is why it’s more important than ever before to continuously tighten your security practices. Great security practices in the cloud are often the simplest of steps designed around access management and control. Let’s jump into two such quick tutorials that will allow you to enforce water-tight password policies and help set up multi-factor authentication to strengthen your organization’s overall security posture.

## Setting up a password policy for your AWS Account using IAM

In this section, we’ll help you set up your AWS account password policy.

1. Navigate to the AWS IAM console and click on **Account settings** as shown here:

![](https://miro.medium.com/v2/resize:fit:358/0*hFcfUInVeve90cNH)

2. Next, click on the **Set password policy** button

![](https://miro.medium.com/v2/resize:fit:820/0*nu4EQXQOe8ZwkC-u)

3. You can now set up your password policy by defining a set of rules and selecting the complexity requirements for the password an IAM user can set. The example below meets the standards recommended by the Center for Internet Security (CIS):

![](https://miro.medium.com/v2/resize:fit:875/0*fJa233kgtREo5Su6)

## Setting up Multi-Factor Authentication (MFA) using AWS IAM

Multi-Factor Authentication (MFA) protocols offer a great way to improve the overall security posture of your AWS cloud services and resources. This simple step could even prove instrumental in preventing costly breaches for your organization. In this tutorial, we will show you how to set up MFA using a mobile device.

1. Go to the AWS console, and select your username in the top right corner
2. In the dropdown menu, select the **My Security Credentials** button

![](https://miro.medium.com/v2/resize:fit:239/0*efqBAz6f4INy2fhb)

3. Scroll down the page until you reach the section titled **Multi-factor authentication (MFA)**, then select the **Assign MFA Device** button

![](https://miro.medium.com/v2/resize:fit:875/0*6Vnm1jlJu3aKD4VF)

4. Select virtual or hardware MFA device as appropriate

4a. If a virtual MFA device was selected, scan the QR code with your MFA app (such as Duo Mobile, Google Authenticator, Microsoft Authenticator, etc.) and input two subsequent codes. Select the **Assign MFA** button and you’re all set!

![](https://miro.medium.com/v2/resize:fit:875/0*uVKTJVIg0AS6VO1S)

4b. If instead, you wish to use a hardware MFA device (such as a [yubikey](https://www.yubico.com/)) for additional security, you will be prompted to insert the MFA device and tap the button. Your web browser may inform you that aws.amazon.com is requesting information about your hardware device. If so, grant it. Now your hardware MFA device is ready to go.

![](https://miro.medium.com/v2/resize:fit:875/0*-KrM02PQkZp98HJM)

# What’s New in AWS IAM?

During re:Invent 2019 earlier this month, AWS announced a new feature to IAM — AWS Identity and Access Management [(IAM) Access Analyzer](https://aws.amazon.com/about-aws/whats-new/2019/12/introducing-aws-identity-and-access-management-access-analyzer/?trk=ls_card). The AWS Identity and Access Management Access Analyzer offers an additional level of security that lets you continuously examine and analyze permissions given using policies for all organization’s resources — IAM roles, Amazon S3 buckets, AWS KMS keys, Lambda functions, and SQS queues. Before we dig into what Access Analyzer does, let’s understand what triggered its release.

With increased scrutiny surrounding customer data leaks and recent high-profile episodes of [Capital One breach](https://krebsonsecurity.com/tag/capital-one-breach/) that allowed misconfigured access, and [Attunity Leaks](https://searchcloudsecurity.techtarget.com/news/252465992/Another-Amazon-S3-leak-exposes-Attunity-data-credentials) which exposed Amazon S3 buckets data from top clients (Netflix, Ford, and TD Bank), Access Analyzer was just the tool everyone was anticipating.

Another [announcement](https://aws.amazon.com/about-aws/whats-new/2019/12/aws-security-hub-integrates-with-the-aws-identity-and-access-management-iam-access-analyzer/) concerning admins and SecOps teams was that of direct integration capabilities between AWS Security Hub and AWS IAM Access Analyzer to send detailed findings when policies allow public or external access to resources.

# What AWS IAM Access Analyzer can do?

IAM Access Analyzer helps you generate a comprehensive report for all your AWS resources that could be accessed publicly i.e. outside of AWS accounts. This also includes “service last accessed” data which essentially is a timestamp of what resources and services were accessed by which users and roles. By using Access Analyzer, admins can examine thousands of policies in their environments in a matter of seconds. Access Analyzer is part of Amazon’s [Provable Security](https://aws.amazon.com/security/provable-security/) efforts to achieve the highest levels of security using automated reasoning technology and mathematics logic.

IAM Access Analyzer (also includes [Access Analyzer for Amazon S3](https://aws.amazon.com/about-aws/whats-new/2019/12/introducing-access-analyzer-for-amazon-s3-to-review-access-policies/), had its separate press release) is in line with the overall ethos of AWS IAM service, meaning it involves no additional cost and is included as part of the IAM console.

# IAM Best Practices you should know

Before we wrap up, let’s review some of the best practices you will find useful to help secure your AWS resources:

- **Avoid the use of root account unless strictly necessary:** Do not use the root account for day to day administration activities. By default, the root account user has access to all resources for all AWS services and it’s best practice to create IAM users with least privilege access. Additionally, do not create access keys for the root account unless strictly necessary. Finally, set up monitoring to detect and alert on root account activity, and ensure hardware-based MFA is set up for root account access.
- **Use temporary credentials:** Never share your credentials with anyone. It’s advisable to create individual users for anyone who has access requirements and even better use temporary credentials. Dynamically generated credentials that expire after a configurable interval, are a great way to tackle this. You can visit our practical tutorial on [Securing Multi-Account Access on AWS](https://blog.runpanther.io/secure-multi-account-aws-access/) for detailed instructions on this.
- **Embrace the least privilege principle and review all IAM permissions periodically:** It is important to follow the security principle of least privilege, which means that if a user doesn’t need to interact with a resource, then it is best not to provide them access to that resource. IAM permissions allow for very granular access controls, so avoid the use of policy statements that grant access to all actions, all principals, or all resources. Additionally, use the IAM Access Advisor regularly to ensure that all permissions assigned to a particular user are indeed being used.
- **Enforce the least privilege principle to be implemented bi-directionally**: Many AWS resources (such as S3 buckets) can have their access policy attached directly. Don’t fall into the trap of thinking that because access is tightly controlled in one direction (i.e. an IAM Role that grants very specific permissions), that you should be less rigid in the other direction (for example, when an S3 bucket access policy grants read access to all entities in your account). Optimally use both sides of the least privilege principle to achieve favorable outcomes.
- **Monitor account activity regularly using IAM Access Analyzer and AWS CloudTrail:** In addition to what we discussed about the newly released IAM Access Analyzer, the good old AWS CloudTrail is an excellent tool to monitor all activities in your account. You can easily use CloudTrail logs to identify suspicious activity and take necessary actions depending on your findings. You will find our deep-dive, practical tutorial on [AWS Security Logging with CloudTrail](https://blog.runpanther.io/aws-cloudtrail-fundamentals/) interesting with step by step instructions to help you do this.
- **Use Multi-Factor Authentication (MFA)**: Enable MFA to build an additional layer of security for interaction with the AWS API.
- **Enforce strong passwords:** Enforce strong passwords by configuring account password policy that involves password rotation, discourages the use of old passwords, only allows alphanumeric characters, and more.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1705593027115/a6c9e0a0-3d1b-46e5-9fa4-451cbb5e07ff.png?auto=compress,format&format=webp)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1705592569133/fdc66b56-2e0c-4a0d-8ec1-f3f952d0561c.png?auto=compress,format&format=webp)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1705592676256/f0563c0a-310e-4f03-9fcb-1ee04e695830.png?auto=compress,format&format=webp)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1705592732581/0fe8483c-1eb2-4c5e-8c3d-94a8bdb968ff.png?auto=compress,format&format=webp)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1705592766223/9b6a6dfd-c909-4c41-b636-61ceb820196f.png?auto=compress,format&format=webp)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1705592797799/c3e68372-d14d-4b05-9f4d-33dd40a23b33.png?auto=compress,format&format=webp)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1705592814974/9de79b65-3ff7-48a4-8356-9363738bc08a.png?auto=compress,format&format=webp)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1705592837867/7edd3f4d-bada-4ce3-ac5b-c838987df3fd.png?auto=compress,format&format=webp)