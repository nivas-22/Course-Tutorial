> Building an end-to-end CI/CD pipeline for Django applications using Jenkins, Docker, Kubernetes, EKS, ArgoCD, GitHub Actions, AWS EC2, and Terraform can be quite a robust setup. In this article, we will guide you through setting up a comprehensive CI/CD pipeline using AWS EC2, AWS EKS, Jenkins, Github actions, Docker, trivy scan, SonarQube, ArgoCD, Kubernetes cluster of your choice, and terraform

![Technical Guide: End-to-End CI/CD DevOps with Jenkins, Docker, Kubernetes, ArgoCD, Github Actions , AWS EC2 and Terraform by joel otepa wembo](https://miro.medium.com/v2/resize:fit:875/1*rlPRYAfJ_aFOfoj52U7y2A.png)

Technical Guide: End-to-End CI/CD DevOps with Jenkins, Docker, Kubernetes, ArgoCD, GitHub Actions, AWS EC2 and Terraform

# Preface

This guide is designed to walk you through the entire process of setting up an end-to-end CI/CD pipeline using a myriad of industry-leading technologies. From automating builds and tests to seamlessly deploying your application in a Kubernetes cluster, we cover it all.

Whether you’re a seasoned DevOps engineer looking to refine your skills or a developer eager to embrace modern deployment practices, this guide caters to all skill levels.

> **_To enhance readability_**_, this article is divided into chapters and split into series. The second part,_ **_“_**[**DevOps hands-on Lab: How to Provision and Monitor EKS Cluster using Prometheus and Grafana deployed via Helm charts**](https://towardsaws.com/devops-hands-on-lab-how-to-provision-and-monitor-eks-cluster-using-prometheus-and-grafana-helm-740abfc6b805)**_”_** _will be covered in a separate article to keep the reading time manageable and ensure focused content._

# Acknowledgment

We extend our appreciation to the open-source communities, whose collaborative spirit and dedication have been instrumental in the advancement of tools like _Terraform_ and the broader _DevOps_ ecosystem.

# Abstract

DevOps automation is the addition of technology that performs tasks with reduced human assistance to processes that facilitate feedback loops between operations and development teams so that iterative updates can be deployed faster to applications in production.

DevOps automation plays a pivotal role in modern software development and deployment. Automation streamlines repetitive and manual DevOps tasks, allowing them to be executed without human intervention.

_By automating processes across the DevOps lifecycle — such as design, development, deployment, and monitoring — teams achieve greater efficiency and consistency._

![](https://miro.medium.com/v2/resize:fit:875/0*Lm4DdT6rpSAl155_)

# Table of Contents

· [Preface](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#cb63)  
· [Acknowledgment](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#06fa)  
· [Abstract](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#7cec)  
· [Table of Contents](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#34d3)  
· [Introduction](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#967a)  
· [Prerequisites:](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#0a13)  
· [Why Jenkins?](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#2e6b)  
· [1. Create AWS Access Keys](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#0806)  
· [2. Set Up Custom Domain](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#065e)  
· [3. Create Route53 Hosted Zone](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#17b4)  
· [4. Code your Django application](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#b1c8)  
· [5. Dockerize the Django application](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#15a0)  
· [6. AWS EC2 Provisioning Using Terraform and GitHub Actions](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#5e59)  
· [7. Create a Key Pairs](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#dd4d)  
· [8. backend.tf](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#f20d)  
· [8.1 S3 bucket for terraform state management](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#e7cb)  
∘ [Replace remote backend with Terraform Cloud](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#0a8c)  
· [8.2 Terraform Cloud Configuration](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#9a7f)  
· [9. provider.tf](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#9c6e)  
· [10. variable.tf](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#0681)  
· [11. main.tf](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#3cf2)  
· [12. Validate and Test your first solution](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#3568)  
· [13. Complete your Jenkins installations](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#5455)  
· [14. Create a new Jenkins Job](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#a9d9)  
∘ [Advantages of using Jenkins](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#884f)  
∘ [Disadvantages of using Jenkins](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#7ae1)  
· [15. Kubernetes Orchestration & Continuous Delivery with ArgoCD](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#d85d)  
· [16. Check the result using your aws ec2 terminal and aws management console](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#79e1)  
· [17. Continuous Delivery with ArgoCD](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#953b)  
∘ [Step 5: ArgoCD Load Balancer in EKS](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#82e9)  
∘ [Step 6: Let access the AWS EKS ArgoCD GUI](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#3ea8)  
· [18. Integrate Django APIs with AWS API Gateway with a custom domain](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#bc34)  
· [Clean up Cluster](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#8378)  
· [Summary](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#ab5d)  
· [About me](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#c99b)  
· [References](https://medium.com/django-unleashed/technical-guide-end-to-end-ci-cd-devops-with-jenkins-docker-kubernetes-argocd-github-actions-fee466fe949e#e9f5)

# Introduction

In this article, we will guide you through setting up a comprehensive CI/CD pipeline using AWS EC2, AWS EKS, Jenkins, Github actions, Docker, trivy scan, SonarQube, ArgoCD, Kubernetes cluster of your choice, and terraform. It covers provisioning an EC2 instance using Terraform, managing terraform state using Terraform cloud, installing/configuring Jenkins, and SonarQube, adding credentials, installing Docker, building Django images for dev and production, building pipelines, deploying with ArgoCD in Kubernetes, and performing cleanup. By following this technical guide, you’ll gain hands-on experience in automating the build, test, and deployment processes of your applications.

Building an end-to-end CI/CD pipeline for Django applications using Jenkins, Docker, Kubernetes, ArgoCD, GitHub Actions, AWS EC2, and Terraform can be quite a robust setup. Here’s a high-level overview of how you might set it up:

1. **Initial environment setup:**

- Register your AWS Account
- Register your domain name
- Create AWS Key Pairs
- Create AWS Access Keys
- Setup Django Application
- Dockerize the Django Application

**2. GitHub Repository Setup:**

- Create a GitHub repository for your Django application.
- Add your Django code to this repository.

**3. Continuous Integration with GitHub Actions**:

- Configure GitHub Actions workflows to run tests, linting, and other checks on every push or pull request.
- Utilize Docker containers for consistency across different environments.

4. **Infrastructure Provisioning with Terraform**:

- Define infrastructure requirements using Terraform.
- Provision necessary AWS resources (like EC2 instances, VPC, subnets, etc.) for the Jenkins server, Kubernetes cluster, and any other required services.

5. **Continuous Deployment with Jenkins**:

- Set up Jenkins on a server (can be an AWS EC2 instance).
- Configure Jenkins pipelines to:
- Automatically trigger on successful CI builds.
- Build Docker images for your Django application.
- Push these Docker images to a Docker registry (e.g., Docker Hub, AWS ECR).
- Deploy Docker images to Kubernetes clusters using the Kubernetes plugin for Jenkins.

**6. Kubernetes Orchestration:**

- Set up a Kubernetes cluster on AWS using tools like Kops, EKS, or even Terraform itself.
- Deploy your Django application using Kubernetes manifests.
- Utilize Helm charts for managing complex deployments.

**7. Continuous Delivery with ArgoCD:**

- Install and configure ArgoCD on your Kubernetes cluster.
- Set up GitOps workflows by syncing Kubernetes manifests from a Git repository (where your Kubernetes manifests are stored).
- ArgoCD will continuously monitor the Git repository for changes and automatically apply them to the Kubernetes cluster, ensuring your application is always up-to-date.

**8.** [**Monitoring and Logging**](https://joelotepawembo.medium.com/devops-hands-on-lab-how-to-provision-and-monitor-eks-cluster-using-prometheus-and-grafana-helm-740abfc6b805)**:**

- Implement monitoring and logging solutions such as Prometheus, Grafana, and ELK stack to monitor the health and performance of your Django application and infrastructure.
- Add Slack Notification

**9. Security Considerations:**

- Implement security best practices throughout the pipeline, including secure storage of secrets and credentials, network security, and container security.

**10. Setting Up Custom domain names for our Django Rest APIs**

**11. Integrate Django APIs with AWS API Gateway with a custom domain**

**12. Documentation and Maintenance:**

- Document the setup, configuration, and maintenance processes to ensure that the pipeline can be easily understood and maintained by your team.

This setup will provide you with a comprehensive CI/CD pipeline for your Django application using Jenkins, terraform, Docker, and Kubernetes, from code commit to deployment, with automation at every step. However, keep in mind that setting up such a complex pipeline requires careful planning, configuration, and ongoing maintenance.

![](https://miro.medium.com/v2/resize:fit:875/1*jaG-MWIg7iEpjUI0NHBx_A.png)

Jenkins CI/CD

# Prerequisites:

Before we get into the good stuff, first we need to make sure we have the required services on our local machine or dev server, which are:

1. Basic knowledge of [Django](https://www.djangoproject.com/)
2. [AWS Account](http://aws.com/)
3. [GitHub Account](https://github.com/)
4. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) installed and configured.
5. [EKS CLI](https://docs.aws.amazon.com/cli/latest/reference/eks/)
6. [Docker](https://docs.docker.com/desktop/install/windows-install/) installed locally.
7. [Typescript](https://www.npmjs.com/package/typescript) installed
8. [Postman](https://learning.postman.com/docs/getting-started/installation/installation-and-updates/)
9. [Python 3](https://www.python.org/downloads/)
10. [NPM](https://www.npmjs.com/)
11. [NodeJS](https://www.npmjs.com/)
12. [Terraform](https://towardsaws.com/the-guide-to-terraform-devops-implementing-ci-cd-pipelines-for-eks-workloads-with-github-actions-b6a08cc984b0)
13. Basic Understanding of [Jenkins](https://www.jenkins.io/) and Kubernetes
14. A Domain name Hosted by any domain name provider ( Ex: AWS [Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-in-use.html) )
15. Basic familiarity with [YAML](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started) and [GitHub workflows](https://docs.github.com/en/actions/using-workflows).
16. A [Django project](https://github.com/joelwembo/django-multitenant-saas-ecommerce-kubernetes) hosted in a GitHub repository
17. Basic knowledge of HTML or [React](https://github.com/joelwembo/prodx-reactwebui-react-demo-1)
18. Any Browser for testing

You can follow along with this source code:

[

## GitHub - joelwembo/django-multitenant-saas-ecommerce-kubernetes: Django Multi-tenant …

### Django Multi-tenant, microservices , Kubernetes, Jenkins, Github Actions, and Multiple Databases using docker, bash…

github.com



](https://github.com/joelwembo/django-multitenant-saas-ecommerce-kubernetes?source=post_page-----fee466fe949e--------------------------------)

# Why Jenkins?

Jenkins is a server-based application and requires a web server like Apache Tomcat to run on various platforms like Windows, Linux, macOS, Unix, etc. To use Jenkins, you need to create pipelines which are a series of steps that a Jenkins server will take. Jenkins Continuous Integration Pipeline is a powerful instrument that consists of a set of tools designed to host, monitor, compile, and test code, or code changes, like:

- Continuous Integration Server (Jenkins, Bamboo, CruiseControl, TeamCity, and others)
- Source Control Tool (e.g., CVS, SVN, GIT, Mercurial, Perforce, ClearCase, and others)
- Build tools (Make, ANT, Maven, Ivy, Gradle, and others)
- Automation testing framework (Selenium, Appium, TestComplete, UFT, and others)

![](https://miro.medium.com/v2/0*Jt_OZ6gWw_soZsXA)

# 1. Create AWS Access Keys

> AWS access keys are credentials used to access Amazon Web Services (AWS) programmatically.

**Steps to Create Access Keys**

1. Go to the AWS management console, click on your Profile name, and then click on My Security Credentials. …
2. Go to Access Keys and select Create New Access Key. …
3. Click on Show Access Key and save/download the access key and secret access key.

![](https://miro.medium.com/v2/resize:fit:875/1*1FMrTp0-QXg7pB7xJPdxcw.png)

Create and Sign in your AWS Account

![](https://miro.medium.com/v2/resize:fit:774/1*v8038WhWpN68W7Ss7lw4Kw.png)

Step 1

![](https://miro.medium.com/v2/resize:fit:875/0*AWmpaPF21U99Tfem.png)

Step 2

![](https://miro.medium.com/v2/resize:fit:875/0*d_ypEaJiwX-qnZR2.png)

Step 3

**(Optional for Experts Only**) you can scale this process by using a shell script to create multiple AWS IAM users, grant access, and generate an IAM Access key to the corresponding user as demonstrated in the source code below:

#!/usr/bin/env bash  
#  vim:ts=4:sts=4:sw=4:et  
#  
#  Author: Joel wembo  
#  Date: 2021-02-20 17:26:21 +0000 (Sat, 20 April 2024)  
  
usage_description="  
Creates an AWS service account for CI/CD automation or AWS CLI to avoid having to re-login every day via SSO with 'aws sso login'  
  
Grants this service account Administator privileges in the current AWS account unless an alternative group or policy is specified  
  
Creates an IAM access key (deleting an older unused key if necessary), writes a CSV just as the UI download would, and outputs both shell export commands and configuration in the format for copying to your AWS profile in ~/.aws/credentials  
  
The following optional arguments can be given:  
  
- user name         (default: \$USER-cli)  
- keyfile           (default: ~/.aws/keys/\${user}_\${aws_account_id}_accessKeys.csv) - be careful if specifying this, a non-existent keyfile will create a new key, deleting the older of 2 existing keys if necessary to be able to create this  
- group/policy      (default: Admins group or falls through to AdministratorAccess policy - checks for this group name first, or else policy by this name)  
  
This can also be used as a backup credential - this way if something accidentally happens to your AWS SSO you can still get into your account  
  
Idempotent - safe to re-run, will skip creating a user that already exists or CSV export that already exists  
  
  
$usage_aws_cli_required  
"  
  
# used by usage() in lib/utils.sh  
# shellcheck disable=SC2034  
usage_args="<username> [<group1,group2,policy1,policy2...> <keyfile>]"  
  
help_usage "$@"  
  
#min_args 1 "$@"  
  
user="${1:-$USER-cli}"  
  
#group="${2:-Admins}"  
#policy="${2:-AdministratorAccess}"  
groups_or_policies="${2:-}"  
default_group="Admins"  
default_policy="AdministratorAccess"  
  
aws_account_id="$(aws_account_id)"  
  
access_keys_csv="${3:-$HOME/.aws/keys/${user}_${aws_account_id}_accessKeys.csv}"  
  
export AWS_DEFAULT_OUTPUT=json  
  
aws_create_user_if_not_exists "$user"  
  
exports="$(aws_create_access_key_if_not_exists "$user" "$access_keys_csv")"  
  
group_exists(){  
    # causes a failure in the if policy test condition, probably due to early exit on one of the pipe commands  
    set +o pipefail  
    aws iam list-groups | jq -r '.Groups[].GroupName' | grep -Fixq "$1" || return 1  
    set -o pipefail  
}  
  
policy_exists(){  
    # causes a failure in the if policy test condition, probably due to early exit on one of the pipe commands  
    set +o pipefail  
    aws iam list-policies | jq -r '.Policies[].PolicyName' | grep -Fixq "$1" || return 1  
    set -o pipefail  
}  
  
grant_group_or_policy(){  
    local group_or_policy="$1"  
    if group_exists "$group_or_policy"; then  
        group="$group_or_policy"  
        timestamp "Adding user '$user' to group '$group' on account '$aws_account_id'"  
        aws iam add-user-to-group --user-name "$user" --group-name "$group"  
    elif policy_exists "$group_or_policy"; then  
        policy="$group_or_policy"  
        timestamp "Determining ARN for policy '$policy'"  
        policy_arn="$(aws iam list-policies | jq -r ".Policies[] | select(.PolicyName == \"$policy\") | .Arn")"  
        timestamp "Determined policy ARN:  $policy_arn"  
        timestamp "Granting policy '$policy' permissions directly to user '$user' in account '$aws_account_id'"  
        aws iam attach-user-policy --user-name "$user" --policy-arn "$policy_arn"  
    else  
        die "Group/Policy '$group_or_policy' not found in account '$aws_account_id'"  
    fi  
    echo  
}  
  
if [ -n "$groups_or_policies" ]; then  
    for group_or_policy in ${groups_or_policies//,/ }; do  
        grant_group_or_policy "$group_or_policy"  
    done  
else  
    if group_exists "$default_group"; then  
        grant_group_or_policy "$default_group"  
    elif policy_exists "$default_policy"; then  
        grant_group_or_policy "$policy"  
    else  
        die "Neither default group '$default_group', nor default policy '$default_policy' in account '$aws_account_id'"  
    fi  
fi  
  
echo  
echo "Set the following export commands in your environment to begin using this access key in your CLI immediately:"  
echo  
echo "$exports"  
echo  
echo "or add the following to your ~/.aws/credentials file:"  
echo  
aws_access_keys_exports_to_credentials <<< "$exports"  
echo  
echo

Next, Generates an AWS IAM credentials report

![](https://miro.medium.com/v2/resize:fit:875/1*v1S-19yQSnhKXXqG-RD77w.png)

Generate a Report for your AWS Credentials

![](https://miro.medium.com/v2/resize:fit:875/1*B_tofxJQx1jacv79T4Z16A.png)

![](https://miro.medium.com/v2/resize:fit:875/1*kWN_kktoir_AIuURnEChQQ.png)

View All AWS Accounts created

# 2. Set Up Custom Domain

To configure a custom domain with CloudFront, you need to create a CloudFront SSL certificate in AWS Certificate Manager (ACM) and associate it with your CloudFront distribution. Then, you can configure Route 53 or your DNS provider to point your custom domain to the CloudFront distribution.

To set up a custom domain using Route 53 with your CloudFront distribution, you’ll need to follow these steps:

**Register a Domain**: If you haven’t already, register a domain name through Route 53 or another registrar.

**Create a Hosted Zone in Route 53**: This is where you’ll manage DNS records for your domain.

**Create an Alias Record**: Alias records are used to map your domain to your CloudFront distribution.

![](https://miro.medium.com/v2/resize:fit:875/0*1Z51pT91sXgA-vy1.png)

How to register a domain name in Route 53

![](https://miro.medium.com/v2/resize:fit:875/0*AMcSECACDxX3GqQO.png)

Route 53 Domain pricing and validation

# 3. Create Route53 Hosted Zone

> A Hosted Zone, in the context of Amazon Web Services (AWS) Route 53, is a container for records that define how you want to route traffic for a specific domain, such as example.com or subdomain.example.com. Route 53 is a scalable Domain Name System (DNS) web service designed to provide reliable and cost-effective domain name resolution.

![](https://miro.medium.com/v2/resize:fit:875/0*z0tQBXALtYpbYE-s.png)

Hosted Zone creation

![](https://miro.medium.com/v2/resize:fit:875/0*c6z8wQJsFFLp6las.png)

# 4. Code your Django application

_Django is a free and open-source, Python-based web framework that runs on a web server. It follows the model–template–views architectural pattern. It is maintained by the Django Software Foundation, an independent organization established in the US as a 501 non-profit._

Make sure you have the following prerequisites installed on your Windows machine or Ubuntu server to follow the instructions:

- Python 3.6 or higher ([download](https://www.python.org/downloads/))
- virtualenv
- Docker

> _We will use the built-in Command Prompt (CMD) for this tutorial. You can search for CMD to open it using Windows search._

**Step 1: Create a virtual environment to hold all pip library installations**

If you don’t have `virtualenv` installed, you can install it by running the following command in your CMD **after Python was installed**:

virtualenv venv

**Step 2: Activate the environment:**

For Windows  
source ./venv/Scripts/activate  
source ./venv/Scripts/deactivate  
  
For Ubuntu  
source ./venv/bin/activate  
source ./venv/bin/deactivate ( To Deactivate )

**Step 3: Create a project folder**

mkdir app

**Step 4: Install Django**

pip install django

**Step 5: Create a new Django project inside the project folder**

> A Django app is a self-contained component of a Django project. It is a module that provides specific functionality, such as handling authentication, managing blog posts, or serving an API. An app should represent a single, specific functionality or purpose within the overall website.

django-admin startproject django-multitenant-saas-ecommerce-kubernetes

**Step 6: Create a new test app:**

within the Django project using the following command:

python manage.py startapp app apps/app

*****Adding a new app to the project*****

> _python manage.py startapp home apps/home_

**Step 7: Execute ORM Data Migrations:**

Update your database settings in settings.py

# Database postgres Docker   
# Docker host : host.docker.internal  or database service name   
# docker inspect cloudapp-django-postgresdb | grep "IPAddress"  
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': os.environ.get("POSTGRES_NAME", "DB2"),  
        'USER': os.environ.get("POSTGRES_USER", "postgres"),  
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", "postgres"),  
        'HOST': os.environ.get("POSTGRES_HOST", "localhost"),  
        'PORT': int(os.environ.get("POSTGRES_PORT", "5432")),  
    }  
}

python manage.py makemigrations  
python manage.py migrate

![](https://miro.medium.com/v2/resize:fit:875/1*tkTgFa51MowcYKWzRZEKUg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*UYztzc9WJrZ-uqAvaIzAzA.png)

Django ORM applying migrations

**Step 8: Launch the Django development server**

python manage.py runserver

![](https://miro.medium.com/v2/resize:fit:854/1*EQXcEralh3vmmvSQvjWrMw.png)

Running django server

# 5. Dockerize the Django application

> **Docker** is a popular platform for developing, shipping, and running applications.

**Docker** provides developers and organizations with a flexible, efficient, and scalable platform for building, deploying, and managing applications in **_various environments_**.

Dockerizing a Django application with PostgreSQL involves creating Docker containers for both Django and PostgreSQL and then configuring them to work together. Below are the steps to dockerize a Django application with PostgreSQL:

**Step 1:** Dockerfile for Django Application: Create a `Dockerfile` in the root directory of your Django project. This file will define the configuration for building the Docker image for your Django application. Here's a basic example:

# Use an official Python runtime as a parent image  
FROM python:3.11-slim-bullseye  
# Set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1  
ENV PYTHONUNBUFFERED 1  
# Set the working directory in the container  
WORKDIR /app  
# Copy the requirements file into the container at /app  
COPY requirements.txt /app/  
COPY gunicorn-cfg.py /app/  
# COPY deployments ./app/deployments/  
RUN pip install --upgrade pip  
RUN pip install --upgrade setuptools  
# Install any needed packages specified in requirements.txt  
# RUN pip install --no-cache-dir -r requirements.txt  
RUN pip install -r requirements.txt  
# RUN pip install django-filter  
# Copy the current directory contents into the container at /app  
COPY . /app/  
EXPOSE 8585

**Step 2:** docker-compose.yml:

> Docker Compose is a tool for defining and running multi-container Docker applications. It allows you to use a YAML file to configure your application’s services, networks, and volumes, and then to run and manage your entire application stack with a single command.

Create a `docker-compose.yml` file in the root directory of your project. This file defines the services, networks, and volumes for your Docker containers.

version: "3.9"  
services:  
  web:  
    image: joelwembo/cloudapp-django-web:latest  
    container_name: cloudapp-django-web  
    env_file: .env  
    restart: always  
    build:  
      context: .  
      dockerfile: Dockerfile  
    environment:  
      - DJANGO_SETTINGS_MODULE=multitenantsaas.settings  
      - DJANGO_LOG_LEVEL=DEBUG  
      - ENV=local  
      - POSTGRES_NAME=DB2  
      - POSTGRES_USER=postgres  
      - POSTGRES_PASS=postgres  
      - POSTGRES_HOST=cloudapp-django-postgresdb  
      - POSTGRES_PORT=5432    
    command:  
      - /bin/sh  
      - -c  
      - |  
        python manage.py makemigrations  
        python manage.py migrate  
        python manage.py runserver 0.0.0.0:8585       
    ports:  
      - "8585:8585"  
    networks:  
      - web_network  
    volumes:  
       - appdata:/app  
    depends_on:  
      - cloudapp-django-postgresdb  
      - redis   
    deploy:  
      resources:  
        limits:  
          cpus: '0.001'  
          memory: 50M  
        reservations:  
          cpus: '0.0001'  
          memory: 20M   
  celery:  
    container_name: cloudapp-django-celery  
    build: .  
    command:   
       - /bin/sh  
       - -c  
       - |  
        user=django  
        group=developers  
        environment=C_FORCE_ROOT="yes"  
        environment=HOME="/root",USER="django"  
        celery -A multitenantsaas worker -l info  
          
    volumes:  
      - .:/django_app  
    environment:  
      - DEBUG=0  
      - DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 172.104.60.217  [::1]  
      - CELERY_BROKER_URL="redis://redis:6379/0"  
      - CELERY_RESULT_BACKEND="redis://redis:6379/0"  
      - broker_connection_retry_on_startup="True"  
      - CELERY_TASK_ALWAYS_EAGER=True  
      - C_FORCE_ROOT=true  
      - BROKER_TRANSPORT="kombu.transport.django"  
    depends_on:  
      - redis  
  redis:  
      image: "redis:alpine"  
      container_name: cloudapp-django-redis  
      ports:  
        - '6379:6379'  
      expose:  
        - "6379"    
      volumes:  
          - redisDB:/data  
      # networks:  
      #     - db_network  #  
  cloudapp-django-postgresdb:  
    restart: always  
    image: postgres:latest  
    container_name: cloudapp-django-postgresdb  
    volumes:  
      - pgdata:/var/lib/postgresql/data  
    environment:  
      - POSTGRES_DB=DB2  
      - POSTGRES_USER=postgres  
      - POSTGRES_PASSWORD=postgres  
      - POSTGRES_PORT=5432  
      - "POSTGRES_HOST_AUTH_METHOD=trust"  
    expose:  
       - "5432"  
    ports:  
       - "5432:5432"  
    # networks:  
    #    - data_network     
  pgadmin:  
        restart: always  
        image: dpage/pgadmin4  
        container_name: cloudapp-fintech-pgadmin   
        # depends_on:  
        #   - cloudapp-django-postgresdb  
        ports:  
          - "5051:80"  
        environment:  
          PGADMIN_DEFAULT_EMAIL: 19718580.dev1@protonmail.com  
          PGADMIN_DEFAULT_PASSWORD: postgres     
          PGADMIN_CONFIG_ENHANCED_COOKIE_PROTECTION: 'False'  
          PGADMIN_CONFIG_WTF_CSRF_CHECK_DEFAULT: 'False'  
  
networks:  
  web_network:  
    driver: bridge  
volumes:  
  pgdata:  
  # redisDB:  
  appdata:  
   driver: local  

**Step 3:** define the .env to save the development environment variables

SERVER=https://cloudapp.io  
DEBUG=True  
SECRET_KEY=  
DJANGO_SECRET_KEY=%jjnu7=  
DJANGO_SUPERUSER_PASSWORD=  
DJANGO_SUPERUSER_EMAIL=  
DJANGO_SUPERUSER_USERNAME=joelwembo  
ALLOWED_PORTS=localhost  
POSTGRES_NAME=DB2  
POSTGRES_USER=postgres  
POSTGRES_PASSWORD=postgres  
POSTGRES_PORT=5432  
# POSTGRES_HOST=host.docker.internal  
# POSTGRES_HOST=localhost  
POSTGRES_HOST=cloudapp-django-postgresdb

Let's first Launch the development server locally by using the Make file

> [Makefiles](https://makefiletutorial.com/) are used to help decide which parts of a large program need to be recompiled. In the vast majority of cases, C or C++ files are compiled.

ifndef VERBOSE  
MAKEFLAGS += --no-print-directory  
endif  
SHELL := /bin/bash  
.DEFAULT_GOAL := help  
  
DOCKER_USERNAME ?= joelwembo  
APPLICATION_NAME ?= cloudapp-django-web  
GIT_HASH ?= $(shell git log --format="%h" -n 1)  
  
help:  
 @ echo "Use one of the following targets:"  
 @ tail -n +8 Makefile |\  
 egrep "^[a-z]+[\ :]" |\  
 tr -d : |\  
 tr " " "/" |\  
 sed "s/^/ - /g"  
 @ echo "Read the Makefile for further details"  
  
venv virtualenv:  
 @ echo "Creating a new virtualenv..."  
 @ rm -rf venv || true  
 @ python3.11 -m venv venv  
 @ echo "Done, now you need to activate it. Run:"  
 @ echo "source venv/bin/activate"  
activate:  
 @ echo "Activating this python3.11 Virtual venv Env:"  
 @ bash --rcfile "./venv/bin/activate"  
  
requirements pip:  
 @ if [ -z "${VIRTUAL_ENV}" ]; then \  
  echo "Not inside a virtualenv."; \  
  exit 1; \  
 fi  
 @ echo "Upgrading pip..."  
 @ python3.11 -m pip install --upgrade pip  
 @ echo "Updating pip packages:"  
 @ pip install -r "requirements.txt"  
 @ echo "Self installing this package in edit mode:"  
 # @ pip install -e .  
 @ echo "All pip libraries installed You are ready to go ;-)"  
  
requirementsdev:  
 @ if [ -z "${VIRTUAL_ENV}" ]; then \  
  echo "Not inside a virtualenv."; \  
  exit 1; \  
 fi  
 @ echo "Upgrading pip..."  
 # @ python3.11 -m pip install --upgrade pip  
 @ echo "Updating pip packages:"  
 @ pip install -r "requirements_dev.txt"  
  
cleanfull:  
 @ echo "Cleaning old files..."  
 @ rm -rf **/.pytest_cache  
 @ rm -rf .tox  
 @ rm -rf dist  
 @ rm -rf build  
 @ rm -rf **/__pycache__  
 @ rm -rf *.egg-info  
 @ rm -rf .coverage*  
 @ rm -rf **/*.pyc  
 @ rm -rf env  
 @ rm -rf venv  
 @ rm -rf local  
 @ rm -rf .aws-sam  
 @ echo "All done!"  
clean:  
 @ echo "Cleaning old files..."  
 @ rm -rf **/.pytest_cache  
 @ rm -rf .tox  
 @ rm -rf dist  
 @ rm -rf build  
 @ rm -rf **/__pycache__  
 @ rm -rf *.egg-info  
 @ rm -rf .coverage*  
 @ rm -rf **/*.pyc  
 @ echo "All done!"  
start-engine:  
 @ python3.11 manage.py makemigrations  
 @ python3.11 manage.py migrate  
 @ python3.11 manage.py runserver 0.0.0.0:8585  
  
build:  
 @ docker build --tag ${DOCKER_USERNAME}/${APPLICATION_NAME} .  
push:  
 @ docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}  
docker-run:  
 @ docker-compose down   
 @ docker-compose build --no-cache  
 @ docker-compose up  
release:  
 @ docker pull ${DOCKER_USERNAME}/${APPLICATION_NAME}:${GIT_HASH}  
 @ docker tag  ${DOCKER_USERNAME}/${APPLICATION_NAME}:${GIT_HASH} ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest  
 @ docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest

![](https://miro.medium.com/v2/resize:fit:875/0*Ym4ZJrWCEXeZzSZW.png)

Docker Compose

![](https://miro.medium.com/v2/resize:fit:875/0*AYPpOeBxj9Q-gozR.png)

Manage your Django docker container using the following command format to interact with the images :

# makemigrations using docker exec  
docker exec -it cloudapp-django-web python manage.py makemigrations  
  
docker exec -it cloudapp-django-web python manage.py migrate  
  
# create super user or admin  
  
docker exec -it cloudapp-django-web python manage.py createsuperuser

![](https://miro.medium.com/v2/resize:fit:658/1*e5rf89Ai0L7vwr_16Y_4Cg.png)

django docker exec

To view the Django app, open your browser and type this address 127.0.0.1:8585

![](https://miro.medium.com/v2/resize:fit:875/0*Bey48cZWNSL7y9Nn.png)

Django Rest Framework Viewset

![](https://miro.medium.com/v2/resize:fit:875/0*p4NP7g2w2HvYocTU.png)

![](https://miro.medium.com/v2/resize:fit:875/0*jvQXYQ4x_aASyrYJ.png)

![](https://miro.medium.com/v2/resize:fit:875/0*Rb-Xlt-r1iK2roPX.png)

**Pgadmin4** credentials in docker-compose.yaml

You can access your pgadmin4 page using [http://localhost:5051/browser](https://localhost:5051/browser), we have docker-compose to provision both postgres and pgadmin4 as follow as side with another option of using AWS RDS for postgres as follows:

cloudapp-django-postgresdb:  
    restart: always  
    image: postgres:latest  
    container_name: cloudapp-django-postgresdb  
    volumes:  
      - pgdata:/var/lib/postgresql/data  
    environment:  
      - POSTGRES_DB=DB2  
      - POSTGRES_USER=postgres  
      - POSTGRES_PASSWORD=postgres  
      - POSTGRES_PORT=5432  
      - "POSTGRES_HOST_AUTH_METHOD=trust"  
    expose:  
       - "5432"  
    ports:  
       - "5432:5432"  
    # networks:  
    #    - data_network     
  pgadmin:  
        restart: always  
        image: dpage/pgadmin4  
        container_name: cloudapp-fintech-pgadmin   
        depends_on:  
          - cloudapp-django-postgresdb  
        ports:  
          - "5051:80"  
        environment:  
          PGADMIN_DEFAULT_EMAIL: 19718580.dev1@protonmail.com  
          PGADMIN_DEFAULT_PASSWORD: postgres     
          PGADMIN_CONFIG_ENHANCED_COOKIE_PROTECTION: 'False'  
          PGADMIN_CONFIG_WTF_CSRF_CHECK_DEFAULT: 'False'

![](https://miro.medium.com/v2/resize:fit:875/0*89gpsUN-VJGVuUmV.png)

pgadmin4 using docker-compose

> You will need a DockerHub or any docker registry Account and Access Token to push and pull your images

**Docker Hub** is a cloud-based service from Docker that allows developers to share containerized applications and automate workflows. It serves as a centralized resource for **container image discovery**, distribution, and collaboration.

To create a new access token for Docker Hub, follow these steps:

1. **Log in to Docker Hub**: Visit the Docker Hub website (https://hub.docker.com/) and log in to your Docker Hub account if you’re not already logged in.

![](https://miro.medium.com/v2/resize:fit:875/1*I1ipZEBSitmAdrmsEmC7Tw.png)

**2. Access Token Settings:** Once logged in, click on your profile icon at the top right corner of the page, then select “Account Settings” from the dropdown menu.

**3. Navigate to Security Settings:** In the Account Settings page, navigate to the “Security” tab.

![](https://miro.medium.com/v2/resize:fit:875/1*qXDdC_Bp4AtTf7wdxUCJHA.png)

**4. Generate Access Token:** Scroll down to the “Access Tokens” section and click on the “New Access Token” button.

![](https://miro.medium.com/v2/resize:fit:875/1*xFmIuFThhh36LOCFXeSDeg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*jKuQEzuRSdKyhdiACvSpYw.png)

![dockerhub Access Token to manage container images by joel wembo](https://miro.medium.com/v2/resize:fit:875/1*IWJZ-4xTEZpTwH1kIQZrwQ.png)

dockerhub Access Token to manage container images

# 6. AWS EC2 Provisioning Using Terraform and GitHub Actions

In this step, we are going to automate the provisioning of the Ubuntu aws ec2 server using Terraform and GitHub actions.

![](https://miro.medium.com/v2/resize:fit:875/1*y9BY6aXtqC2Noh3FuUtfIQ.png)

> _GitHub Actions is a feature provided by GitHub that allows you to automate various tasks within your software development workflows directly from your GitHub repository. It enables you to build, test, and deploy your code directly within GitHub’s ecosystem._

For more details regarding terraform provisioning of AWS resources, you can read this material [_The Guide to Terraform DevOps: Implementing CI/CD Pipelines for EKS workloads with GitHub Actions for Multi-Environments Approach_](https://towardsaws.com/the-guide-to-terraform-devops-implementing-ci-cd-pipelines-for-eks-workloads-with-github-actions-b6a08cc984b0)

Now, let’s set up our AWS environment. We will be using Terraform to create our infrastructure. We will be creating the following main resources:

- Amazon EC2
- Amazon S3
- IAM roles and policies

Let’s first create files that we plan to use in our `terraform/` directory.

![](https://miro.medium.com/v2/resize:fit:875/0*jMPi38D7UOIDnune.png)

Project Folder Structure

First, let set up our GitHub Actions and Environment settings

1. On GitHub.com, navigate to the main page of the repository.
2. Under your repository name, click Settings. …
3. In the “Security” section of the sidebar, select Secrets and Variables, then click Actions.
4. Click the Secrets tab.
5. Click New Repository secret.

![](https://miro.medium.com/v2/resize:fit:875/0*MlyFXCGYiqyjEurX.png)

![](https://miro.medium.com/v2/resize:fit:875/0*01fARBTYjG0xqXLv.png)

![](https://miro.medium.com/v2/resize:fit:875/0*jWMSYFxdJbRKtwnw.png)

![](https://miro.medium.com/v2/resize:fit:875/0*BzNLuELlWg_ikaPt.png)

Terraform TF API Token

![](https://miro.medium.com/v2/resize:fit:875/0*-qhWllp9FbvHEGHf.png)

Setup Repository secrets in Github for GitHub Actions

In the .**github**/**workflows** directory, create a **file** with the .**yml** or .**yaml** extension. This tutorial will use terraform-aws-ec2–4.yaml as the **file** name.

name: "Terraform Pipeline Provision EC2"  
  
on:  
 push:  
   branches: ['master' , 'main']  
 pull_request:  
   branches: ['master', 'main']  
  
permissions:  
    contents: write     
  
env:  
 # verbosity setting for Terraform logs  
  TF_LOG: INFO  
  # Credentials for deployment to AWS  
  AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}  
  AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}  
  TF_CLOUD_ORGANIZATION: "prodxcloud"  
  TF_WORKSPACE: "prodxcloud"  
  TF_API_TOKEN: ${{ secrets.TF_API_TOKEN}}  
  CONFIG_DIRECTORY: "./deployments/terraform/terraform-aws-ec2-tf/terraform/"  
  
   
jobs:  
 terraform:  
   name: "Terraform Pipeline Provision EC2 with TF Cloud"  
   runs-on: ubuntu-latest  
   defaults:  
     run:  
       shell: bash  
       # We keep Terraform files in the terraform directory.  
       working-directory: ./deployments/terraform/terraform-aws-ec2-tf/terraform  
   
   steps:  
     - name: Checkout the repository to the runner  
       uses: actions/checkout@v2  
   
     - name: Setup Terraform with specified version on the runner  
       uses: hashicorp/setup-terraform@v2  
       with:  
         terraform_version: 1.3.0  
      
     - name: Terraform init   
       id: init  
       run: terraform init -lock=false  
      #  env:  
      #     TF_CLI_ARGS_init: '-backend-config="token=${{ secrets.TF_API_TOKEN }}"'  
   
     - name: Terraform format  
       id: fmt  
       run: terraform fmt  
      
     - name: Terraform validate  
       id: validate  
       run: terraform validate  
       env:  
          GITHUB_TOKEN: ${{ secrets.G_TOKEN}}  
          TFE_TOKEN: ${{ secrets.TF_API_TOKEN }}  
   
     - name: Terraform Apply  
       run: terraform apply -auto-approve -input=false -lock=false     

6. Create S3 Buckets to manage our terraform states

Next, let's manually create s3s bucket folders for our state management during terraform workflows and GitHub.

![](https://miro.medium.com/v2/resize:fit:875/0*Sdr0nKutHoSeTfA7.png)

S3 Bucket for terraform state

![](https://miro.medium.com/v2/resize:fit:875/0*M8WBndYFjZTrZZY3.png)

State Keeping with S3

We can also provision the s3 bucket using the aws command line or CloudFormation:

aws s3api create-bucket --bucket django-app-8 --region ap-southeast-1  
aws s3api create-bucket --bucket django-terraform-rds-1 --region ap-southeast-1

# 7. Create a Key Pairs

Next, create a **key pair** using Amazon **EC2** · In the navigation pane, under Network & Security, choose **Key Pairs**. · Choose Create **key pair**. · For Name, enter a descriptive

![](https://miro.medium.com/v2/resize:fit:875/0*xIN0picYEp54i_UX.png)

![](https://miro.medium.com/v2/resize:fit:875/0*wIpsYQL5H8qOIcGd.png)

![](https://miro.medium.com/v2/resize:fit:875/0*cznPe6xLkALi1jVi.png)

Key pair list

Key pairs are necessary for accessing your EC2 instances using terminal/shell, especially Linux-based instances. You can also create your key pairs using the aws cli command

To create a key-pair using AWS CLI, type aws ec2 create-key-pair — key-name <your_key_name>, where <your_key_name> is your key’s name by which it would be saved in the AWS. The output for the same is shown below, which is in the JSON format.

aws ec2 create-key-pair --key-name prodxcloud_test_key.pem < any-name >

![](https://miro.medium.com/v2/resize:fit:875/0*dVWtjaYdeo1LmAun.png)

![](https://miro.medium.com/v2/resize:fit:306/0*Tns8p8bVYyV0wpMp.png)

# 8. backend.tf

> In Terraform, the backend is the component responsible for storing and retrieving Terraform state files, which contain information about your infrastructure and the resources managed by Terraform.

**Remote state** is simply storing that **state** file remotely, rather than on your local filesystem. With a single **state** file stored remotely

# 8.1 S3 bucket for terraform state management

Just verify first that the bucket where you are going to save the terraform state was already created.

terraform {  
  backend "s3" {  
    bucket         = "django-app-9"  
    region         = "ap-southeast-1"  
    key            = "state/terraform.tfstate"  
    dynamodb_table = "data_onents_tf_lockid"  
    encrypt        = true  
  }  
}  
  

_The code above ensures that the state of our terraform resources is kept in the s3 folder._

![](https://miro.medium.com/v2/resize:fit:875/1*6EzaD3ZQWgqSXbZeQDaAEg.png)

Terraform State management Using AWS S3 Bucket

![](https://miro.medium.com/v2/resize:fit:875/1*XxiLCUEWlzMw1IzFNuFcPQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*cJZXsLAix_LcttYEKWlcUQ.png)

Or, you have another option to keep your state and run at the same place using **Terraform Cloud**.

## Replace remote backend with Terraform Cloud

Using AWS services as a remote backend requires managing disparate services to handle your Terraform state. You need an S3 bucket for state storage and a DynamoDB instance for state locking. You must manage the security and lifecycle of these resources for each of your Terraform projects. Instead, you can use Terraform Cloud for state storage, locking, and remote execution for all of your Terraform projects.

When interacting with Terraform-specific network services, Terraform expects to find API tokens in CLI configuration files in `credentials` blocks:

In your terraform solution directory create a file .terraformrc and update the token with your TF_API_TOKEN that we created earlier.

credentials "app.terraform.io" {  
  token = "{{TF_API_TOKEN}}"  
}

# backend.tf To migrate your state from S3 to Terraform Cloud, you need to replace the backend configuration.  
terraform {  
  backend "remote" {    
    hostname="app.terraform.io"    
    organization = "prodxcloud"   
    workspaces {  
      prefix = "prodxcloud"   
    }  
  }  
}

Still working on your `learn-terraform-migrate-s3-tfc` directory, replace the `backend “s3"` block in `main.tf` with the following `cloud` block, replacing `<YOUR-ORG-NAME>` with your Terraform Cloud organization’s name.

# 8.2 Terraform Cloud Configuration

HashiCorp provides GitHub Actions that integrate with the Terraform Cloud API. These actions let you create your own custom CI/CD workflows to meet the needs of your organization.

![](https://miro.medium.com/v2/resize:fit:875/0*53Seh2aYRf0aZ89R)

**Step 1: Create your project and workplace in terraform cloud**

![](https://miro.medium.com/v2/resize:fit:875/0*cjVRkeFqM2fwU1SJ.png)

Create a project in Terraform Cloud

![](https://miro.medium.com/v2/resize:fit:875/0*5-gAF49eOV4oeVac.png)

**Step 2: Define Variables set to allow** [**terraform cloud**](https://app.terraform.io/app/getting-started) **for state management**

![](https://miro.medium.com/v2/resize:fit:875/0*VeokYH4xDJ1jOOIO.png)

**Step 3: Change the default execution Mode to remote**

![](https://miro.medium.com/v2/resize:fit:875/0*pBvxMWLfedeh0E6U.png)

**Step 4: Create API tokens for Github actions to interact with Terraform Cloud**

![](https://miro.medium.com/v2/resize:fit:875/0*8MTMW-7cV8WmNMLy.png)

Terraform cloud API tokens

![](https://miro.medium.com/v2/resize:fit:875/0*cnTqLCa_LlTQI4ME.png)

API Token for your project

![](https://miro.medium.com/v2/resize:fit:875/0*DgRVa-7Gtg-vep4I.png)

Generated Token

![](https://miro.medium.com/v2/resize:fit:875/0*hlVW2MDaihoB8e6f.png)

Organization token ( Optional )

**Step 5 : Add TF_API_TOKEN in your Github Actions environment**

![](https://miro.medium.com/v2/resize:fit:875/0*BzNLuELlWg_ikaPt.png)

Terraform TF_API_TOKEN

# 9. provider.tf

> A Terraform provider is a plugin responsible for understanding API interactions with a particular infrastructure service. Providers can manage resources, execute operations, and handle authentication and communication with the underlying infrastructure.

==provider== =="aws"== =={  
  region === =="us-east-1"==  ======# alias      === =="use_default_region"==  ======# profile====="default"====  
}==

# 10. variable.tf

_Terraform supports a few different variable formats. Depending on the usage, the variables are generally divided into inputs and outputs._

_The input variables are used to define values that configure your infrastructure. These values can be used again and again without having to remember their every occurrence in the event it needs to be updated._

_Output variables, in contrast, are used to get information about the infrastructure after deployment. These can be useful for passing on information such as IP addresses for connecting to the server._

variable "aws_region" {  
  type    = string  
  default = "us-east-1"  
}  
  
variable "backend_organization" {  
  type    = string  
  default = "prodxcloud"  
}  
  
variable "backend_worspaces" {  
  type    = string  
  default = "prodxcloud"  
}  
  
variable "access_key" {  
  default = ""  
}  
variable "secret_key" {  
  default = ""  
}  
  
variable "bucket" {  
  default = "bucket"  
}  
  
  
variable "cidr_block" {  
  default = "10.0.0.0/16"  
}  
variable "subnet" {  
  default = "10.0.0.0/24"  
}  
variable "instance_type" {  
  type    = string  
  default = "t2.micro"  
}  
  
variable "instance_ami" {  
  description = "AMI ID for the EC2 instance"  
  type        = string  
  default     = ""  
}  
  
variable "instance_vpc_id" {  
  type    = string  
  default = ""  
}  
  
variable "instance_subnet_id" {  
  type    = string  
  default = ""  
}  
  
variable "instance_keyName" {  
  type    = string  
  default = "prodxsecure"  
}  
  
variable "instance_secgroupname" {  
  description = "This is a security Group Name"  
  type        = string  
  default     = "prodxcloud-aws-ec2-lab-1"  
}  
  
variable "instance_publicip" {  
  type    = bool  
  default = true  
}  
  
variable "aws_availability_zone" {  
  type    = string  
  default = "us-east-1b"  
}  
  
  
variable "ingress_rules" {  
  default = {  
    "my ingress rule" = {  
      "description" = "For HTTP"  
      "from_port"   = "80"  
      "to_port"     = "80"  
      "protocol"    = "tcp"  
      "cidr_blocks" = ["0.0.0.0/0"]  
    },  
    "my other ingress rule" = {  
      "description" = "For SSH"  
      "from_port"   = "22"  
      "to_port"     = "22"  
      "protocol"    = "tcp"  
      "cidr_blocks" = ["0.0.0.0/0"]  
    },  
  
    "Postgres port" = {  
      "description" = "For HTTP postgres"  
      "from_port"   = "5432"  
      "to_port"     = "5432"  
      "protocol"    = "tcp"  
      "cidr_blocks" = ["0.0.0.0/0"]  
    },  
  
    "Jenkins port" = {  
      "description" = "For Jenkins"  
      "from_port"   = "8080"  
      "to_port"     = "8080"  
      "protocol"    = "tcp"  
      "cidr_blocks" = ["0.0.0.0/0"]  
    },  
  
     "React Application port" = {  
      "description" = "For React"  
      "from_port"   = "3000"  
      "to_port"     = "3000"  
      "protocol"    = "tcp"  
      "cidr_blocks" = ["0.0.0.0/0"]  
    },  
  
    "Django Application port" = {  
      "description" = "For Django"  
      "from_port"   = "8585"  
      "to_port"     = "8585"  
      "protocol"    = "tcp"  
      "cidr_blocks" = ["0.0.0.0/0"]  
    },  
     "Django alt Application port" = {  
      "description" = "For Django alt port"  
      "from_port"   = "8000"  
      "to_port"     = "8000"  
      "protocol"    = "tcp"  
      "cidr_blocks" = ["0.0.0.0/0"]  
    }  
  
    "All Ports" = {  
      "description" = "For HTTP all ports"  
      "from_port"   = "3000"  
      "to_port"     = "65535"  
      "protocol"    = "tcp"  
      "cidr_blocks" = ["0.0.0.0/0"]  
    }  
  }  
  type = map(object({  
    description = string  
    from_port   = number  
    to_port     = number  
    protocol    = string  
    cidr_blocks = list(string)  
  }))  
  description = "Security group rules"  
}

# 11. main.tf

_Amazon Elastic Compute Cloud is a part of Amazon.com’s cloud-computing platform, Amazon Web Services, that allows users to rent virtual computers on which to run their own computer applications._

How to obtain your Amazon machine image (AMI)?

> **An Amazon Machine Image** (**AMI**) is **a** supported and maintained image provided by AWS that provides the information required to launch **an** instance.

![](https://miro.medium.com/v2/resize:fit:875/1*uDIuh1ItvL5zM4e5rpeyVg.png)

![How to obtain your Amazon machine image (AMI ) by Joel Wembo](https://miro.medium.com/v2/resize:fit:875/1*ueqj2hLlP_6CcApgzevVmw.png)

How to obtain your Amazon machine image

# Terraform provision AWS EC2 instance with Terraform Cloud Management  
  
variable "awsprops" {  
  type = map(any)  
  default = {  
    region       = "us-east-1"  
    vpc          = "vpc-06e427b3d907fb984"  
    ami          = "ami-0cd59ecaf368e5ccf"  
    itype        = "t2.micro"  
    subnet       = "subnet-063a85d9139280d8a"  
    publicip     = true  
    keyname      = "prodxsecure"  
    secgroupname = "prodxcloud-aws-ec2-lab-1"  
  }  
}  
  
  
// AMI Security group setting using HashiCorp Configuration Language (HCL)  
resource "aws_security_group" "prod-sec-sg" {  
  name        = var.instance_secgroupname  
  description = var.instance_secgroupname  
  vpc_id      = var.instance_vpc_id  
  
  // To Allow SSH Transport  
  
  dynamic "ingress" {  
    for_each = var.ingress_rules  
    content {  
      description = lookup(ingress.value, "description", null)  
      from_port   = lookup(ingress.value, "from_port", null)  
      to_port     = lookup(ingress.value, "to_port", null)  
      protocol    = lookup(ingress.value, "protocol", null)  
      cidr_blocks = lookup(ingress.value, "cidr_blocks", null)  
    }  
  }  
  
  egress {  
    from_port   = 0  
    to_port     = 0  
    protocol    = "-1"  
    cidr_blocks = ["0.0.0.0/0"]  
  }  
  
  
  tags = {  
    Name = "allow_tls"  
  }  
  
  lifecycle {  
    create_before_destroy = false  
  }  
}  
  
  
# instance identity  
resource "aws_instance" "project-iac-2" {  
  ami                         = lookup(var.awsprops, "ami")  
  instance_type               = lookup(var.awsprops, "itype")  
  subnet_id                   = lookup(var.awsprops, "subnet")  
  associate_public_ip_address = lookup(var.awsprops, "publicip")  
  key_name                    = lookup(var.awsprops, "keyname")  
  
  
  # security group  
  vpc_security_group_ids = [  
    aws_security_group.prod-sec-sg.id  
  ]  
  root_block_device {  
    delete_on_termination = true  
    volume_size           = 40  
    volume_type           = "gp2"  
  }  
  tags = {  
    Name        = "prodxcloud-aws-ec2-lab-1"  
    Environment = "DEV"  
    OS          = "UBUNTU"  
    Managed     = "PRODXCLOUD"  
  }  
  
  provisioner "file" {  
    source      = "installer.sh"  
    destination = "/tmp/installer.sh"  
  
  }  
  
  provisioner "remote-exec" {  
    inline = [  
      "sudo chmod +x /tmp/installer.sh",  
      "sh /tmp/installer.sh"  
    ]  
  
  }  
  depends_on = [aws_security_group.prod-sec-sg]  
  
# connecting to AWS instance to install jenkins and docker  
  connection {  
    type        = "ssh"  
    host        = self.public_ip  
    user        = "ubuntu"  
    private_key = file("./prodxsecure.pem")  
  }  
}  
  
  
output "ec2instance" {  
  value = aws_instance.project-iac-2.public_ip  
}  
  

To create your VPC and get the subnet ID, the following screenshot and the instructions below:

**Open the Amazon VPC console at** [**http://console.aws.amazon.com/vpc/**](https://console.aws.amazon.com/vpc/) **.**

1. On the VPC dashboard, choose Create VPC.
2. For Resources to create, choose VPC and more.
3. Keep Name tag auto-generation selected to create Name tags for the VPC resources or clear it to provide your own Name tags for the VPC resources.

![](https://miro.medium.com/v2/resize:fit:875/1*c0c5lGKNeWxwlMUDdyNNPQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*UE7K2FvHJtvUihCypeEfZA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*YxeTOHBjxgpu2g2_vwQeAQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*_4KS-P-keoX9xBeZF4IcTA.png)

Add the installer.sh file to install Jenkins and docker in your ec2 instance

#!/bin/bash  
  
Java Installations  
sudo apt-get install openjdk-11-jdk -y  
sudo apt-get install zip -y  
echo 'JDK Installed successfully installer'  
  
  
# Jenkins installations  
sudo apt update  
apt install make  
sudo apt-get install debian-keyring debian-archive-keyring --assume-yes  
sudo apt-key update  
sudo apt-get update  
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 40976EAF437D05B5  
sudo apt update  
sudo apt install openjdk-11-jre-headless --assume-yes  
sudo java -version  
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null  
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null  
sudo apt-get update  
sudo apt-get install jenkins --assume-yes  
# sudo service jenkins status  
echo 'Jenkins successfully installer : password '  
  
  
# Docker installation  
sudo apt install apt-transport-https ca-certificates curl software-properties-common --assume-yes  
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  
sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable'  
apt-cache policy docker-ce  
sudo apt install docker-ce --assume-yes  
sudo chmod 777 /var/run/docker.sock  
  
# sudo systemctl status docker  
echo 'Docker successfully installer'  
  
# install docker compose  
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose   
sudo chmod +x /usr/local/bin/docker-compose  
docker-compose --version  
echo "Docker Compose Installed successfully installer"  
  
# nginx installation for testing purpose  
docker run --name mynginx1 -p 80:80 -d nginx  
echo "nginx server running in your domain.com at port 80"  
  
# eks cli installer  
  
# argocd cli installer  
  
# sonarQube installer

![](https://miro.medium.com/v2/resize:fit:1250/1*GovxX-1okaf8zczW52STKw.png)

Current Directory

# 12. Validate and Test your first solution

Push all your current changes to your github repo

![](https://miro.medium.com/v2/resize:fit:875/1*giPTgaoU3-C3qtNmVb3CLA.png)

![](https://miro.medium.com/v2/resize:fit:1250/1*Q9-DEBw6JsuofwAR0GsLfw.png)

![](https://miro.medium.com/v2/resize:fit:1250/1*gyvzrAxZ28kEaAAgnRUE-g.png)

GitHub Actions Progress

![](https://miro.medium.com/v2/resize:fit:875/1*gWp27l47SPJokm8HPu6SDA.png)

GitHub Actions Update

![](https://miro.medium.com/v2/resize:fit:875/1*-P4F0kXMcjgYuO3Z1aCMWQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*DPkF-CBNOss5g_-H_ZKluQ.png)

Security group rules added

![](https://miro.medium.com/v2/resize:fit:875/1*TjM-kC8KbMZ-Ng54D60SSw.png)

![](https://miro.medium.com/v2/resize:fit:875/1*OBq1U69HmQRAFABvfhGE_g.png)

# 13. Complete your Jenkins installations

**13.1 Finalize your Jenkins installation**

![](https://miro.medium.com/v2/resize:fit:875/1*ZJW61gIBj17C7nSfyM9pvQ.png)

Accessing your AWS EC2 instance

![](https://miro.medium.com/v2/resize:fit:875/1*UCaV9H9VibEMeyrut94YCw.png)

![](https://miro.medium.com/v2/resize:fit:836/1*FK9sKikeYH3-HPc2XmW4ww.png)

![](https://miro.medium.com/v2/resize:fit:875/1*4eGhA7raqmEH2HsJ-O15tg.png)

Checking Jenkins service in aws ec2

![](https://miro.medium.com/v2/resize:fit:875/1*Bn8Te8ovApzt9--toJhGcQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*fnL5Q4hRJD2L5P2GnDDrkA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*bbMV38JNBe_GOTfRxu4y4A.png)

![](https://miro.medium.com/v2/resize:fit:875/1*OXuK4dd3rvwICVJa3b5Xfg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*pOFNDo3inHrJd205AQAjUw.png)

![](https://miro.medium.com/v2/resize:fit:875/1*nxwjhe9VfCHvWuh1nnlh9Q.png)

![](https://miro.medium.com/v2/resize:fit:875/1*1yxWdZ44LcoUpb0M9mKa_g.png)

![](https://miro.medium.com/v2/resize:fit:875/1*JPkfeS7KLYoENanOfj6trA.png)

Login to Jenkins

**13.2 Install Jenkins plugins**

Installing plugins in Jenkins is a straightforward process through the Jenkins web interface. Here’s how you can do it:

1. **Access Jenkins Dashboard**:

- Open your web browser and navigate to the Jenkins dashboard by entering the URL of your Jenkins server (e.g., [http://your-jenkins-server:8080).](http://your-jenkins-server:8080).)

**2. Navigate to Plugin Manager**:

- Once you’re logged into Jenkins, click on “Manage Jenkins” from the left-hand sidebar.

**3. Access Plugin Manager:**

- In the “Manage Jenkins” page, you’ll see various options. Click on “Manage Plugins.”

**4. Available Plugins Tab:**

- In the “Manage Plugins” section, you’ll see different tabs. Click on the “Available” tab.

**5. Search for Plugins:**

- You can search for plugins by typing keywords into the search box. Alternatively, you can browse through the list of available plugins.

**6. Select Plugins for Installation:**

- Check the checkbox next to the plugin(s) you want to install.

**7. Installation Process:**

- Once you’ve selected the plugins you want, scroll down to the bottom of the page and click the “Install without restart” button

> Wait for Installation to Complete:

- Jenkins will start downloading and installing the selected plugins.

**8. Confirmation:**

- Once the installation is complete, you’ll see a confirmation message indicating that the plugins were successfully installed.

**9 . Restart Jenkins (if necessary):**

- If you choose the “Download now and install after restart” option, you’ll need to manually restart Jenkins for the changes to take effect.

**10. Verify Installation:**

- After Jenkins restarts (if necessary), you can verify that the plugins were installed successfully by checking the “Installed” tab in the “Manage Plugins” section.

![](https://miro.medium.com/v2/resize:fit:875/1*QxKdnh30NKZGkrWJngeAkw.png)

![](https://miro.medium.com/v2/resize:fit:875/1*8NKWjWqA3jEh8-d5K4SgXg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*MZi91j-E_wZ_VXpH3TRkGA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*RtbCJ-wv0-4tjVQUocOLaA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*X1RgTzKKpkBRtypO8qlXiw.png)

You can now start using the new features provided by the installed plugins in your Jenkins pipelines and configurations.

**13.4 Add Services Providers Credentials**

How to add GitHub, Docker, or AWS credentials into Jenkins, click on “Jenkins” to access global credentials or a specific domain to limit the scope. — Choose “Add Credentials” to create a new set of credentials. — Select the appropriate credential type, such as “Username with password” or “SSH Username with private key,” depending on your Git authentication method.

![](https://miro.medium.com/v2/resize:fit:875/1*BNcVccrUxhDgwcq5JxSauQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*-BddNoW6vWc0YCn8tL_2jg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*Eger_tnXMDjsf1tqluPrdg.png)

Setting your Docker Credentials

![](https://miro.medium.com/v2/resize:fit:875/1*-ZBagvy34OU2D0I-lblw4w.png)

Jenkins Global Credentials

# 14. Create a new Jenkins Job

Jenkins Jobs are a given set of tasks that run sequentially as defined by the user. Any automation implemented in Jenkins is a Jenkins Job. These jobs are a significant part of Jenkins’s build process. We can create and build Jenkins jobs to test our application or project. In this chapter, we are going to explore many scenarios of how to run Jenkins build, we will also establish a webhook connection between our Jenkins server with aws ec2 to listen to every push event from developers

**Below is a step-by-step process to create a job in Jenkin.**

1. Login to Jenkins. …
2. Create a New Item. …
3. Enter Item details. …
4. Enter Project details. …
5. Enter the repository URL. …
6. Tweak the settings. …
7. Save the project. …
8. Build Source code.

![](https://miro.medium.com/v2/resize:fit:875/1*p_MrNolefD7XpgFDHbv5fg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*xKhUKtw_Ye6GzKBh86ihvw.png)

![](https://miro.medium.com/v2/resize:fit:875/1*NhbnBFNlo6J4VRCt-kUF8g.png)

![](https://miro.medium.com/v2/resize:fit:875/1*iw-mcpbJeHnUWCNkbBOT9g.png)

Next, we are going add a new **webhook in GitHub**, to establish a webhook connection between our Jenkins server with aws ec2 to listen to every push event from developers.

In your **GitHub** repository, go to “Settings” > “**Webhooks**” > “Add webhook.” Enter the Jenkins webhook URL (usually in the format [http://jenkins-server/github-webhook/)](http://jenkins-server/github-webhook/)) and select the events that should trigger the webhook (e.g., push events).

![](https://miro.medium.com/v2/resize:fit:875/1*XIA2NQNeU9OwvwAfbGI8wQ.png)

Settings up webhook Step 1

![](https://miro.medium.com/v2/resize:fit:875/1*h7pljsUIY4lSqwqXTL7PCQ.png)

Settings up webhook Step 2

![](https://miro.medium.com/v2/resize:fit:875/1*G3FWuSgfjmoggRzjJOMWgw.png)

Here is the template Jenkinsfile that you can customize as we progress

pipeline{  
    agent any  
     options {  
        buildDiscarder(logRotator(numToKeepStr: '3'))  
      }  
      environment {  
        DOCKERHUB_CREDENTIALS = credentials('globaldockerhub')  
        appName = "server"  
        registry = ""  
        registryCredential = ""  
        projectPath = ""  
        AWS_ACCESS_KEY_ID = credentials('your_aws_access_key_id')  
        AWS_SECRET_ACCESS_KEY = credentials('your_aws_secret_access_key')  
        AWS_REGION = 'your_aws_region'  
        EC2_INSTANCE = 'your_ec2_instance_id'  
        SSH_KEY = credentials('your_ssh_key')  
      }  
    stages {  
  
            stage('Environment'){  
            steps {  
                sh 'python3 --version'  
                    git url: 'https://github.com/joelwembo/django-multitenant-saas-ecommerce-kubernetes.git'   
                }  
          
            }  
            stage('Build'){   
                steps  {  
                  
                    sh 'docker build -t joelwembo/cloudapp-django-web:latest --no-cache .'  
                }  
            }  
  
            stage('SonarQube Analysis') {  
                environment {  
                    // Set environment variables required for SonarQube scanner  
                    SONAR_SCANNER_HOME = tool 'SonarQube Scanner'  
                }  
                steps {  
                    // Run SonarQube scanner  
                    script {  
                        withSonarQubeEnv('SonarQube Server') {  
                            sh "${env.SONAR_SCANNER_HOME}/bin/sonar-scanner"  
                        }  
                    }  
                }  
           }  
  
            stage('Login') {  
                steps {  
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'  
                      
                }  
            }  
  
            stage('trivy Scan') {  
                steps {  
                    sh 'trivy image joelwembo/cloudapp-django-web:latest'  
                }  
            }  
  
           stage('Docker Push') {  
                steps {  
                    sh 'docker images'  
                    sh 'docker images --filter "reference=django_app*"'   
                    sh 'docker push joelwembo/cloudapp-django-web:latest'  
                }  
            }  
            stage('Run the Application'){  
                steps {  
                    sh 'docker-compose up -d'  
                }  
            }  
  
         stage('Deploy to AWS EC2') {  
            steps {  
                 dir('deployments') {  
                    sh "pwd"  
                    sh "chmod +x -R ./deploy-aws-ec2.sh"  
                    sh 'docker images --filter "reference=cloudapp-django-web*"'   
                    sh './deploy-aws-ec2.sh'  
                 }  
                
            }  
        }   
    }  
  
    post {  
            success {  
                script {  
                    currentBuild.result = 'SUCCESS'  
                    slackSend(color: 'good', message: "Deployment successful! :tada:", channel: "#DEV")  
                    emailext subject: 'Deployment Successful',  
                            body: 'Deployment was successful!',  
                            recipientProviders: [[$class: 'CulpritsRecipientProvider']]  
                }  
            }  
            failure {  
                script {  
                    currentBuild.result = 'FAILURE'  
                    slackSend(color: 'danger', message: "Deployment failed. :x:", channel: "#DEV")  
                    emailext subject: 'Deployment Failed',  
                            body: 'Deployment failed!',  
                            recipientProviders: [[$class: 'CulpritsRecipientProvider']]  
                }  
            }  
  
        }  
  
}

> **Important Notes:**

- Replace placeholders like `YOUR_ACCESS_KEY`, `YOUR_SECRET_KEY`, `your-cluster-name`, etc. with your actual values.
- Adjust the paths to your Kubernetes deployment files and values files accordingly.

![](https://miro.medium.com/v2/resize:fit:754/1*9ESmWmHzrJUnIBtWIu53LA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*yTlDee1oWTPhsvGqX2HxEA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*Ejl-51ljGcnBv1XHMbaqfw.png)

![](https://miro.medium.com/v2/resize:fit:875/1*Exa0iVuWGqz7kE3qUpyUkw.png)

![](https://miro.medium.com/v2/resize:fit:875/1*lFf3QGCacZtbDoQVatRuAQ.png)

Pushing Django app to the docker hub

![](https://miro.medium.com/v2/resize:fit:654/1*YIYt3qvz03BELEL4u6RHUw.png)

pushing Django app to the docker hub

![](https://miro.medium.com/v2/resize:fit:875/1*5ASInhDZvHDN37EET3GIgg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*xZp3CaWcnc-Ngt3Z0eycYQ.png)

Docker images pushed

![](https://miro.medium.com/v2/resize:fit:875/1*SvgDzO-GS1i_Gq9KPbcSkQ.png)

docker image details

## Advantages of using Jenkins

- Jenkins is being managed by the community which is very open.
- So far around 280 tickets have closed, and the project publishes a stable release every three months.
- As technology grows, so does Jenkins. So far Jenkins has around 320 plugins published in its plugins database.
- Jenkins tool also supports cloud-based architecture so that you can deploy Jenkins in cloud-based platforms.

## Disadvantages of using Jenkins

- Though Jenkins is loved by many developers, it’s not that easy to maintain it because Jenkins runs on a server and requires some skills as a server administrator to monitor its activity.
- Continuous integrations regularly break due to some small setting changes. Continuous integration will be paused and therefore requires some developer attention.

# 15. **Kubernetes Orchestration &** Continuous Delivery with ArgoCD

> Kubernetes is an open-source container orchestration system for automating software deployment, scaling, and management. Originally designed by Google, the project is now maintained by a worldwide community of contributors, and the trademark is held by the Cloud Native Computing Foundation

Now we just need to set EKS Cluster and install ArgoCD

**We are going to add scripts into our Jenkins ( installer. sh ) to install AWS CLI, eksctl, kubectl in to Create, and interact with EKS Cluster in AWS.**

![](https://miro.medium.com/v2/resize:fit:875/1*6Ckb47lIKMt4F_jKdnTYiQ.png)

Update your installer.sh

AWS CLI Installation script

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"  
unzip awscliv2.zip  
sudo ./aws/install  
# Check AWS CLI version  
aws --version

AWS EKS installation script

curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp  
sudo mv /tmp/eksctl /usr/local/bin   
eksctl version  
echo "eksctl Installed successfully installer"

Let us Install kubectl

curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.27.1/2023-04-19/bin/linux/amd64/kubectl  
chmod +x ./kubectl  
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH  
echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc  
kubectl version --short --client

Command to Create AWS EKS Cluster using eksctl command

eksctl create cluster - name <name-of-cluster> - nodegroup-name <nodegrpname> - node-type <instance-type> - nodes <no-of-nodes>  
eksctl create cluster - name django_cluster - nodegroup-name ng-test - node-type t3.medium - nodes 2

![](https://miro.medium.com/v2/resize:fit:875/1*PDCTqI5uWCODyVmFJgz4Mw.png)

AWS EKS Cluster provisioning demo

![](https://miro.medium.com/v2/resize:fit:875/1*rzjBgp6unI_HAd3xhaftuQ.png)

Demo provisioning using command

> The following bash script is **optional ( Expert Only )**, you can create an actual bash script file that can help you create and monitor the progress of You are CloudFormation stack provisioning eks cluster in your aws account

usage_description="  
Sets up a test AWS EKS cluster using eksctl with 3 worker nodes in a 1-4 node AutoScaling group  
  
Takes about 20 minutes - uses CloudFormation to first create a stack with an EKS cluster management plane, then another stack with a node group,  
and finally configures kubectl config with a context in the form of \$email@\$clustername.\$region.eksctl.io  
  
Environment variables to configure:  
  
EKS_CLUSTER - default: 'test'  
EKS_VERSION - default: 1.21 - you should probably set this to the latest supported to avoid having to upgrade later  
AWS_DEFAULT_REGION - default: 'eu-west-2'  
AWS_ZONES - defaults to zones a, b and c in AWS_DEFAULT_REGION (eg. 'eu-west-2a,eu-west-2b,eu-west-2c') - may need to tweak them anyway to work around a lack of capacity in zones. Must match AWS_DEFAULT_REGION  
"  
  
# used by usage() in lib/utils.sh  
# shellcheck disable=SC2034  
usage_args="[<cluster_name> <kubernetes_version> <region> <aws_zones>]"  
  
help_usage "$@"  
  
#min_args 1 "$@"  
  
if ! command -v eksctl &>/dev/null; then  
    "$srcdir/../setup/install_eksctl.sh"  
    echo  
fi  
  
EKS_CLUSTER="${1:-${EKS_CLUSTER:-test}}"  
EKS_VERSION="${2:-${EKS_VERSION:-1.21}}"  
# set a default here as needed to infer zones if not set  
AWS_DEFAULT_REGION="${3:-${AWS_DEFAULT_REGION:-eu-west2}}"  
AWS_ZONES="${4:-${AWS_DEFAULT_REGION}a,${AWS_DEFAULT_REGION}b,${AWS_DEFAULT_REGION}c}"  
  
# shellcheck disable=SC2013  
for zone in ${AWS_ZONES//,/ }; do  
    region="${zone::${#zone}-1}"  
    if [ "$region" != "$AWS_DEFAULT_REGION" ]; then  
        usage "invalid zone '$zone' given, must match region '$AWS_DEFAULT_REGION'"  
    fi  
done  
  
# cluster will be called "eksctl-$name-cluster", in this case "eksctl-test-cluster"  
timestamp "Creating AWS EKS cluster via eksctl"  
eksctl create cluster --name "$EKS_CLUSTER" \  
                      --version "$EKS_VERSION" \  
                      --region "$AWS_DEFAULT_REGION" \  
                      --zones "$AWS_ZONES" \  
                      --managed \  
                      --nodegroup-name standard-workers \  
                        --node-type t3.micro \  
                        --nodes 3 \  
                        --nodes-min 1 \  
                        --nodes-max 4

Another option, to provision the aws eks cluster is to use Terraform, if you are interested, you can follow this tutorial [**The Guide to Terraform DevOps: Implementing CI/CD Pipelines for EKS workloads with GitHub Actions for Multi-Environments Approach**](https://medium.com/towards-aws/the-guide-to-terraform-devops-implementing-ci-cd-pipelines-for-eks-workloads-with-github-actions-b6a08cc984b0)

Let's add these script solutions to Jenkinsfile to automate the deployment of our docker image to the AWS EKS Cluster.

pipeline {  
    agent any  
      
    environment {  
        AWS_REGION = 'us-east-1'  
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')  
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')  
        DOCKER_REGISTRY_URL = 'docker.io'  
        EKS_CLUSTER_NAME = 'mycluster'  
        EKS_NAMESPACE = 'default'  
        APP_NAME = 'joelwembo/cloudapp-django-web'  
        DOCKER_IMAGE_TAG = 'latest'  
    }  
      
    stages {  
        stage('Checkout') {  
            steps {  
                // Checkout your source code repository  
                git 'https://github.com/joelwembo/django-multitenant-saas-ecommerce-kubernetes.git'  
            }  
        }  
          
        stage('Build Docker Image') {  
            steps {  
                script {  
                    // Build your Docker image  
                    docker.build("${DOCKER_REGISTRY_URL}/${APP_NAME}:${DOCKER_IMAGE_TAG}")  
                }  
                  
            }  
        }  
          
        stage('Push Docker Image to Registry') {  
            steps {  
                script {  
                    // Push your Docker image to the registry  
                    docker.withRegistry(DOCKER_REGISTRY_URL, 'globaldockerhub') {  
                        docker.image("${DOCKER_REGISTRY_URL}/${APP_NAME}:${DOCKER_IMAGE_TAG}").push()  
                    }  
                }  
                  
            }  
        }  
  
        stage('Create EKS Cluster') {  
            steps {  
                script {  
                    sh "eksctl create cluster --name $EKS_CLUSTER_NAME --nodegroup-name ng-test - node-type t3.medium - nodes 2"  
                      
                }  
            }  
        }  
  
        stage('Update Kubeconfig') {  
            steps {  
                script {  
                    sh "aws eks --region us-east-1 update-kubeconfig --name mycluster"  
                      
                }  
            }  
        }  
          
        stage('Deploy to EKS') {  
            steps {  
                script {  
                    // Authenticate with AWS EKS  
                    sh "aws eks --region us-east-1 update-kubeconfig --name mycluster"  
                      
                    // Deploy to EKS // k8s deployments folder  
                    sh "kubectl apply -f deployments/k8s/deployment.yaml --namespace=default"  
                }  
            }  
        }  
    }  
}

‘Suivant!’ Let's edit the Kubernetes deployment file for the Django app

kind: Deployment  
apiVersion: apps/v1  
metadata:  
  name: cloudapp-django-web  
spec:  
  replicas: 2  
  selector:  
    matchLabels:  
      app: cloudapp-django-web  
  template:  
    metadata:  
      labels:  
        app: cloudapp-django-web  
    spec:  
      containers:  
      - name: cloudapp-django-web  
        image: joelwembo/cloudapp-django-web:latest  
        resources:  
            limits:  
              memory: 200Mi  
            requests:  
              cpu: 100m  
              memory: 200Mi  
        ports:  
        - containerPort: 80      

![](https://miro.medium.com/v2/resize:fit:875/1*ng0YhB1IKkHzmqt01k6z5A.png)

![](https://miro.medium.com/v2/resize:fit:875/1*7wS_kRzmxms32xnjxOWIGw.png)

![](https://miro.medium.com/v2/resize:fit:875/1*Ra4DgsCQSFz1JvrZcJuEtA.png)

Lunching EKS Cluster Pipeline Prod

![](https://miro.medium.com/v2/resize:fit:875/1*OeXWMiU-Wb6A7PtLObRlBw.png)

**15.1 Let's add SonarQube Code Scanning**

> Configure your SonarQube server(s): Log into Jenkins as an administrator and go to Manage Jenkins > Configure System. Scroll down to the SonarQube configuration section, click Add SonarQube, and add the values you’re prompted for. The server authentication token should be created as a Secret Text credential.

![](https://miro.medium.com/v2/resize:fit:875/1*p8yQibTRHXL8TbWOkX2w2Q.png)

SonarQube Plugin in Jenkins

![](https://miro.medium.com/v2/resize:fit:875/1*5Uc-POKb4Ol3F4YlorEt0A.png)

![](https://miro.medium.com/v2/resize:fit:875/1*UKDij7zQ-AZTMYA_kuWcYQ.png)

Verify your SonarQube Installation in Jenkins

Go to Jenkins Dashboard -> Manage Jenkins > System to configure SonarQube servers

![](https://miro.medium.com/v2/resize:fit:875/1*FWHeRdXs0-ptpLwuZeMVIg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*aFG4rnuDFSK1fIWEn4eTcQ.png)

SonarQube Servers settings

- SSH into the EC2 instance.
- Follow the official SonarQube documentation for Ubuntu installation: [https://docs.sonarqube.org/latest/setup/install-server/](https://docs.sonarqube.org/latest/setup/install-server/)

> **Certain parts of this handbook will be removed or skipped to avoid redundancy and to save reading time**

**15.1.1 Install Postgres and create a user**

sudo vim /etc/sysctl.conf

  
# These configurations must be added to this file.  
  
vm.max_map_count=262144  
fs.file-max=65536  
ulimit -n 65536  
ulimit -u 4096

![](https://miro.medium.com/v2/resize:fit:875/0*3YKbXiraHAjEazw-.png)

15.1.2 Configure Sonar User and DB

![](https://miro.medium.com/v2/resize:fit:875/1*afZfts7ABB38KVwHz94FvQ.png)

PostgreSQL is now installed. After that, SonarQube, JDK 11, and ZIP will be installed.

sudo wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.8.0.63668.zip  
sudo unzip sonarqube-9.8.0.63668.zip  
sudo mv sonarqube-9.8.0.63668 /opt/sonarqube  
sudo groupadd sonar  
sudo useradd -d /opt/sonarqube -g sonar sonar  
sudo chown sonar:sonar /opt/sonarqube -R

cd /opt/sonarqube/extensions/plugins  
sudo wget https://github.com/mc1arke/sonarqube-community-branch-plugin/releases/download/1.14.0/sonarqube-community-branch-plugin-1.14.0.jar

Sonarqube-community-branch-plugin-1.14.0.jar is required because I installed version 9.8 for SonarQube. This directory, “/opt/sonarqube/extensions/plugins,” is where we need to install them.

The SonarQube configuration file must then be configured.

sudo vim /opt/sonarqube/conf/sonar.properties

These configurations must be added to this file.

sonar.jdbc.username=sonar  
sonar.jdbc.password=postgres  
sonar.jdbc.url=jdbc:postgresql://localhost:5432/sonarqube  
  
sonar.web.javaAdditionalOpts=-javaagent:/opt/sonarqube/extensions/plugins/sonarqube-community-branch-plugin-1.14.0.jar=web  
sonar.ce.javaAdditionalOpts=-javaagent:/opt/sonarqube/extensions/plugins/sonarqube-community-branch-plugin-1.14.0.jar=ce

This file is now required for SonarQube to run as a service.

sudo vim /etc/systemd/system/sonar.service

Add the following to the file.

[Unit]  
Description=SonarQube service  
After=syslog.target network.target  
[Service]  
Type=forking  
ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start  
ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop  
User=sonar  
Group=sonar  
Restart=always  
LimitNOFILE=65536  
LimitNPROC=4096  
[Install]  
WantedBy=multi-user.target

**15.1.2 The next step is to enable and start SonarQube as a service.**

sudo systemctl enable sonar  
sudo systemctl start sonar  
sudo systemctl status sonar

![](https://miro.medium.com/v2/resize:fit:875/1*3_illZ7MPUM0KfcDi0Kkfg.png)

- Once SonarQube is installed and running, access it through
- http://<public-ip>:9000

To log in to SonarQube use, Username and Password both: admin

![](https://miro.medium.com/v2/resize:fit:875/0*UXPCAAK_JFRV_f4D.png)

**15.1.3 If you don’t want to install SonarQube** within your ec2 instance, you can also opt for SonarCloud (Optional):

> SonarCloud is designed to help you achieve a state of Clean Code, that is, code with attributes that contribute to making your software reliable, maintainable, and secure. To do this, SonarCloud identifies both issues and security hotspots in your code.

![](https://miro.medium.com/v2/resize:fit:721/1*QQRikZaae2wYHEjohgX1bA.png)

Authorize SonarCloud to your Github Repo

![](https://miro.medium.com/v2/resize:fit:776/1*oQbuHk3q0y88xC_wlALF8g.png)

Choose Organization

![](https://miro.medium.com/v2/resize:fit:875/1*acGKD3qRNxi9evARWl2p2w.png)

![](https://miro.medium.com/v2/resize:fit:875/1*UH8M4doG7tsZfTFVa6amPg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*pKOUYe1EQt9Ti23Bltz0gw.png)

**15.1.4 Add the following stage** in your **Jenkinsfile** stages :

 stage('SonarQube Analysis') {  
                environment {  
                    // Set environment variables required for SonarQube scanner  
                    SONAR_SCANNER_HOME = tool 'SonarQube Scanner'  
                }  
                steps {  
                    // Run SonarQube scanner  
                    script {  
                        withSonarQubeEnv('SonarQube Server') {  
                            sh "${env.SONAR_SCANNER_HOME}/bin/sonar-scanner"  
                        }  
                    }  
                }  
           }

![](https://miro.medium.com/v2/resize:fit:875/1*EqjfMS-E1KZ33NL5LxEkkw.png)

SonarQube Code Analysis and Quality Control

![](https://miro.medium.com/v2/resize:fit:875/1*si8L6_d6_hmM0jzYjUux_A.png)

**15.2 Let's add Trivy Scan**

> **Trivy** (pronunciation) is a comprehensive and versatile security **scanner**. **Trivy** has scanners that look for security issues, and targets where it can find those …

1. **Edit your Jenkins Stages**, add this stage right before pushing the image to the docker registry :

  
stage('Build') {  
      steps {  
        sh 'docker build -t joelwembo/cloudapp-django-web:latest .'  
      }  
    }  
  
stage('trivy Scan') {  
      steps {  
        sh 'trivy image joelwembo/cloudapp-django-web:latest'  
      }  
    }

**2. Update your Dockerfile** to give trivy scan access to read your GitHub repo

# Run vulnerability scan on build image  
FROM build AS vulnscan  
COPY --from=aquasec/trivy:latest /usr/local/bin/trivy /usr/local/bin/trivy  
RUN trivy rootfs --no-progress /

Here are the full updated **Dockerfile instructions**

# Use an official Python runtime as a parent image  
FROM python:3.11-slim-bullseye as build  
# Set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1  
ENV PYTHONUNBUFFERED 1  
# Set the working directory in the container  
WORKDIR /app  
# Copy the requirements file into the container at /app  
COPY requirements.txt /app/  
COPY apps /app/  
COPY media /app/  
COPY multitenantsaas /app/  
# COPY staticfiles /app/  
COPY tests /app/  
COPY .env /app/  
COPY manage.py /app/  
  
  
RUN pip install --upgrade pip  
RUN pip install --upgrade setuptools  
# Install any needed packages specified in requirements.txt  
# RUN pip install --no-cache-dir -r requirements.txt  
RUN pip install -r requirements.txt  
# Copy the current directory contents into the container at /app  
# COPY . /app/  
  
# Run vulnerability scan on build image  
FROM build AS vulnscan  
COPY --from=aquasec/trivy:latest /usr/local/bin/trivy /usr/local/bin/trivy  
RUN trivy rootfs --no-progress /  
  
EXPOSE 8585  
EXPOSE 8000

3. **Install Trivy** in your ec2 instance ( Optional )

wget https://github.com/aquasecurity/trivy/releases/download/v0.18.3/trivy_0.18.3_Linux-64bit.deb  
sudo dpkg -i trivy_0.18.3_Linux-64bit.deb

![](https://miro.medium.com/v2/resize:fit:875/1*ZP3P_ZZEIyikfbR5SmxLAA.png)

Trivy Scan Using Dockerfiles and Jenkins

![](https://miro.medium.com/v2/resize:fit:875/1*XcKVaRfaQNOdr9-W5J38xg.png)

Scanning for security vulnerability

![Jenkins Job for Scanning for security vulnerability and potential dangers before pushing to docker hub](https://miro.medium.com/v2/resize:fit:875/1*4YiztmDkb2vCYVHrIBb9Mw.png)

Jenkins Job for Scanning for security vulnerabilities and potential dangers before pushing to the docker hub

You can also run the trivy scanning command from your EC2 dev server without a Jenkins server to check for image security issues.

![](https://miro.medium.com/v2/resize:fit:875/1*gBsueilGMyqjDEyeX2Py6w.png)

![](https://miro.medium.com/v2/resize:fit:875/1*vcmF3ePquVgQI2N2dl8_zQ.png)

Trivy Image scan

![](https://miro.medium.com/v2/resize:fit:1250/1*OYUFXK6xTrSrj6zV1m7rEA.png)

# 16. Check the result using your aws ec2 terminal and aws management console

![](https://miro.medium.com/v2/resize:fit:875/1*K62JojeZLj4GT7H704e4_Q.png)

![](https://miro.medium.com/v2/resize:fit:875/1*LqhPg9mFwlvu8QsIyNa22Q.png)

![EKS Cluster With Jenkins by Joel Wembo](https://miro.medium.com/v2/resize:fit:1250/1*IUR-1xCY4rswf-yfmMOdYw.png)

EKS Cluster With Jenkins

Use the following command to list all clusters in your AWS account:

aws eks list-clusters

![](https://miro.medium.com/v2/resize:fit:365/1*7zewNIB3gncDuUyrgKeNcQ.png)

Cluster, service, and pods in AWS EKS Control plane:

![](https://miro.medium.com/v2/resize:fit:875/1*UZk2DftL4rJY9_tsfFt0LA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*lg3IARkj7Noe0ptD4Xpowg.png)

django app deployment details

![](https://miro.medium.com/v2/resize:fit:1250/1*2-5SOiYuY_gqQt3ILrZd7g.png)

View All Pods in the EKS Control Plane

![](https://miro.medium.com/v2/resize:fit:1250/1*FMiBqf25Qng8y7anctl26Q.png)

Running Pod in EKS Control Plane

![](https://miro.medium.com/v2/resize:fit:875/1*z46lQaNaJSokY01gD0nnKA.png)

**EKS Cluster is up and ready**

# **17. Continuous Delivery with ArgoCD**

> Argo CD is a declarative continuous delivery tool for Kubernetes. It can be used as a standalone tool or as a part of your CI/CD workflow to deliver needed resources to your clusters.

![](https://miro.medium.com/v2/resize:fit:875/0*7UgFEXURmOZ_dEOL.png)

ArgoCD System Design using Jenkins and K8s

> EKS Cluster is up and ready.
> 
> Now lets install ArgoCD in EKS Cluster

**Step 1**: I**nstall ArgoCD in EKS Cluster**

# This will create a new namespace, argocd, where Argo CD services and application resources will live.  
kubectl create namespace argocd  
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

![](https://miro.medium.com/v2/resize:fit:875/1*R6AjjzJ3cT_kpnmLcM982A.png)

ArgoCD Installation

**Step 2 : Download Argo CD CLI**

curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64  
sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd  
rm argocd-linux-amd64

> Quick note : All the installation script of eks, aws cli, and argoCD were already added during aws ec2 provisioning using terraform . All you need to do is update your installer.sh with the above script . You can also work with your ArgoCD CLI using any ubuntu server at this state of the tutorial

**Step 3: Change the ArgoCD password**

kubectl -n argocd patch secret argocd-secret -p '{"stringData": { "admin.password": "$2a$10$rRyBsGSHK6.uc8fntPwVIuLVHgsAhAX7TcdrqW/RADU0uh7CaChLa",  "admin.passwordMtime": "'$(date +%FT%T%Z)'" }}'

You can view your newly created password or secrets here in the AWS EKS Control plane as well :

![](https://miro.medium.com/v2/resize:fit:1250/1*vqoPsZqordYGzUofcFuqVQ.png)

Because Kubernetes deploys services to arbitrary network addresses inside your cluster, you’ll need to forward the relevant ports in order to access them from your local machine. Argo CD sets up a service named `argocd-server` on port 443 internally. Because port 443 is the default HTTPS port, and you may be running some other HTTP/HTTPS services, it’s common practice to forward those to arbitrarily chosen other ports, like `8080`, like so:

**Step 4: Access ArgoCD UI**

kubectl port-forward svc/argocd-server -n argocd 8383:443 --address 0.0.0.0 &

![](https://miro.medium.com/v2/resize:fit:875/1*AbX6VWxssa_QIEZrJkVQKg.png)

In the meantime, you should be able to access Argo CD in a web browser by navigating to `localhost:8383 or any port of your choice`. However, you’ll be prompted for a login password which you’ll need to use the command line to retrieve in the next step. You’ll probably need to click through a security warning because Argo CD has not yet been configured with a valid SSL certificate.

![](https://miro.medium.com/v2/resize:fit:875/1*pJ5naQonhUwle1X6DDxMEQ.png)

ArgoCD successfully installed

To log in to ArgoCD, get the initial password using the next command:

argocd admin initial-password -n argocd

![](https://miro.medium.com/v2/resize:fit:875/1*z1slQLBt-Yv0NNf9om5Kyg.png)

## **Step 5:** ArgoCD Load Balancer in EKS

> Load balancers improve application performance by increasing response time and reducing network latency. They perform several critical tasks such as the following: Distribute the load evenly between servers to improve application performance. Redirect client requests to a geographically closer server to reduce latency.

# Change the argocd-server service type to LoadBalancer.  
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'

![](https://miro.medium.com/v2/resize:fit:875/1*64l5LuU_zAaTVhBgHBoSNA.png)

Next, let's get the load balancer DNS URL

kubectl get svc -n argocd

![](https://miro.medium.com/v2/resize:fit:875/1*4y6KC9V_B2jJkqkdiKtrGQ.png)

## Step 6: Let access the AWS EKS ArgoCD GUI

![](https://miro.medium.com/v2/resize:fit:1250/1*YNgU_KOAJbdHw7-jFCqBxQ.png)

![](https://miro.medium.com/v2/resize:fit:1250/1*TCl-eQWmmwJQK--7uffNFQ.png)

ArgoCD EKS Cluster URL

![](https://miro.medium.com/v2/resize:fit:1250/1*Vx3Nmte9I16NBOgWIRanWQ.png)

ArgoCD pods running in your EKS Cluster

![](https://miro.medium.com/v2/resize:fit:875/1*jwSO562SJy526M3B94FlVg.png)

Argo CD create app

![](https://miro.medium.com/v2/resize:fit:875/1*IGstA1TCyYOurKRzFFqIOQ.png)

Specify the repo URL and branch

![](https://miro.medium.com/v2/resize:fit:1250/1*VQCIgkbZoXqIISFfnx-lvA.png)

![](https://miro.medium.com/v2/resize:fit:1250/1*4zNu-WeYRM79dvcJ_BwaiQ.png)

ArgoCD Deploying eks cluster

![](https://miro.medium.com/v2/resize:fit:1250/1*XC1IpBfsa07r6hs94dFbvQ.png)

![](https://miro.medium.com/v2/resize:fit:1250/1*d-tHalfVKRwEZjwnAPF58g.png)

> Argo CD has the ability to automatically sync an application when it detects differences between the desired manifests in Git, and the live state in the cluster. A benefit of automatic sync is that CI/CD pipelines no longer need direct access to the Argo CD API server to perform the deployment.

![](https://miro.medium.com/v2/resize:fit:1250/1*xsEuT4U6KGMz5EiB9BI7kw.png)

Now let's **automate** ArgoCD with an Amazon EKS (Elastic Kubernetes Service) cluster via **Jenkinsfile** [**posted here**](https://github.com/joelwembo/django-multitenant-saas-ecommerce-kubernetes/blob/master/deployments/Jenkins/JenkinsfileArgoCDTemplate) [https://github.com/joelwembo/django-multitenant-saas-ecommerce-kubernetes/blob/master/deployments/Jenkins/JenkinsfileArgoCDTemplate](https://github.com/joelwembo/django-multitenant-saas-ecommerce-kubernetes/blob/master/deployments/Jenkins/JenkinsfileArgoCDTemplate)

stage('Deploy') {  
            steps {  
                // Deploy to Argo CD  
                script {  
                    // Install argocd CLI if not already installed  
  
                    // Login to Argo CD (replace placeholders with your Argo CD credentials)  
                    sh 'argocd login <ARGOCD_SERVER> --insecure --username=<USERNAME> --password=<PASSWORD>'  
                      
                    // Sync your application with Argo CD (replace placeholders with your application details)  
                    sh 'argocd app sync <APPLICATION_NAME> --namespace <NAMESPACE>'  
                }  
            }  
        }

![](https://miro.medium.com/v2/resize:fit:875/1*ndhWGN9Y2YH7FSDfEz4qmA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*wQkWTEiZvMhLrdRioRX92A.png)

![](https://miro.medium.com/v2/resize:fit:875/1*qxUuiS1LIvXJOb-gEAb8kA.png)

![](https://miro.medium.com/v2/resize:fit:1250/1*cqQX_S8DhI6G5ovKSS_gXA.png)

Current Django application without a domain name, next we are going to attach an API Gateway and a custom name for our application

![](https://miro.medium.com/v2/resize:fit:875/1*I18h2OqUpuESP-tJUkRHCQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*dPNOASteWl1FvlH5u-ZluQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*4P7wV2yRXTYK-fGpwMPsBg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*-yrs3AMdG3Pp-GQpZkjelg.png)

# 18. **Integrate Django APIs with AWS API Gateway with a custom domain**

Integrating Django APIs with AWS API Gateway and setting up a custom domain involves several steps. Here’s a general overview of the process:

**Step 1 Create API Gateway Endpoint, Choose HTTP API:**

![](https://miro.medium.com/v2/resize:fit:875/1*1vM_i0f8_zdyKmSdomELWw.png)

create stages

![](https://miro.medium.com/v2/resize:fit:875/1*Sgrk2dJpZPMZZKEiaqYzWw.png)

Create a new Integration

![](https://miro.medium.com/v2/resize:fit:875/1*kMojc5OdTfrPzzaRHRMhHQ.png)

**Step 2 : Configure CORS settings.py:**

CORS_ALLOWED_ORIGINS = [  
    "http://127.0.0.1",  
    "http://localhost",  
    "https://792jz173sj.execute-api.us-east-1.amazonaws.com",  
    "https://socialcloudsync.com"  
]

> For Production, you can use your EKS Cluster Load balancer DNS address which was issue earlier using EKS instead of the test environment EC2 IP . Both use cases will work in route53

**Step 3: Request ACM for SSL Certification**

- You can set up SSL/TLS certificates for your custom domain using AWS Certificate Manager (ACM) or a third-party certificate authority.
- Configure your custom domain in API Gateway to use the SSL certificate.

![](https://miro.medium.com/v2/resize:fit:875/1*OikqzRFXStuxuQ-JJ4675A.png)

**Step 4: Create a new Record Routing to your API Gateway main URL**

In your DNS management console (like Route 53 if using AWS), configure the domain’s DNS settings to point to the API Gateway’s custom domain.

![](https://miro.medium.com/v2/resize:fit:875/1*O8ZMwDjNalTvQCuqAb4mkw.png)

![](https://miro.medium.com/v2/resize:fit:875/1*PUvH4bFuIdP82Cwrg6YXHg.png)

After deployment, test the integration by sending requests to the API Gateway endpoint. Ensure that CORS headers are properly handled by your Django application, allowing seamless communication between the API Gateway and your Django REST API.

![Automating Django deployments using Jenkins, Kubernetes Terraform and GitHub Actions](https://miro.medium.com/v2/1*fbXjRdItM14_QB791rWK4Q.png)

Automating Django deployments using **Jenkins**, Kubernetes Terraform, and GitHub Actions

# Clean up Cluster

# delete cluster using eks cli command  
eksctl delete cluster --name <name-of-cluster>

You can also delete the entire resource using CloudFormation in the AWS management console

![](https://miro.medium.com/v2/resize:fit:875/1*ZHwbeRVriugdk8wB9arbGQ.png)

Also, don’t forget to delete your aws ec2 instances that you created using Terraform with these scripts :

     - name: Terraform Destroy All Resources  
      #  if: github.ref == 'refs/heads/master' && github.event_name == 'push'  
       run: terraform destroy -auto-approve -input=false -lock=false    
       env:  
          TFE_TOKEN: ${{ secrets.TF_API_TOKEN }}

![](https://miro.medium.com/v2/resize:fit:875/1*QU98AwjBCtXOToiKqU13gA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*xjsumjK9BSbWkS2DO_dTWw.png)

**For monitoring and logging**, we have published a separate article [**DevOps hands-on Lab: How to provision and monitor EKS Cluster using Prometheus and Grafana Helm Charts**](https://joelotepawembo.medium.com/devops-hands-on-lab-how-to-provision-and-monitor-eks-cluster-using-prometheus-and-grafana-helm-740abfc6b805)

![EKS, Prometheus, Grafana and Helm Charts Architecture by joel wembo](https://miro.medium.com/v2/resize:fit:473/1*WRQY-iwb_7t3vSmn-c_Y4w.png)

EKS, Prometheus, Grafana and Helm Charts Architecture

# Summary

Automating Django deployments using **Jenkins**, Kubernetes [Terraform and GitHub Actions](https://medium.com/towards-aws/the-guide-to-terraform-devops-implementing-ci-cd-pipelines-for-eks-workloads-with-github-actions-b6a08cc984b0) offers a streamlined and reliable way to manage application delivery. This comprehensive guide offers a detailed and hands-on walkthrough for establishing a resilient CI/CD pipeline utilizing AWS EC2, EKS, Jenkins, **terraform,** Docker, SonarQube, and **ArgoCD**. By following the step-by-step instructions, you can successfully automate the build, test, and deployment processes of your applications.