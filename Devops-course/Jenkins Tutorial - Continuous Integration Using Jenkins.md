
![[Pasted image 20240511120045.png]]

Continuous Integration is an integral part of DevOps, and Jenkins is the most famous Continuous Integration tool. In this article, I will focus on Jenkins architecture and Jenkins build a pipeline along with that I will show you how to create a build in Jenkins.

Before we proceed with the article, few key takeaways about Jenkins are as follows:

- Jenkins is used to integrate all DevOps stages with the help of plugins.
- Commonly used Jenkins plugins are Git, Amazon EC2, Maven 2 project, HTML publisher, etc.
- Jenkins has well over 1000 plugins and 147,000 active installations along with over 1 million users around the world.
- With Continuous Integration, every change made in the source code is built. It performs other functions as well, that depends on the tool used for Continuous Integration.
- Nokia shifted from Nightly build to Continuous Integration.
- Process before Continuous Integration had many flaws. As a result, not only the software delivery was slow but the quality of the software was also not up to the mark. Developers also had a tough time locating and fixing bugs.
- Continuous Integration with Jenkins overcame these shortcomings by continuously triggering a build and test for every change made in the source code.

Now is the correct time to understand Jenkins architecture.

# Jenkins Architecture

You can refer to the below diagram to understand Jenkins standalone Architecture.

![](https://miro.medium.com/v2/resize:fit:1050/1*37ZlHNqrQ4Zfrshy23_4Rw.png)

Jenkins Standalone Architecture - Jenkins Tutorial

This single Jenkins server was not enough to meet certain requirements like:

- Sometimes you might need several different environments to test your builds. This cannot be done by a single Jenkins server.
- If larger and heavier projects get built on a regular basis then a single Jenkins server cannot simply handle the entire load.

To address the above-stated needs, Jenkins distributed architecture was introduced.

# Jenkins Distributed Architecture

Jenkins uses a Master-Slave architecture to manage distributed builds. In this architecture, Master and Slave communicate through TCP/IP protocol.

**Jenkins Master**

Your main Jenkins server is the Master. The Master’s job is to handle:

- Scheduling build jobs.
- Dispatching builds to the slaves for the actual execution.
- Monitor the slaves (possibly taking them online and offline as required).
- Recording and presenting the build results.
- A Master instance of Jenkins can also execute build jobs directly.

# Jenkins Slave

A Slave is a Java executable that runs on a remote machine. Following are the characteristics of Jenkins Slaves:

- It hears requests from the Jenkins Master instance.
- ==Slaves can run on a variety of operating systems.==
- The job of a Slave is to do as they are told to, which involves executing build jobs dispatched by the Master.
- You can configure a project to always run on a particular Slave machine or a particular type of Slave machine, or simply let Jenkins pick the next available Slave.

The diagram below is self-explanatory. It consists of a Jenkins Master which is managing three Jenkins Slave.

![](https://miro.medium.com/v2/resize:fit:1050/1*RCToSje_f9hd7LjpHrQQGg.png)

Jenkins Master-Slave - Jenkins Tutorial

Now let us look at an example in which Jenkins is used for testing in different environments like Ubuntu, MAC, Windows, etc.

The diagram below represents the same:

![](https://miro.medium.com/v2/resize:fit:1050/1*MhcTCvUslrhtOdkLWXPtMw.png)

Distributed Testing - Jenkins Tutorial

The following functions are performed in the above image:

- Jenkins checks the Git repository at periodic intervals for any changes made in the source code.
- Each builds requires a different testing environment which is not possible for a single Jenkins server. In order to perform testing in different environments, Jenkins uses various Slaves as shown in the diagram.
- Jenkins Master requests these Slaves to perform testing and to generate test reports.

# Jenkins Build Pipeline

It is used to know which task Jenkins is currently executing. Often several different changes are made by several developers at once, so it is useful to know which change is getting tested or which change is sitting in the queue or which build is broken. This is where pipeline comes into the picture. The _Jenkins Pipeline_ gives you an overview of where tests are up to. In build pipeline, the build as a whole is broken down into sections, such as the unit test, acceptance test, packaging, reporting, and deployment phases. The pipeline phases can be executed in series or parallel, and if one phase is successful, it automatically moves on to the next phase (hence the relevance of the name “pipeline”). The below image shows how a multiple build Pipeline looks like.

![](https://miro.medium.com/v2/resize:fit:1050/1*26DnaGx9kB1HY9NtIl8u6Q.png)

Jenkins Build Pipeline - Jenkins Tutorial

Hope you have understood the theoretical concepts. Now, let’s have some fun with hands-on.

I will create a new job in Jenkins, it is a **Freestyle Project**. However, there are 3 more options available. Let us look at the types of build jobs available in Jenkins.

## **Freestyle Project:**

Freestyle build jobs are general-purpose build jobs, which provides maximum flexibility. The freestyle build job is the most flexible and configurable option and can be used for any type of project. It is relatively straightforward to set up, and many of the options we configure here also appear in other build jobs.

## **Multiconfiguration Job:**

The “multiconfiguration project” (also referred to as a “matrix project”) allows you to run the same build job on different environments. It is used for testing an application in different environments, with different databases, or even on different build machines.

## **Monitor an External Job:**

The “Monitor an external job” build job lets you keep an eye on non-interactive processes, such as cron jobs.

## **Maven Project:**

The “maven2/3 project” is a build job specially adapted to Maven projects. Jenkins understands Maven pom files and project structures and can use the information gleaned from the pom file to reduce the work you need to do to set up your project.

**Step 1:** From the Jenkins interface home, select **New Item.**

![](https://miro.medium.com/v2/resize:fit:1050/1*Hlt1toore9_TJOIMZZWY0w.png)

**Step 2:** Enter a name and select **Freestyle project**.

![](https://miro.medium.com/v2/resize:fit:1050/1*Ol_OKuB9-ahm1dnUzWfPIQ.png)

**Step 3:** This next page is where you specify the job configuration. As you’ll quickly observe, there are a number of settings available when you create a new project. On this configuration page, you also have the option to **Add build step** to perform extra actions like running scripts. I will execute a shell script.

![](https://miro.medium.com/v2/resize:fit:510/1*mGhiiSPHaa7BV9137WIlsQ.png)

This will provide you with a text box in which you can add whatever commands you need. You can use scripts to run various tasks like server maintenance, version control, reading system settings, etc. I will use this section to run a simple script.

![](https://miro.medium.com/v2/resize:fit:1050/1*26tP4qkaP6mcl4Yt9uyP6g.png)

**Step 4:** Save the project, and you’ll be taken to a project overview page. Here you can see information about the project, including its built history.

![](https://miro.medium.com/v2/resize:fit:1050/1*I2a2a8mZ-ci-P2AetkGY5A.png)

**Step 5:** Click **Build Now** on the left-hand side to start the build.

![](https://miro.medium.com/v2/resize:fit:1050/1*qEKUwYbUJUSTsxXfx8SohQ.png)

**Step 6:** To see more information, click on that build in the build history area, whereupon you’ll be taken to a page with an overview of the build information.

![](https://miro.medium.com/v2/resize:fit:1050/1*IiGRSPHhBP0CBQyttiHIqQ.png)

**Step 7:** The **Console Output** link on this page is especially useful for examining the results of the job in detail.

![](https://miro.medium.com/v2/resize:fit:1050/1*iEQoBcmdblL5VlPlSL0f3g.png)

**Step 8:** If you go back to Jenkins home, you’ll see an overview of all projects and their information, including status.

![](https://miro.medium.com/v2/resize:fit:1050/1*EKnfPiCU7dMPr0BenY0EBQ.png)

Status of the build is indicated in two ways, by a weather icon, and by a colored ball. The weather icon is particularly helpful as it shows you a record of multiple builds in one image.

As you can see in the above image, the _sun_ represents that all of my builds were successful. The _color of the ball_ gives us the status of that particular build, in the above image the color of the ball is blue which means that this particular build was successful.