
Deploying cloud infrastructure manually may have numerous disadvantages: Manual deployments are vulnerable to human error, inclusive of misconfigurations, typos, or overlooking essential steps. These mistakes can cause downtime, protection vulnerabilities, or overall performance issues. It can bring about inconsistencies throughout environments. Even with special documentation, there`s a chance that configurations might also additionally range among deployments, main to surprising conduct and problems in troubleshooting. It require considerable time and effort, in particular while deploying complicated infrastructure or making adjustments throughout a couple of environments. This can sluggish down improvement cycles and avert agility. As your infrastructure grows, guide deployment strategies end up an increasing number of tough to manipulate and scale. It may be hard to make certain consistency and reliability throughout a big and dynamic infrastructure manually. Manual deployments generally lack automation, ensuing in repetitive, error-susceptible obligations for infrastructure provisioning, configuration, and updates. This limits performance and will increase the chance of inconsistencies. Without computerized strategies and special logs, it could be hard to keep an correct audit path of infrastructure adjustments. This can pose demanding situations for compliance necessities and auditing purposes. Overall, guide deployments of cloud infrastructure are much less efficient, extra error-susceptible, and tougher to manipulate in comparison to computerized processes the usage of equipment like Terraform, Jenkins, or different infrastructure as code solutions.

There are various benefits to deploying AWS resources using Terraform and Jenkins:  
  
**Infrastructure as Code (IaC):** Terraform makes it possible to define infrastructure as code, guaranteeing consistency and repeatability.  
  
**Automation:** Jenkins triggers infrastructure changes based on events such as code commits, automating deployment operations.  
  
**Version Control:** Version control solutions enable the tracking of changes and collaboration by storing Terraform configurations.  
  
**Reliability:** Automated deployments provide consistent and dependable infrastructure configurations by minimizing human error.  
  
**Scalability:** Jenkins makes infrastructure scaling easier by managing deployments across several settings.  
  
**Compliance and Auditing:** An audit trail of infrastructure modifications is provided by combining Terraform and Jenkins, which is crucial for compliance and auditing needs.

GitHub is a web-based software development project hosting platform and service. Git is a distributed version control system that is mainly used for version control. Developers may collaborate on projects, manage code repositories, and keep track of changes with GitHub.

Jenkins is an open source automation server. It helps automate the parts of software development related to building, testing, and deploying, facilitating continuous integration, and continuous delivery.

Terraform is an open-source Infrastructure as Code (IaC) tool developed by HashiCorp. It allows users to define and provision infrastructure resources using a declarative configuration language. With Terraform, you can manage various cloud providers, including AWS, Azure, Google Cloud, and others, as well as on-premises infrastructure and services. Terraform enables infrastructure automation, version control, and consistency, making it easier to manage complex deployments and scale infrastructure as needed.

**Architecture:**

![](https://miro.medium.com/v2/resize:fit:875/1*EK-jfFIdcr35RMLRF2fIeg.png)

**Prerequisites:**

a. one t3.medium EC2 instance created using Linux 2 AMI with below Software installed.

i. **Git:**

- yum install git -y

ii. **Jenkins:**

- sudo wget -O /etc/yum.repos.d/jenkins.repo [https://pkg.jenkins.io/redhat-stable/jenkins.repo](https://pkg.jenkins.io/redhat-stable/jenkins.repo)

- sudo rpm — — import [https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key](https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key)

- amazon-linux-extras install java-openjdk11 -y

- yum install jenkins -y

- systemctl enable Jenkins

- systemctl start Jenkins

- systemctl status Jenkins

- systemctl start Jenkins

- systemctl status Jenkins

- cat /var/lib/jenkins/secrets/initialAdminPassword (to get Jenkins password)

**iii.** **terraform:**

· wget [https://releases.hashicorp.com/terraform/1.5.1/terraform_1.5.1_linux_amd64.zip](https://releases.hashicorp.com/terraform/1.5.1/terraform_1.5.1_linux_amd64.zip)

· unzip terraform_1.5.1_linux_amd64.zip

· sudo mv terraform /usr/bin/

· terraform –version

b. Create inbound rule with port 8080 on EC2 Security Group.

c. Github account and repo created with source code.

You can also refer below github repo for source code used in this Blog.

[

## GitHub - Vaishu-psv/terraform-1

### Contribute to Vaishu-psv/terraform-1 development by creating an account on GitHub.

github.com



](https://github.com/Vaishu-psv/terraform-1.git?source=post_page-----3ee596d06aea--------------------------------)

![](https://miro.medium.com/v2/resize:fit:875/1*mGtN-8bpKOCEuC3VLHjQxw.png)

d. Create a iam role similar to below snapshot and attach it EC2 instance which we created as part of Prerequisites.

![](https://miro.medium.com/v2/resize:fit:875/1*8GBd-U132cgotPB5sUyOCg.png)

**Steps:**

1. Login to Jenkins console ([http://ec2-public-ip:8080/login](http://ec2-public-ip:8080/login)).

![](https://miro.medium.com/v2/resize:fit:875/1*eRtPFFB3DCFyD1NGDLnoNA.png)

2. Select Install suggested plugin and it will start installing suggested plugin.

![](https://miro.medium.com/v2/resize:fit:875/1*pyBJgXcEEBRP6iPeis8tqQ.png)

3. Click on New Item.

![](https://miro.medium.com/v2/resize:fit:875/1*UC_Fk5mQRGLVLrGtXxifmg.png)

4. Enter item name and item type as “Pipeline” and Click on OK.

![](https://miro.medium.com/v2/resize:fit:875/1*59JevzRZder6jYmiKQ2gVw.png)

5. In Configuration->Pipeline, Select Definition as “Pipeline script from scm”, SCM as “Git”, Repository Url as “Github_URL”, Branch Specifier as “*/main” and Click on Save.

![](https://miro.medium.com/v2/resize:fit:875/1*aAr0j1fmC00BBgZGvIrPHA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*bzrVwLzoMrJMuSvFeXE21A.png)

![](https://miro.medium.com/v2/resize:fit:875/1*_JD8X78Y3Q-p4tImShhutg.png)

6. In left panel, Click on Build Now.

![](https://miro.medium.com/v2/resize:fit:875/1*FVwMPhnGoH-jyL7HnmmnpA.png)

7. In Build History, click on #1, Select console output to see Output. It will first clone the git repo, downloads 2 files (main.tf, Jenkinsfile) from GitHub repo, then start execute pipeline according to jenkinsfile (terraform init, plan,apply) Once all steps are executed, we can see Success message at end.

![](https://miro.medium.com/v2/resize:fit:875/1*hXtpq1THk6pVxOl9innxVQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*AFpDMwN5zJqdyQ3Spk-kLQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*q5CP-JkaT5-L5BXzgDzbqw.png)

8. Once this pipeline is executed successfully, we can see new ec2 instance created in AWS console.

![](https://miro.medium.com/v2/resize:fit:875/1*ly5JaqLhHgANu9V1wlk3ZQ.png)