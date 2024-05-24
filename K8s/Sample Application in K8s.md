
It is common knowledge that **_Amazon Web Services(AWS)_** is a well-known provider of cloud services, while Kubernetes is quickly becoming the standard way to manage application containers in the production environment. While many developers would gladly use **_Kubernetes_**, the time-consuming cluster management process can be a turnoff. As a solution, developers can use Amazon Elastic Container Service for Kubernetes (Amazon EKS), which allows them to create Kubernetes clusters in the cloud very quickly and easily.

Let’s take a look at the topics covered in this article:

1. Amazon EKS & its Benefits
2. How does Amazon EKS work?
3. Build a Kubernetes app with Amazon EKS

Let’s get started!

# Amazon EKS

Though containers have been around since the early days of Linux, Docker introduced the modern version of this technology. Kubernetes is an open source software that allows you to deploy and manage containerized applications at scale. It also provides portability and extensibility, enabling you to scale containers seamlessly. But, the downside of Kubernetes is that it takes a lot of time to deploy a cluster with master and worker nodes. A turn around for this is Amazon EKS.

# Amazon Elastic Container Service for Kubernetes(Amazon EKS)

==Amazon Elastic Container Service for Kubernetes (Amazon EKS) is a managed service that makes it easy for users to run Kubernetes on AWS without needing to stand up or maintain your own Kubernetes control plane.== Since Amazon EKS is a managed service it handles tasks such as provisioning, upgrades, and patching.

Definition aside, let’s take a look at the benefits of Amazon EKS:

- Amazon EKS runs the Kubernetes management infrastructure across multiple AWS Availability Zones, thereby freeing users from maintaining Kubernetes control plane.
- Infrastructure running on Amazon EKS is secure by default by setting up a secure and encrypted communication channel between worker nodes & Kubernetes endpoint.
- AWS actively works with the Kubernetes community and makes contributions to the Kubernetes code base.
- Applications managed by Amazon EKS are fully compatible with applications managed by any standard Kubernetes environment.

So, the above reasons are convincing enough to start using Amazon EKS. Now, let’s take a look at how Amazon EKS actually works.

# How does Amazon EKS work?

![](https://miro.medium.com/v2/resize:fit:1400/1*DNdvPQsTd9EM3IFlYfFVrg.png)

Representation of Workflow of Amazon EKS - Amazon EKS

Getting started with Amazon EKS is easy fairly easy:

1. First, create an Amazon EKS cluster in the AWS Management Console or with the AWS CLI or one of the AWS SDKs
2. Then, launch worker nodes and enable them to join the Amazon EKS cluster which you created earlier
3. When your cluster is ready, you can configure your favorite Kubernetes tools to communicate with your cluster
4. Deploy and manage applications on your Amazon EKS cluster the same way that you would with any other Kubernetes environment

Now, let’s see how to deploy a containerized application onto a Kubernetes cluster using Amazon Elastic Container Service for Kubernetes.

# Deploy a Kubernetes Application with Amazon EKS

**Demo:** In this demo, we will see how to launch a simple nginx application on Kubernetes cluster using Amazon EKS. Here are the steps you will follow:

- Create an AWS IAM service role and an AWS VPC
- Create Amazon EKS cluster
- Configure kubectl for Amazon EKS cluster
- Launch and configure Amazon EKS worker nodes
- Launch a simple nginx application
- Cleaning up the application & assigned resources

This section will walk you through these steps in detail.

# Assumptions and Prerequisites

- You should have an AWS account with an active subscription and be able to log in using AWS IAM account credentials. If you don’t have either of these create an AWS account & create an IAM user in your AWS account.
- You should install the latest version of the AWS command-line interface (CLI), to a location in your system path. In case you haven’t, install it using these instructions.

# Step 1: Create an AWS IAM service role and a VPC

The first step is to create an IAM role that Kubernetes can assume to create AWS resources. To do this:

- Navigate to AWS IAM Console & in “**Roles**” section, click the “**Create role**” button
- Select “**AWS service**” as the type of entity and “**EKS**” as the service
- Enter a name for the service role and click “**Create role**” to create the role

![](https://miro.medium.com/v2/resize:fit:1400/1*T8fJMnm8AjiKU-0h2eoL1w.png)

Amazon EKS also requires a Virtual Private Cloud (VPC) to deploy the cluster. To create this VPC:

- Navigate to the _AWS CloudFormation_ console and click on “**Create Stack**”
- On the “**Select Template**” page, select the option to “**Specify an Amazon S3 template URL**” and enter the URL
- After specifying all the details, review and confirm them. Then click “**Create**” to proceed

![](https://miro.medium.com/v2/resize:fit:1400/1*-kYC_AlZAkjDigaE4wWX4w.png)

# Step 2: Create an Amazon EKS cluster

At this point, you are ready to create a new Amazon EKS cluster. To do this:

- Navigate to the Amazon EKS console and click on “**Create cluster**” button
- Enter details into the EKS cluster creation form such as cluster name, role ARN, VPC, subnets and security groups
- Click “**Create**” to create the Amazon EKS cluster

![](https://miro.medium.com/v2/resize:fit:1400/1*X6PDKkmyySmqveuL-74FJA.png)

# Step 3: Configure kubectl for Amazon EKS cluster

Kubernetes uses a command-line utility called **_Kubectl_** for communicating with Kubernetes cluster. Amazon EKS clusters also require the AWS IAM Authenticator for Kubernetes to allow IAM authentication for your Kubernetes cluster. So, install both of these binaries. Instructions for downloading and setup are in the Amazon EKS documentation.

**Note:** Ensure that you have at least version of the AWS CLI installed and your system’s Python version must be Python 2.7.9 or greater.

Next, you have to create a **_kubeconfig_** file for your cluster with the AWS CLI **update-kubeconfig** command as follows:

- Use the AWS CLI **update-kubeconfig** command to create or update your kubeconfig for your cluster
- Test your configuration

![](https://miro.medium.com/v2/resize:fit:1400/1*Q6IExsNC0tAMkXW9NiCcgA.png)

# Step 4: Launch and configure Amazon EKS worker nodes

**Note:** Wait for your cluster status to show as **ACTIVE**`.` If you launch your worker nodes before the cluster is active, the worker nodes will fail to register with the cluster and you will have to relaunch them.

Once the control plane of your cluster has been activated, the next step is to add nodes to it. To do this:

- Navigate to the AWS CloudFormation console and click on “**Create stack**” option
- On the “**Select Template**” page, select the option to “**Specify an Amazon S3 template URL**” and enter the URL
- On the “**Specify Details**” page, enter details as shown below. Review the details and click on “**Create**”
- Once stack creation is complete, select the stack name in the list of available stacks and select the “**Outputs**” section in the lower left pane. Make a note of Role ARN

![](https://miro.medium.com/v2/resize:fit:1400/1*R-YTwEzn_5l7txdu8qVz4g.png)

Now to enable worker nodes to join Kubernetes cluster follow below steps:

- On your local system, create a file named **_aws-auth-cm.yaml_** and fill it with the content below. Replace the AWS-ARN with the node instance role that you copied from the stack output earlier

![](https://miro.medium.com/v2/resize:fit:1056/1*cSdf4R5u0NdO98tuR3Ojug.png)

- Apply the configuration. This command may take a few minutes to finish.
- Watch the status of your nodes and wait for them to reach the `Ready` state

![](https://miro.medium.com/v2/resize:fit:1400/1*9Qx1ZL3JUjRKcjoOXZy0hA.png)

# Step 5: Launch a simple nginx application

To create an application you need to create a Kubernetes object of type **_Deployment_**_. O_n your local system, create a file named **_nginx.yaml_** and fill it with the content below.

Now, as a backup for application, you also need to create a Kubernetes object of Service type. A Kubernetes Service is an abstraction which defines a logical set of Pods running somewhere in your cluster, that all provide the same functionality as ones which you created earlier. On your local system, create a file named **nginx_.yaml_** and fill it with the content below.

![](https://miro.medium.com/v2/resize:fit:1400/1*HU3ky0qUatvO2O01kvuTRA.png)

- Create the nginx application and nginx service
- List the running services and capture the external IP address & port
- After your external IP address is available, point a web browser to that address at the respective port to view your nginx application

![](https://miro.medium.com/v2/resize:fit:1400/1*Ca5rQgyUteCZqZGdP8816g.png)

![](https://miro.medium.com/v2/resize:fit:1400/1*3wbDKjchLUu65VCMvuBcJw.png)

Congratulations! Now you know how to deploy a containerized application onto a Kubernetes cluster using Amazon Elastic Container Service(Amazon EKS).

# Step 6: Cleaning up the application & assigned resources

When you are finished experimenting with your application, you should clean up the resources that you created for it to avoid incurring unnecessary costs. You can do so using the following commands:

![](https://miro.medium.com/v2/resize:fit:1400/1*uDjgcUbkjp1Ueg1XUNISMw.png)

I hope now you have a basic idea of what Amazon EKS is and how to use it to create and launch containerized applications on a Kubernetes cluster.