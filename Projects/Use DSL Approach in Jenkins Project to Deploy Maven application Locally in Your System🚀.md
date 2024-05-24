
# Project Description 📄

This Jenkins project utilizes the DSL (Domain-Specific Language) approach to automate various tasks in the Jenkins CI/CD pipeline. It is designed to streamline the software development process by automatically retrieving code from a specified GitHub repository, building a JAR file using Maven, testing the code, deploying the JAR file locally, archiving build artifacts, storing JUnit test results, and sending email notifications in the event of job failures. GitHub webhook integration is also configured to trigger the job automatically upon code changes.

# Workflow Diagram 📊

![](https://miro.medium.com/v2/resize:fit:1400/0*Zi-Zp5PpPtBNHN9C)

# Why Use DSL? 🤔

DSL is a programming language that is designed to perform a specific set of tasks. It is a high-level language that is easy to read and understand. DSL is used to automate various tasks in the CI/CD pipeline, such as code retrieval, building, testing, and deployment. It is also used to archive build artifacts, store test results, and send email notifications in case of job failures. DSL is a powerful tool that can be used to enhance the automation and efficiency of the software development process. **In simple words to describe, DSL is used for Configure Jenkins Job automatically.**

# Best Practices 📝

- Since DevOps involve many automation, Using DSL is consider as one of the Best Practice.

# Tools Used 🛠️

- Jenkins
- GitHub
- Maven

# Steps 🏁

## Step-1: Install Jenkins on Virtual Machine(Any Linux Distributions Preferred):

## Prerequisites

- Linux OS (Ubuntu Preferred)

## Steps

- Install Java

sudo apt-get update  
sudo apt-get install fontconfig openjdk-11-jre

- Add Jenkins Repository

sudo apt-get update

curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \  
    /usr/share/keyrings/jenkins-keyring.asc > /dev/null  
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \  
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \  
    /etc/apt/sources.list.d/jenkins.list > /dev/null

- Install Jenkins

sudo apt-get update  
sudo apt-get install jenkins

- Enable Jenkins

sudo systemctl enable jenkins

- Start Jenkins

sudo systemctl start jenkins

- Check Jenkins Status

sudo systemctl status jenkins

- Open Jenkins in Browser

http://your-machine-ip:8080

- Unlock Jenkins

sudo cat /var/lib/jenkins/secrets/initialAdminPassword

- Click on “Install Suggested Plugins”
- Create Admin User
- Save and Finish
- Start Using Jenkins

## Step-2: Install Plugins

## Plugins to be installed

1. **Maven Integration**

- Maven Integration: Configured to build the Maven project and generate the JAR file.

**2. Job DSL**

- Job DSL: Configured to create a DSL seed job to generate the Jenkins job using the DSL approach.

**3. Mailer**

- Mailer: Configured to send email notifications in case of job failures.

## To Install Plugins Follow the Steps:

![](https://miro.medium.com/v2/resize:fit:1400/0*Z6GSywbZY1PnUhLP)

![](https://miro.medium.com/v2/resize:fit:1400/0*MeK33ZHGg4PyzvG8)

![](https://miro.medium.com/v2/resize:fit:1400/0*hJqExIkTAxm_j0jN)

After the above steps , Jenkins will automatically restart and you will be redirected to the Jenkins Dashboard.

## Step-3: Configuring Seed Job:

- Click on “New Item.”
- Enter the name of the job.
- Select “Freestyle project.”
- Click on “OK.”
- Click on Configure.
- Select Source Code Management as “Git.”
- You can provide the link to my repository if you’d like, or you can create your own repository by forking mine. Just be sure to update the email address. I will provide the repository link at the end of this blog.
- In case of your Maven Job build fail you will receive mail, **Check your mail in spam folders**. Not that it’s for Maven job not for DSL Seed Job.

![](https://miro.medium.com/v2/resize:fit:1400/0*YmdK5QSsGHKlWA1P)

- Click on Build Step and select “Process Job DSLs.”

![](https://miro.medium.com/v2/resize:fit:1400/0*wlfWKa0QMsAWadUS)

![](https://miro.medium.com/v2/resize:fit:1400/1*RPXGUWkaUaD0nKVXSQ75WA.png)

## Step-4: Maven Job Build and Test

- After you have set up the Seed job , you can now Click on “Build Now” to generate the Maven Job.
- The Maven will be generated as per the DSL Script.

## Step-5: Build the Maven Job

- After your Maven Job is generated , you can now build the job.
- Click on the Generated Maven Job
- Click on “Build Now” to build the job.
- The job will be built as per the DSL Script.
- You can also check the console output of the job.

![](https://miro.medium.com/v2/resize:fit:1400/0*NMtRR2NUOGpg8hlk)

![](https://miro.medium.com/v2/resize:fit:1400/1*_7E8N13geCkahBFT0oHdhQ.png)

## Step-6: Steps for configuring webhook for the pipeline

- As we already given in the Jenkins job configuration to trigger the Maven job when there is any changes in the GitHub repository, we need to configure the webhook in the GitHub repository.(As per DSl script)
- But We need to configure for Seed job Manually. For that we need to go to Jenkins and configure the webhook for the seed job.

1. Go to the Jenkins server
2. Click on the Seed job in the dashboard
3. Click on ‘Configure’ in the left side of the dashboard
4. Scroll down to the ‘Build Triggers’ section
5. Select ‘GitHub hook trigger for GITScm polling’
6. Click ‘Save’

- Now , Repeat the below steps for the two repositories(The repositories which contains code for both jobs if you kept the code for both jobs in same repository if need to do that on that particular repository) which you have created in the GitHub.
- Go to the GitHub repository
- Click on ‘Settings’ in the right side of the repository
- Click on ‘Webhooks’ in the left side of the repository
- Click on ‘Add webhook’
- Give the Payload URL as

http://<Jenkins-IP>:8080/github-webhook/

- Give the Content type as ‘application/json’
- Give the Secret as ‘mysecret’
- Select ‘Just the push event’ in the ‘Which events would you like to trigger this webhook?’ section
- Click ‘Add webhook’
- Now if you make any changes in the GitHub repository the pipeline will automatically start building the project.

**GitHub Repository** : [https://github.com/mathesh-me/dsl-approach-jenkins-project](https://github.com/mathesh-me/dsl-approach-jenkins-project)

If you like this project, give it a go! If you enjoy it, 👏clap for it, and follow me for more DevOps and Cloud projects