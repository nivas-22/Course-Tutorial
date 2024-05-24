
# **Introduction**

Terraform is an IAAC (Infrastructure As A Code). We can automate our infrastructure using codes. We can define infrastructure as a state. It works with automation tools like Ansible after the infra is set up and ready. Terraform does not have any programming language. It has its syntax domain-specific language similar to JSON.

> Let’s see how we can create an EC2 instance using Terraform. 😎

To do this exercise first we need to download and install Terraform on Windows.

To download Terraform on Windows click on the link below 👇

[

## Install | Terraform | HashiCorp Developer

### Explore Terraform product documentation, tutorials, and examples.

developer.hashicorp.com



](https://developer.hashicorp.com/terraform/install?product_intent=terraform&source=post_page-----71776acf16e3--------------------------------#Windows)

You can also install Terraform using Windows Powershell using the choco command

# Open the PowerShell as admin and run the below command (make sure to install choco package on windows.)  
  
choco install terraform

![](https://miro.medium.com/v2/resize:fit:875/1*ePhsJOojjWld0907KLjjjQ.png)

![](https://miro.medium.com/v2/resize:fit:781/1*KjXJEJMQjnpwU1XJ-vcWgA.png)

**To confirm the terraform is installed you can use this command**

Next, we need to install AWS CLI

![](https://miro.medium.com/v2/resize:fit:875/1*fU-KmxDeY4Y0mgd4ZSEJ5g.png)

**To install AWS CLI enter this command**

Once the AWS CLI is installed we can access the AWS account using the IAM user **access key** and **secret key.**

- If you don’t have access and a secret key for the IAM user then you can create it from the console for the IAM user.

![](https://miro.medium.com/v2/resize:fit:875/1*E66sSn4B9_p9BCoRLInirA.png)

**Go to IAM from the console and follow the below steps**

![](https://miro.medium.com/v2/resize:fit:875/1*c8CL9nik9na3Ak9L_Fmfxg.png)

**Go to users and click on your username, click on the security credentials tab and scroll down**

![](https://miro.medium.com/v2/resize:fit:875/1*iXKQfyKJKXrakY_VJhQJXg.png)

**Under access keys click on create access key**

![](https://miro.medium.com/v2/resize:fit:875/1*nK5YoDYSItB6uN-CFii6ng.png)

![](https://miro.medium.com/v2/resize:fit:875/1*dgLk3Bpac7DA61GTy423gQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*ChD1rAV933myJHlkoD6gyQ.png)

**Download this and keep it safe. Don’t share this access key and secret key with anyone.**

- Once the credentials have been created for the user we can access it using CLI.
- Open Gitbash or any other terminal and follow the below steps;

![](https://miro.medium.com/v2/resize:fit:875/1*GTGQwuvqhqZdvp_GJCkWxw.png)

**Copy and paste your access key and secret. Enter the region code if you are using a different region**

![](https://miro.medium.com/v2/resize:fit:875/1*Onleue0Cb2vk_AQSWDJh8w.png)

**we can get all the terraform commands using the above command as we have already installed the terraform**

![](https://miro.medium.com/v2/resize:fit:875/1*yXMJVkHY0WrM0Ogo9_raXQ.png)

**create a folder and subfolders to save the script to do the exercise**

- Open this folder in Vscode and create a new file called first_instance.tf

![](https://miro.medium.com/v2/resize:fit:875/1*hJQ31lVEUvB7TnTnXQOrmg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*1Gidv8BEkkv7Pe91CpJ_Ww.png)

**go to the path and click on select folder**

![](https://miro.medium.com/v2/resize:fit:738/1*cNYCg3hySHb_E9pIQgwgag.png)

**click on the ‘+’ button and create new file named first_instance.tf (make sure to have .tf extension)**

![](https://miro.medium.com/v2/resize:fit:875/1*BeG6snKa23agOHBodIGtAQ.png)

- Make sure to change the AMI ID _(you can get the AMI ID from the launch instance page. Copy any AMI you want and paste it here)_
- create new key pair if you don’t have and add it under the key name
- Create a new security group from the console paste the **sg id** under **vpc_security_group_ids** and save the file.

# You can copy and paste the below script in the first_instance.tf file (make the above mentioned changes wherever is required)  
  
provider "aws" {  
    region = "us-east-1"  
}  
  
resource "aws_instance" "terraform_instance" {  
  ami = "your-ami-id"  
  instance_type = "t2.micro"  
  availability_zone = "your-avaialablity_zone-name"  
  key_name = "your-keypair-name"  
  vpc_security_group_ids = ["your-security_group-id"]  
  tags = {  
    Name = "Terraform_Instance"  
  }  
}

Now if we go gitbash and open the file we can see the file update in the directory we created.

![](https://miro.medium.com/v2/resize:fit:875/1*f0fDbNgzrmy2BEGskePvLQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*IU9nC0rVbricnodF-Nqe2Q.png)

**terraform init** command will the check provider (which is AWS) and install the necessary plugins for AWS in the current working directory

![](https://miro.medium.com/v2/resize:fit:875/1*9jBO9E9hTYTDFwwoF-MfBg.png)

**Now we can see a new file and directory have been created with the necessary plugins**

Next, we can execute the script but before executing the script it is always best practice to check the syntax error by using the below command 👇

![](https://miro.medium.com/v2/resize:fit:875/1*kceyTe5ZG8S2J27lMFpUqg.png)

**There is no syntax errors in our code. We will make some errors in the code and validate again to see the error.**

![](https://miro.medium.com/v2/resize:fit:875/1*LP8f4KePOOmVPmmF3gvFKg.png)

**I have removed the double quotes from the security group and we can see the terraform validate command is showing that error. You can make any error and also check.**

![](https://miro.medium.com/v2/resize:fit:875/1*aD_Nnr1Z9B0-fPdJxr4-gA.png)

**We can also use this command to set the format and alignment of the code**

Next, we can use the terraform plan command. It will show what this code will do (just like a preview).

![](https://miro.medium.com/v2/resize:fit:875/1*DT08ICy7kM6Az2QaX1Tv1Q.png)

Now we are good to go and apply our terraform script.💪

![](https://miro.medium.com/v2/resize:fit:875/1*r3jhT2IEBAqECUwI1riogA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*pjus9M6wr5woRgz7H6S_kw.png)

Enter the value as **Yes** to launch the instance and wait for sometime

![](https://miro.medium.com/v2/resize:fit:875/1*fyCgHbUrzt2wLnO2GrOP3w.png)

**If we go to the console we can see the instance has been created**

## We have successfully created Ec2 instance using terraform script 😊

# Clean UP 🧹

To delete the instance we created using terraform we can use the below command 👇

![](https://miro.medium.com/v2/resize:fit:875/1*liyrxSLggDXqassn2x3w4Q.png)

![](https://miro.medium.com/v2/resize:fit:875/1*F1oPirHm1LrBKKD_yv0mPA.png)

Enter the value as **Yes**