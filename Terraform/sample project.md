
Hello, in this post, we will create infrastructure on AWS consisting of EC2 and Security Group using Terraform as an infrastructure-as-code tool. If you have never used Terraform before or are still a beginner, this post is perfect for you.

![](https://miro.medium.com/v2/resize:fit:1400/1*rojRn0kPfvk0fKnQElqbRQ.gif)

# Pre-requirements:

- Terraform installed on your local machine
- AWS Account

1. **Create Terrafrom project**

Create a folder for Terraform and open your IDE. Then, create a file named provider.tf. A provider is a plugin that Terraform uses to create and manage your resources.

provider "aws" {  
  region     = "eu-west-3"  
}  
  
terraform {  
  required_providers {  
    aws = {  
      source  = "hashicorp/aws"  
      version = "~> 4.16"  
    }  
  }  
  
  required_version = ">= 1.2.0"  
}

![](https://miro.medium.com/v2/resize:fit:1362/1*uu80RxFZlIkvL5C24b-4OA.png)

**2. Create an EC2 resources**

You can open the documentation at registry.terraform.io to see all the resources that can be created. Create a file named ec2.tf with the following contents:

resource "aws_instance" "web" {  
  ami                    = "ami-008bcc0a51a849165" #ubuntu 20  
  instance_type          = "t3.micro"  
  key_name               = "react-ec2-key"  
  
  tags = {  
    Name = "react-app-ec2" #give your ec2 name here  
  }  
}

For the AMI ID, you can find it in the AWS console under EC2 services. Then, click “Launch instances.”

![](https://miro.medium.com/v2/resize:fit:1400/1*dyTYJZkH7oeS5cfiLaWoBA.png)

Select Ubuntu from the Amazon Machine Image (AMI) options, then copy the AMI ID on the right side.

![](https://miro.medium.com/v2/resize:fit:1400/1*YIwplcgLT5paH6j1bMX0ew.png)

For the instance type, you can use “t3.micro”. This type has 2 vCPUs and 1 GiB of memory.

![](https://miro.medium.com/v2/resize:fit:1400/1*5fc-7rUNJNtnrNKo9Rg31Q.png)

Create a key pair in the AWS console under the EC2 services section and name the key pair according to the Terraform file we created, which is “react-ec2-key”.

![](https://miro.medium.com/v2/resize:fit:1400/1*CxAZ4Ikji4Ycx7DanDYJtw.png)

![](https://miro.medium.com/v2/resize:fit:1400/1*QFuvwfH9PJzha44CwNSBfg.png)

Give your EC2 a name in the tags section:

![](https://miro.medium.com/v2/resize:fit:1128/1*2zIFg-PaDnnlw7QI199o_g.png)

After creating the `ec2.tf` and `provider.tf` files, create an IAM user for Terraform and provide an access key ID.

![](https://miro.medium.com/v2/resize:fit:1400/1*b08uJDUpZ2gTNFhrUSYWlg.png)

pergi ke IAM User, lalu pilih users pada sisi kiri dan click Create user

![](https://miro.medium.com/v2/resize:fit:1400/1*g3F9Vr6oSBHLuqxh1EqtxQ.png)

![](https://miro.medium.com/v2/resize:fit:1400/1*YDqk6hLqbPYOpK83DkyioQ.png)

![](https://miro.medium.com/v2/resize:fit:1400/1*X9oZJiuYgESE189hRq6DvA.png)

Select the IAM user you have created, go to the “Security credentials” tab, and scroll down. Then, click on “Create access key.”

![](https://miro.medium.com/v2/resize:fit:1400/1*sa6XjoDh2NW9g5zmP45cXg.png)

![](https://miro.medium.com/v2/resize:fit:1388/1*NS89J_RPgylUH3i_UAoL-Q.png)

![](https://miro.medium.com/v2/resize:fit:1400/1*u5QbzQv95WcK69mZtbAMaQ.png)

After creating the IAM user, the next step is to set up AWS configure in the terminal to log in to AWS using the access key ID we created.

![](https://miro.medium.com/v2/resize:fit:774/1*mTRi9Fb81EQsqRg-5ejoKw.png)

Run `terraform init` in your local terminal.

![](https://miro.medium.com/v2/resize:fit:1400/1*PfnW1gZXuPBG27SCanvuAg.png)

After that, run `terraform plan` to see what resources Terraform will create in AWS.

![](https://miro.medium.com/v2/resize:fit:1400/1*JXzw6NI5CSWvLKfoZjpc9w.png)

Run `terraform apply` to deploy the resources to AWS.

![](https://miro.medium.com/v2/resize:fit:1242/1*dICRHZzX_DQEjTtKFFPDAg.png)

After the deployment is complete, you can check in the “EC2” services by selecting “Instances.”

![](https://miro.medium.com/v2/resize:fit:1400/1*QYT6hBqINiUVv6gHPld8Aw.png)

3. Create a Security Group

Look at the EC2 instance you created. If you haven’t defined a security group, it will use the default security group by default.

![](https://miro.medium.com/v2/resize:fit:1400/1*Awapwnsy6uaOgDwjwyXsFw.png)

Next, we will create a security group using Terraform. Copy below code

resource "aws_security_group" "security_group_react" {  
  name        = "react1-sg"  
  description = "allow http port"  
  vpc_id      = "vpc-0e80cba955b082b42"  
  
  ingress {  
    description = "allow http"  
    from_port   = 80  
    to_port     = 80  
    protocol    = "tcp"  
    cidr_blocks = ["0.0.0.0/0"]  
  }  
  
  ingress {  
    description = "allow http"  
    from_port   = 22  
    to_port     = 22  
    protocol    = "tcp"  
    cidr_blocks = ["0.0.0.0/0"]  
  }  
  
  egress {  
    from_port   = 0  
    to_port     = 0  
    protocol    = "-1"  
    cidr_blocks = ["0.0.0.0/0"]  
  }  
  
  tags = {  
    Name = "react1-sg"  
  }  
}

![](https://miro.medium.com/v2/resize:fit:1400/1*eMKfeUN8h5e3e9-4x1ps6Q.png)

Add “vpc_security_group_ids” block to ec2.tf

resource "aws_instance" "web" {  
  ami                    = "ami-008bcc0a51a849165" #ubuntu 20  
  instance_type          = "t3.micro"  
  key_name               = "react-ec2-key"  
  vpc_security_group_ids = [aws_security_group.security_group_react.id]  
  
  tags = {  
    Name = "react-app-ec2" #give your ec2 name here  
  }  
}

![](https://miro.medium.com/v2/resize:fit:1400/1*j9Wy8F_aKjLtl0aNqmihGQ.png)

Run `terraform plan` and `terraform apply` again after creating the Terraform configuration for the security group.

To check that port 80 is working after we open the port at Securitu Group, we will install Nginx on the EC2 instance.

sudo apt-get update

sudo apt install nginx -y

Copy the public ip of EC2 instances and paste to your browser

![](https://miro.medium.com/v2/resize:fit:1400/1*EfrTehqqIodwWP95libWhg.png)

You can view the full Terraform code we created earlier at this link: [https://github.com/rizkiprass/terraform-medium](https://github.com/rizkiprass/terraform-medium) in the “simple-ec2” folder.

![](https://miro.medium.com/v2/resize:fit:1400/1*uSdwJRPZB9Tl65aW6Q-GxA.png)

Congratulations, you have successfully deployed EC2 using Infrastructure as a Code Terraform.