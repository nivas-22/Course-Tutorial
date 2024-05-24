![](https://miro.medium.com/v2/resize:fit:866/1*zVtromgUIigUd5QtqfiN1g.png)

AWS Elastic Beanstalk 

Cloud Computing is no longer at its primal stages. It is now well established and is serving as an innovative platform, allowing companies to implement applications that would be impossible to deliver on traditional infrastructure. This success has been accompanied by an exponential increase in _cloud computing services_, PaaS being one of them. Amazon has launched its own service that follows the PaaS model, which is **AWS** **Elastic Beanstalk!**

Let’s take a look at the topics covered in this AWS Beanstalk article:

1. What is Amazon Elastic Beanstalk?
2. Benefits of AWS Elastic Beanstalk
3. AWS Elastic Beanstalk Components
4. AWS Elastic Beanstalk Architecture
5. Demo - Deploy an application on Beanstalk

# What is Amazon Elastic Beanstalk?

![](https://miro.medium.com/v2/resize:fit:149/1*2Y5U-vWxuUqhSVqEkhOAbw.png)

Cloud Computing is reshaping the entire application development process. A number of cloud vendors, including Amazon Web Services and Microsoft Azure, offer development tools to help make the process more simple and secure. AWS Elastic Beanstalk is one such development tool implemented based on PaaS model.

_AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS._

With AWS Elastic Beanstalk, a developer can deploy an application without provisioning the underlying infrastructure while maintaining high availability.

But why choose Elastic Beanstalk when we already have many other platforms? So, Let’s discuss the benefits of Elastic Beanstalk.

# Benefits of AWS Elastic Beanstalk

Below are some benefits that AWS Elastic Beanstalk offers over other PaaS services

**Offers Quicker Deployment:**

![](https://miro.medium.com/v2/resize:fit:80/1*gC0oPov8mTCEP_KIwO_ELg.png)

Elastic Beanstalk offers developers the fastest and simplest way to deploy their application. Within minutes, the application will be ready to use without users having to deal with the underlying infrastructure or resource configuration.

**Supports Multi-Tenant Architecture:**

![](https://miro.medium.com/v2/resize:fit:80/1*TeqoCcRSkX1XmcbNmayicA.png)

AWS Elastic Beanstalk makes it possible for users to share their applications across different devices with high scalability and security. It provides a detailed report of application usage and user profiles.

**Simplifies Operations:**

![](https://miro.medium.com/v2/resize:fit:188/1*MemK2a4fAzNy0WHbyFJDag.png)

Beanstalk provisions and operates the infrastructure and manages the application stack. Developers have to just focus on developing code for their application rather than spending time on managing and configuring servers, databases, firewalls, and networks.

**Offers Complete Resource Control:**

![](https://miro.medium.com/v2/resize:fit:173/1*Jj764nP4qOEZdKRNiSwPcg.png)

Beanstalk gives developers the freedom to select the AWS resources, like _EC2 instance_ type, that are optimal for their application. It allows developers to retain full control over AWS resources and access them at any time.

Now that we have solid reasons to believe why AWS Elastic Beanstalk is preferred by developers, let’s have a look at its fundamental concepts.

# AWS Elastic Beanstalk Components

There are certain key concepts which you will come across frequently when you deploy an application on Beanstalk. Let us have look at those concepts:

# Application:

- An application in Elastic Beanstalk is conceptually similar to a folder
- An application is a collection of components including **_environments, versions_** and **_environment configuration_**

# Application Version:

- An application version refers to a specific, labeled iteration of deployable code for a web application.
- An application version points to an Amazon S3 object that contains the deployable code such as a Java WAR file

# Environment:

- Environments within the Elastic Beanstalk Application is where the current version of the application will be active
- Each environment runs only a single application version at a time. But it is possible to run same or different versions of an application in many environments at the same time

# Environment Tier:

Based on requirement beanstalk offers two different Environment tiers: Web Server Environment, Worker Environment

- Web Server Environment: Handles HTTP requests from clients
- Worker Environment: Processes background tasks which are resource consuming and time intensive

Here is an illustration to show how Application, Application version and Environments relate to each other:

![](https://miro.medium.com/v2/resize:fit:660/1*beLI5iHJ-C_9ciYPdFL42A.png)

And here is how Beanstalk Environment using default container type looks like:

![](https://miro.medium.com/v2/resize:fit:458/1*C1QKQExQEgNr28zxliyP0g.png)

Now that you know about different key concepts pertaining to Elastic Beanstalk, let understand the architecture of Elastic Beanstalk.

**AWS Elastic Beanstalk Architecture**

Before getting into AWS Elastic Beanstalk architecture, let’s answer the most frequently asked question,

# What is an Elastic Beanstalk Environment?

Environment refers to the current version of the application. When you launch an Environment for your application, Beanstalk asks you to choose among two different Environment Tiers i.e, Web _Server Environment_ or _Worker Environment_. Let’s understand them one by one.

## Web Server Environment

Application version which is installed on the Web Server Environment handles HTTP requests from the client. The following diagram illustrates an example AWS Elastic Beanstalk architecture for a Web Server Environment tier and shows how the components in that type of Environment Tier work together.

**Beanstalk Environment** — The Environment is the heart of the application. When you launch an Environment, Beanstalk assigns various resources that are needed to run the application successfully.

**Elastic Load Balancer** — When the application receives multiple requests from a client, Amazon Route53 forwards these requests to the Elastic Load Balancer. The load balancer distributes the requests among EC2 instances of Auto Scaling Group.

**Auto Scaling Group** — Auto Scaling Group automatically starts additional Amazon EC2 instances to accommodate increasing load on your application. If the load on your application decreases, Amazon EC2 Auto Scaling stops instances, but always leaves at least one instance running.

**Host Manager** — It is a software component which runs on every EC2 instance that has been assigned to your application. The host manager is responsible for various things like

- Generating and monitoring application log files
- Generating instance level events
- Monitoring application server

**Security Groups** — Security Group is like a firewall for your instance. Elastic Beanstalk has a default security group, which allows the client to access the application using HTTP Port 80. It also provides you with an option where you can define security groups to the database server as well. The below image summarizes what we have learned about Web Server Environment.

![](https://miro.medium.com/v2/resize:fit:579/1*uQSZ5qpD-8MPbBKL29MjdA.png)

So that’s all about Web Server Environment. But what if the application version installed on Web Server Tier keeps denying multiple requests because it has encountered time intensive and resource consuming tasks while handling a request? Well, this is where Worker Tier comes into the picture.

## Worker Environment

A worker is a separate background process that assists Web Server Tier by handling resource-intensive or time-intensive operations. In addition, it also emails notifications, generates reports and cleans up databases. This makes it possible for the application to remain responsive and handle multiple requests.

That’s great, but how does Worker process know which tasks to handle and when? How do these two Environment tiers communicate? For that, we use a message queuing service by AWS call Amazon Simple Queue Service (SQS). The image below gives you a rough idea of how the worker process receives and handles background tasks.

The workflow of the worker process is fairly simple. When you launch a Worker Environment tier, Elastic Beanstalk installs a daemon on each EC2 instance in the Auto Scaling group. The daemon pulls requests sent from an Amazon SQS queue. Based on the queue’s priority, SQS will send the message via a `POST`request to the HTTP Path of the Worker Environment. The worker on receiving the message executes the tasks and sends an HTTP response once the operation is done. SQS on receiving response message deletes the message in the queue. If it fails to receive a response, it will continuously retry sending the messages.

![](https://miro.medium.com/v2/resize:fit:660/1*iMauFnbjBcZcVwgKmOlo8A.png)

Now that we have seen Elastic Beanstalk theoretically, in the remainder of this blog we will see how to deploy an application on Elastic Beanstalk.

# Deploy an Application on Elastic Beanstalk

Deploying an application on Elastic Beanstalk is a fairly simple process. Let’s see how to deploy an application stepwise.

**Step 1:** On the Elastic Beanstalk console click on _Create New Application_ option. A dialog box appears where you can give a name and appropriate description for your application.

![](https://miro.medium.com/v2/resize:fit:875/1*1IITbPGrIZkEP-ZvWtWOTw.png)

**Step 2:** Now that the application folder has been created, you can click on the _Actions tab_ and select _Create Environment_ option. Beanstalk provides you with an option where you can create multiple Environments for your application.

![](https://miro.medium.com/v2/resize:fit:875/1*bIII4esmlLZ_6qjkoWbwFw.png)

**Step 3:** Choose among two different Environment Tier options. Choose Web Server Environment if you want your application to handle HTTP requests or choose Worker Environment to handle background tasks.

![](https://miro.medium.com/v2/resize:fit:875/1*j2OwAmK5UogBJGLNWP9yZw.png)

**Step 4:** Another dialog appears, where you need to provide a domain name and description for your application.

![](https://miro.medium.com/v2/resize:fit:875/1*iiaSt2mI5uSykXMjU-V3oQ.png)

**Step 5:** Choose a platform of your choice for your application. Elastic Beanstalk will provide you with multiple options. You can choose a sample application provided by Beanstalk, or upload a file which has code for your application.

![](https://miro.medium.com/v2/resize:fit:875/1*FqkKEf-vztoA1E5V4yEwaA.png)

Beanstalk will take a few minutes to launch an Environment. Once the Environment is launched, on the navigation pane you can see multiple options where you can change the configuration of your application, view log files, and events. Since you’re already on Environment page, try exploring different features that Beanstalk offers.

![](https://miro.medium.com/v2/resize:fit:875/1*EvtAihVLyt0jEJh0J9mxZQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*FNhm4hSQB5A5i3QTF1IE_Q.png)

**Step 6:** On the top right corner, you will find the URL of your application version. Click on that URL. You will be taken to a page which will confirm that you have successfully launched your application on Elastic Beanstalk.

![](https://miro.medium.com/v2/resize:fit:875/1*SNzlaZLIoiMfIT9kXwj-iA.png)

**Congratulations!** You have successfully deployed an application on Elastic Beanstalk Platform