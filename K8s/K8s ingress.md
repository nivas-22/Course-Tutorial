
Every Kubernetes cluster needs two things — one, a way to expose the service deployed on the container and, two, a way to balance the load/traffic on these deployed services. In this article, we’re going to discuss how Kubernetes Ingress helps us in achieving these.

These are the following topics that are going to be covered in this article:

- What is Kubernetes?
- Different ways exposing an application/service
- Why do we need Kubernetes Ingress?
- What is Kubernetes Ingress?
- A hands-on demo on setting up a Kubernetes cluster on AWS and setting an ingress for the cluster

# What is Kubernetes?

Before understanding what Kubernetes Ingress is, let’s have an overview of what is Kubernetes. Kubernetes is an open source platform that automates container operations such as deploying containers, scaling up, scaling down of containers, load balancing etc. You can just cluster the hosts running containers and Kubernetes will help you easily and efficiently manage these clusters.

# Different Ways Of Exposing An Application In Kubernetes

Once you’ve deployed your application on the container, you need a way to expose it outside the cluster to get the external traffic, or in simpler words expose it to the internet so the world can access it.

There are three ways to get this done:

## Using service type as ClusterIP:

ClusterIP is the default Kubernetes service type. Using this service type, a Global IP called ClusterIP is assigned to that cluster which is alive till when the cluster is alive. Using this IP, we can access all the services associated with that cluster. So basically, we use this type of service when we want to expose a service to other pods only within the same cluster. This service is accessed using Kubernetes proxy.

## Using a Kubernetes service of type NodePort:

When using service type as NodePort, a port is opened on every node that is part of the cluster and the application can be deployed on that node or the outside traffic is routed to that NodePort even if the application is not running on that node. We can either explicitly mention the port that is to be activated or the Kubernetes assigns a NodePort by default.

## Using a Kubernetes service of type LoadBalancer:

Using service type as LoadBalancer, it automatically creates an external load balancer that points to a Kubernetes cluster, this external load balancer is associated with a specific IP address and routes external traffic to the Kubernetes service in the cluster. Implementation of load balancer depends on your cloud service provider.

## Using Kubernetes Ingress:

Kubernetes ingress is not a service but a collection of routing rules that govern how the external users access services running on the Kubernetes cluster. Ingress sits in front of the cluster and acts as a smart router. This is always implemented using a third party called a proxy. Traffic routing is done by an ingress controller.

I’m sure you guys are wondering what an ingress controller is but don’t worry as that’s the topic we’re going to discuss in detail further in this article but first let’s see what brings us to the needs of Kubernetes Ingress.

# Why Kubernetes Ingress?

When you have an application deployed on your cluster, you obviously want to expose it to the internet to get inbound traffic otherwise what is the deployment for, right? Kubernetes Ingress is a built-in load balancing framework for routing external traffic.

**_There are two main reasons why we use Kubernetes Ingress:_**

1. When running the cluster and deployments on a cloud platform like AWS or GKE, the load balancing feature is available out of the box and there’s no need to define ingress rules. But again, using external load balancers means spending more money and especially when your deployment is a small-scale deployment and you have a tight budget, you might as well use Kubernetes Ingress which is absolutely free and economical.
2. Ingress is an abstraction of layer 7 load balancing and not layer 4. When we talk about layer 7, we refer the layer 7 of the OSI model which is the application layer. It routes the traffic using the actual content of the message. When the load balancer has access to the content of the message, it can obviously make smarter routing decisions compared to counter load balancing techniques which use Layer 4(transport layer).

# What is Kubernetes Ingress?

By now you would have understood that Kubernetes Ingress is a collection of routing rules that govern how external users access services running on the Kubernetes cluster.

Functionalities provided by Kubernetes Ingress:

1. Layer 7 load balancing — As discussed above
2. SSL Termination — Secure your connection with SSL termination
3. Name-based virtual hosting — Defines routes to services based on incoming request’s hostnames. This allows you to run multiple services on the same IP address.

Let’s get further into the details. Ingress is split into two main parts — Ingress resources and ingress controller

1. **Ingress Resources**  
    Ingress Resources defines how you want the requests to the services to be routed. It contains the main routing rules.
2. **Ingress controller  
    **What ingress controller does is, it reads the ingress resource’s information and process the data accordingly. So basically, ingress resources contain the rules to route the traffic and ingress controller routes the traffic.

Routing using ingress is not standardized i.e. different ingress controller have different semantics (different ways of routing).

At the end of the day, you need to build your own ingress controller based on your requirements and implementations. Ingress is the most flexible and configurable routing feature available.

# Demo 1: Create a Kubernetes cluster on AWS

The first thing that’s needed to deploy any kind of service/application on Kubernetes, is a cluster. Every cluster consists of one master and single or multiple nodes depending on the requirement. In this demo, I’m going to show you how to create a Kubernetes cluster on AWS.

**Step 1:** Create an instance, name it kubectl. We’re going to deploy the cluster using this instance. This instance only has the kubectl tool installed that will interact with the master, it does not have Kubernetes installed on it.

> **Note:** We have three services in AWS that we’ll be using here — s3 bucket which stores all the files, EC2 which is used to create an instance and deploy the service and IAM which is used to configure permissions. These three pictures have no clue about each other’s existence and hence Roles come into the picture.

**Step 2:** Create a Role in the IAM section

![](https://miro.medium.com/v2/resize:fit:1400/1*8miFFuPOjwR48oeCK0oNsA.png)

![](https://miro.medium.com/v2/resize:fit:1400/1*ZteontXSNOpQuXEKyvZ-ng.png)

Attach the appropriate policy to your Role (for this example admin access is given)

![](https://miro.medium.com/v2/resize:fit:1400/1*abaFzhfhbEn2eswmWmXQpw.png)

Next, it’ll ask you to add tags which are optional. In my case, I haven’t attached any tags.

Give your Role a name and review the policies assigned to it and then press **Create role**.

![](https://miro.medium.com/v2/resize:fit:1400/1*uLA1epKtfH9m76Q1Tj8uug.png)

**Step 3:** Attach the role to the instance. Go to **instance settings -> Attach/Replace IAM role** -> attach the role you’ve created and then click on **Apply**.

![](https://miro.medium.com/v2/resize:fit:1400/1*e2jmEcXkpHy2bv-xLyuOkw.png)

**Step 4:** Once you’ve created the instance and attached the role, open the command emulator i.e. cmder or putty and connect to the AWS instance. I’ll be using cmder for this demo. Once you’ve connected to the instance, update the repository and install aws-cli using the following commands:

$ sudo apt-get install    
$ sudo apt-get install awscli

**Step 5:** Install and set up kubectl using the following commands:

$ sudo apt-get update && sudo apt-get install -y apt-transport-https  
$ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -  
$ echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list  
$ sudo apt-get update  
$ sudo apt-get install -y kubectl

**Step 6:** Install Kops on the system using the following commands:

$ wget https://github.com/kubernetes/kops/releases/download/1.10.0/kops-linux-amd64  
$ chmod +x kops-linux-amd64   
$ mv kops-linux-amd64 /usr/local/bin/kops

**Step 7:** With Kops installed, you must configure a domain for your cluster to access it from outside. Create a hosted zone for it

**Services-> Route53-> Hosted zones-> Create Hosted Zone**

![](https://miro.medium.com/v2/resize:fit:1400/1*jDYKbMrgyE7KUYPy9xcfPQ.png)

Add a domain name for your cluster, change the type from **Public Hosted Zone** to **Private Hosted Zone for Amazon VPC** and copy your instance **VPC ID** from the instance page to the VPC ID column and add the region you want to create your hosted zone in.

![](https://miro.medium.com/v2/resize:fit:1400/1*o2L1IJvOipQtn-jrfru0og.png)

Copy the VPC ID

![](https://miro.medium.com/v2/resize:fit:668/1*GJPYVYZbf6PGRd7FWaChpg.png)

The above screenshot shows where to add Domain name and VPC ID

![](https://miro.medium.com/v2/resize:fit:1400/1*FT_clynuitVq2eg4ch4JNw.png)

You can now see your Hosted Zone is created.

**Step 8:** Create a bucket as the same name as domain name using the following command:

$ aws s3 mb s3://kube-demo.com

![](https://miro.medium.com/v2/resize:fit:880/1*BupHKYzvva2PaDGQC75h8w.png)

Once you’ve created the bucket, execute the following command:

$ export KOPS_STATE_STORE=s3://kube-demo.com

**Step 9:** Before you create the cluster, you’ll have to create SSH public key.

$ ssh-keygen

Enter file where you want your key pair to be saved and create a password to access the ssh public key. In this case, I’ve chosen the default location and used no password.

**Step 10:** Now that you’ve created the SSH key, create the cluster using the following command:

$ kops create cluster –cloud=aws –zones=us-east-1a –name=useast1.kube-demo.com –dns-zone=kube-demo.com –-dns private

![](https://miro.medium.com/v2/resize:fit:1400/1*9YuZpk5jZt_e8znuogGDIg.png)

And then update the cluster

$ kops update cluster useast1.kube-demo.com

This will create the resources needed for your cluster to run. It will create a master and two node instances.

Now when you check your instances, you would see three new instances that would have got created. One of them will be your master node and the other two your worker nodes and TADA! Your cluster is created.

![](https://miro.medium.com/v2/resize:fit:1400/1*WcIY_foTxbsoyK1GHHfP9w.png)

Your s3 bucket will now have some folder in it, which is basically your cluster configuration file.

![](https://miro.medium.com/v2/resize:fit:1400/1*MhEztDuM4uf9ZHRnNp2paw.png)

**Step 11:** Now if you ssh into your master node and do a kubectl get nodes, you should find your nodes in the ready state.

$ ssh  -i .ssh/id_rsa admin@ipv4-public-ip-of-master   
$ kubectl get nodes

![](https://miro.medium.com/v2/resize:fit:1334/1*5Yr_OIFITrwQ9vaZIMdTDQ.png)

# Demo 2: Create an Ingress(nginx) loadbalancer controller

**Step 1:** The following command is mandatory for all configurations

$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/mandatory.yaml

![](https://miro.medium.com/v2/resize:fit:1400/1*sZDpFqeVYiWZkzVd47s3bA.png)

**Step 2:** Now, the next command depends upon the environment you’re using your cluster in.

For this example we’re going to use AWS L4 configuration:

$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/provider/aws/service-l4.yaml    
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/provider/aws/patch-configmap-l4.yaml

![](https://miro.medium.com/v2/resize:fit:1400/1*JlPGsRvphZLpp-D-Dp1JhQ.png)

**Step 3:** Check your pods to see all the Ingress pods are up and running

$ kubectl get pods --all-namespaces

![](https://miro.medium.com/v2/resize:fit:1400/1*ZqMs2M27Bg05R4TrVCPX2w.png)

**Step 4:** Check the services to verify Ingress service is working

$ kubectl get svc –all-namspaces

![](https://miro.medium.com/v2/resize:fit:1128/0*clk84Iyj2zcDpysb.png)

**Step 5:** Now create a deployment like we did before  
Here we’re using an httpd deployment as an example

**Step 6:** Create an httpd clusterip service

$ kubectl create service clusterip httpd --tcp=80:80

![](https://miro.medium.com/v2/resize:fit:1382/1*9-0jLjehcOKNLHU1EWsCyA.png)

![](https://miro.medium.com/v2/resize:fit:1128/1*UqDrBHh-WMDaTmaZlBub6Q.png)

**Step 7:** Curl the service IP to make sure it is attached to the pods

$ curl <Cluster IP address>

![](https://miro.medium.com/v2/resize:fit:1206/1*0z_pjif-bnqyFQ7bk2_3xA.png)

**Step 8:** Now, create an ingress rule for your service so you can access the service at /test to route the external traffic.

$ vi ingress.yaml

Now, write the following details in the yaml file.

apiVersion: extensions/v1beta1  
kind: Ingress  
metadata:  
  name: test-ing  
  annotations:  
    nginx.ingress.kubernetes.io/rewrite-target: /  
spec:  
  rules:  
  - http:  
      paths:  
      - path: /test  
        backend:  
          serviceName: httpd  
          servicePort: 80

**Step 9:** Deploy the Ingress rule

$ kubectl apply -f ingress.yaml

![](https://miro.medium.com/v2/resize:fit:924/1*exOfiLVoFI4J9LZ-W6lJKw.png)

![](https://miro.medium.com/v2/resize:fit:938/1*oyUj10-jIfdtHEzhKcGCuA.png)

![](https://miro.medium.com/v2/resize:fit:1400/1*2MRr4x6LsKEXGf2IRAfQEg.png)

**Step 10:** Now copy the Ingress service external IP and add /test to it in your browser to verify

![](https://miro.medium.com/v2/resize:fit:1400/1*BMiFXNgE3BW39CuD02wknA.png)

This exact same thing can be done on other cloud platforms as well. I have used this Installation guide for my environment setup which also has a detailed explanation of the installations on other platforms.

Of course, this was a small demo of routing traffic but if implemented well, it can do wonders. Games like Pokémon Go are deployed on Kubernetes and uses Ingress. I’m sure all of you must have heard, if not played the highly trending game, Pokémon Go_._ Now the traffic shot up beyond the company’s expectations and the only reason they were able to handle so much traffic because of Kubernetes.