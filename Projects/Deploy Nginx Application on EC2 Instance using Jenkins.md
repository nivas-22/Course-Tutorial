
GitHub is a web-based software development project hosting platform and service. Git is a distributed version control system that is mainly used for version control. Developers may collaborate on projects, manage code repositories, and keep track of changes with GitHub.

Docker is an open source platform that enables developers to build, deploy, run, update and manage containerized applications.

Docker Images is a read-only template containing a set of instructions for creating a container that can run on the Docker platform.

Docker container encapsulate the application, its dependencies, and the runtime environment in a self-sufficient package.

Jenkins is an open source automation server. It helps automate the parts of software development related to building, testing, and deploying, facilitating continuous integration, and continuous delivery.

In this blog, we are going to deploy docker container on EC2 instance using Jenkins.

**Architecture:**

![](https://miro.medium.com/v2/resize:fit:875/1*AcWJxyzlFEWXqw4G0B5TNg.png)

**Prerequisites:**

a. one EC2 instance created using Linux 2 AMI with below Software installed.

**i.** **Docker:**

- yum install docker -y
- sudo systemctl start docker
- sudo systemctl status docker

![](https://miro.medium.com/v2/resize:fit:875/1*mrfAWCTs7Vl0-TRfAykmeg.png)

**ii.** **Git:**

- yum install git -y

**iii.** **Jenkins:**

- sudo wget -O /etc/yum.repos.d/jenkins.repo [https://pkg.jenkins.io/redhat-stable/jenkins.repo](https://pkg.jenkins.io/redhat-stable/jenkins.repo)
- sudo rpm — — import [https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key](https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key)
- amazon-linux-extras install java-openjdk11 -y
- yum install jenkins -y
- systemctl enable jenkins
- systemctl start jenkins
- systemctl status jenkins
- systemctl start jenkins
- systemctl status Jenkins
- cat /var/lib/jenkins/secrets/initialAdminPassword (to get Jenkins password)

![](https://miro.medium.com/v2/resize:fit:875/1*Kx_Uln7t0dSWftw2w5rWgA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*hT90zFMBHY7kNxfn7DEw_A.png)

![](https://miro.medium.com/v2/resize:fit:875/1*fCG1QGo0omObXN0Z6w10CA.png)

b. Create inbound rule with port 8080 and 8081 on EC2 Security Group.

c. Github account and repo created with source code.

You can also refer below github repo for source code used in this Blog.

[

## GitHub - Vaishu-psv/psv-restaurant-1

### Contribute to Vaishu-psv/psv-restaurant-1 development by creating an account on GitHub.

github.com



](https://github.com/Vaishu-psv/psv-restaurant-1?source=post_page-----3402322b508b--------------------------------)

![](https://miro.medium.com/v2/resize:fit:875/1*jfEpnFEAfc3IVGWBVSFNfg.png)

**Steps:**

1. Login to Jenkins console ([http://ec2-public-ip:8080/login](http://ec2-public-ip:8080/login)).

![](https://miro.medium.com/v2/resize:fit:875/1*2YfnT6xAE1VicZ6fH0JU5w.png)

2. Select Install suggested plugin and it will start installing suggested plugin.

![](https://miro.medium.com/v2/resize:fit:875/1*xFUn0viIzo9vSIQ3aQlghg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*lZvDQuvKUdyQTqbtmk1bUA.png)

3. Click on New Item.

![](https://miro.medium.com/v2/resize:fit:875/1*83iskQv_qMTLiNWLjXS1Yw.png)

4. Enter item name and item type as “Freestyle project”, Click on OK.

![](https://miro.medium.com/v2/resize:fit:875/1*_Hdja5zua-PbxSbEtDd9FA.png)

5. In Configure -> Source Code Management, Select Git and provide Repository URL (GitHub repo url) and Branch Specifier as “*/main”.

![](https://miro.medium.com/v2/resize:fit:875/1*CEmTDW4eDVQUY_V6433OSg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*ntGVMxVV8_bJLr7Eaz6y9w.png)

6. In Build Steps, Select Execute Shell and provide below commands to clone GitHub repo, download files from repo, build new docker image and container.

- git clone [https://github.com/Vaishu-psv/psv-restaurant-1.git](https://github.com/Vaishu-psv/psv-restaurant-1.git)
- cd psv-restaurant-1
- docker build -t custom-nginx .
- docker run -d — name psv-res -p 8081:80 custom-nginx

![](https://miro.medium.com/v2/resize:fit:875/1*o7V3cDUWZsq62rQRgtZ0tQ.png)

7. Click on Save and Apply.

![](https://miro.medium.com/v2/resize:fit:685/1*ylbzW5juMtPPb_9yPqjyeQ.png)

8. In Build History, click on #1 or #2, Select console output to see Output. It will first clone the git repo, downloads 3 files (index.html, food4png.png, Dockerfile) from GitHub repo, then build new image using Dockerfile and with new Docker image, it will create Docker container. Once all steps are executed, we can see Success message at end.

![](https://miro.medium.com/v2/resize:fit:875/1*9AoK4oPlSrH_0rIsf7xYgw.png)

![](https://miro.medium.com/v2/resize:fit:875/1*hICn5Y63VarE-2Xj3OlIgw.png)

9. We have deployed Nginx Docker container on port 8081 for a website. To test it, we can use [http://ec2-public-ip:8081](http://ec2-public-ip:8081)

![](https://miro.medium.com/v2/resize:fit:875/1*HYFu2vNr9pHM_ayQFCVgZw.png)

**Conclusion:**

In this post, we have deployed Nginx Docker container using Jenkins on EC2.