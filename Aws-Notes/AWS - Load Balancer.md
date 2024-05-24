
Introduction to AWS Elastic Load Balancer — What is ELB?

![](https://miro.medium.com/v2/resize:fit:1250/1*g418EM8dPJEAq3hMq9wMTA.png)

AWS Elastic Load Balancer (ELB)

---
**Client:** A browser and the user behind it.

**HTTP:** The protocol used for communication between a browser(client) and a web server.

**HTTPS:** Same as HTTP but the data is encrypted between the browser(client) and the web server.

**IP:** An address for any internet/intranet device like a computer, server… IP addresses are used by all networked devices to communicate between each other. There are public IPs, this means they are accessible via the internet. There are also private IPs, which mean they are not accessible via the internet. Private IPs are only for internal use. You can consider a public IP like your home address which uniquely identifies you worldwide and a private IP like the room number of a hotel.

**Firewall:** Exists as an application or a hardware device. A firewall filters all traffic. This allows it to choose which traffic goes through it and which is blocked. It can look deep into the traffic and if it sees certain types of cyber attacks, it can stop them. A firewall is used to secure your infrastructure.

**Path:** /home/you on your computer is a path.

**Ping:** A method by which you can check if another device is accessible. Knock, knock, are you there? Yes, I am. That’s about it.

**Port:** Imagine your address, 134 Reynolds Road is an apartment building with many tenants going from #101 to #505. Behind each door is a different person, speaking a different language. Each door is a different port on which communication is different since they don’t speak the same language. A port is identified by a number, some reserved like port 80 for HTTP and others not reserved which can be used by any application.

**Subnet:** A group of IP addresses. You can consider it as a street name. On a street you have multiple addresses represented by a number. The IP address would be Canada.Montreal.ReynoldsRoad.25 and the subnet is a group of IPs, like Canada or Montreal or Reynolds Road.

**Request:** When a client wants something, like a webpage, it sends a request to get it from a web server.

# **So, what is AWS Load Balancing?**

A Load Balancer distributes the load evenly to multiple instances. This means when a request comes to the Load Balancer from a client, it sends the request to one of the available instances. Here is an example:

1. You, the client, type www.foo.com in your browser.
2. Your request goes over the internet to the Load Balancer responsible for [www.foo.com.](http://www.foo.com./)
3. The Load Balancer forwards your request to a web server.
4. The web server receives the request and sends back the homepage of www.foo.com via the Load Balancer.
5. Your browser receives the www.foo.com page you requested.

All this obviously done in a few milliseconds.

![](https://miro.medium.com/v2/resize:fit:875/1*10HyhwhP1B8LF8FWisKS4w.jpeg)

# **What does AWS Elastic Load Balancing do? How does it work?**

There are two types of Load Balancers offered by AWS, the Classic Load Balancer and the Application Load Balancer, each one having different features. Let’s start with what they have in common:

## **-Both Load Balancers-**

Their main functions are the following:

1. Distribute traffic across multiple instances.
2. Check the health of the instances then de-register the unhealthy instances and re-register them when they are healthy again.
3. To offload HTTPS encryption/decryption from your instances.

**Distribute traffic across multiple instances**: how do they do this? Depending on the protocol used, they do this in two ways:

1. Round Robin: Each instance has its turn in an equal manner, one after the other gets a request. It doesn’t take into account how many requests the instance is already handling. TCP uses this on the Classic Load Balancer and so does HTTP/HTTPS on the Application Load Balancer.
2. Least outstanding requests (used by HTTP/HTTPS on the Classic Load Balancer)

**Check the health of the instances**. Using ping, port and path protocols, the Load Balancer monitors the instances. They have an unhealthy threshold, which is the number of times the ping fails before the instance is considered unhealthy and a healthy threshold is the number of time the ping is positive before the instance is considered healthy. So you can be reassured, they don’t check only once!

**Offload HTTPS encryption/decryption from your instances**. This means the Load Balancer can encrypt and decrypt HTTPS requests diminishing the load on your instance, in turn saving you money since you may need less instances.

More features both Load Balancers share are:

They can be **Internet or Internal facing**. The first caters to clients directly from the internet. It is on a public subnet. The latter is on a private subnet. The following image will better describe this.

![](https://miro.medium.com/v2/resize:fit:875/1*8i5FXDo8_X3GDFtzkv4VVw.jpeg)

There is support for **Sticky Sessions**. This means the requests from the same client are always forwarded to the same web server instance. When you are exploring a website, you visit multiple pages, you see multiple images and maybe videos… Your browser asks for this information in multiple requests sent to the Load Balancer. The Load Balancer can send each request to different web server instances, distributing the load, or it can use the Sticky Sessions option to send all of them to the same web server instance. Sticky session is also known as Session Affinity.

**Idle connection timeout** is the time before a connection to/from the Load Balancer is closed. This connection is used for the request and the response. As long as it is opened, it can be reused. When the idle timeout is over, the client then receives an error response. You can use a keep-alive to stop the connection from closing.

**Connection draining** happens when an instance is deregistering with a Load Balancer. The Load Balancer will not send new requests to the instance, but existing requests will be handled by the instance until the connection draining timeout period is over.

**Cross-zone** load balancing is when you have instances in multiple Availability Zones. If you don’t have cross-zone enabled, then the Load Balancer will send requests evenly between each Availability Zone. This may sound good, but if you have an uneven number of instances between each Availability Zone, the requests are not distributed evenly. For example, you have 10 instances in Availability Zone A and 2 in Availability Zone B. Each zone will get half of the requests, making the 10 instances in Availability Zone A almost idle compared to the 2 in Availability Zone B very busy. You can fix this by enabling the cross-zone feature.

Elastic Load Balancing doesn’t use **CloudWatch** to monitor the health of instances behind a Load Balancer but you can use it to monitor the Load Balancer.

Using **X-Forward-For/Proto/Ports headers**. This works for both types of Load Balancer but only with HTTP and HTTPS. What this does is add a header to the request specifying information like client IP so the web server instance has this client IP in it’s logs instead of the Load Balancer IP. For various reasons, like statistics, you might want to know this information. But since the Load Balancer is between the client and the instance acting as a proxy, this information is not available to the instance. The Load Balancer adds the header.

And finally, you might want to enable **access logs** on the Load Balancer. You get most connection information from these logs. They are copied to Amazon S3.

Now let’s compare the Classic Load Balancer with the Application Load Balancer and go over the differences between them.

![](https://miro.medium.com/v2/resize:fit:875/1*mEy-AADIol-OQ4-VZft6aQ.png)

## -The Classic Load Balancer-

Supports load balancing based on **TCP/SSL/HTTP/HTTPS**. For HTTP/HTTPS you get less features than with the Application Load Balancer. We’ll go over some of the features you get with HTTP/HTTPS on the Application Load Balancer. Let’s look a little at TCP/SSL/HTTP/HTTPS:

· **TCP** is a protocol used to logically connect a device with another over a network. When you say TCP, you always have a port associated with it. Let’s use email as an example. You would connect using port 25 which is the port the mail server would be listening on for connections. Using ports provides a level of security because you can, if you want, only allow traffic for a specific port to pass on firewalls, security groups…

· **SSL** is a protocol used to encrypt and decrypt communications between the client and the web server or Load Balancer. This way communications between the two cannot be viewed by anyone on the internet.

· **HTTP** is a protocol used for websites. Its port is 80. Your browser connects to the [www.foo.com](http://www.foo.com/) web server instance or Load Balancer using HTTP on port 80. This is how they communicate.

· **HTTPS** is the same as HTTP but with encryption. Its port is 443. For your information, HTTPS is a combination of HTTP and SSL.

The **proxy header** is added to all TCP/SSL connections by the Load Balancer to provide client information to the instances. As we saw earlier, X-Forwarded-For headers are only for HTTP/HTTPS.

## -The Application Load Balancer-

This Load Balancer has more features than the Classic Load Balancer even though it supports only HTTP/HTTPS.

**Path-based routing** is when the Load Balancer chooses which instance to send the request to based on the path in the URL. URL is for example [www.foo.com/thisisaurl/](http://www.foo.com/thisisaurl/). Path-based routing is when you have [www.foo.com/orders](http://www.foo.com/orders) requests sent to instance 1 & 2 and [www.foo.com/images](http://www.foo.com/images) requests sent to instance 3 & 4.

**Host-based routing**, almost the same as path-based routing but the URL is as follows orders.foo.com & images.foo.com

**Route to multiple ports on a single instance**. We looked a bit into ports earlier, it is on a port that the instance listens. Some ports are reserved; for example, HTTP on port 80, but some ports are free to use. Different applications use different ports. This feature allows you to have multiple applications, listening on different ports, to be load balanced on the same Application Load Balancer. This way your instance can handle being load balanced for different applications like HTTP on port 80, SMTP on port 25 and a custom application on port 5500.

This Application Load Balancer also supports **HTTP/2**. This is just a newer version of HTTP with many new features that we will not cover in this article.

Support for **WebSockets**, what is this? This is a protocol that enables a connection between an HTTP/HTTPS client and an HTTP/HTTPS server to have less overhead. The web server instance can send content to the browser without it being requested and also keeps the connection opened.

**Deletion protection** is a small feature that can save you from a whole lot of problems. When you set this, you are unable to delete your Application Load Balancer. Unintentionally deleting a Load Balancer happens to the best of us. With deletion protection set, you need to manually unset it before you are able to delete a Load Balancer.

You can also have **multiple SSL certificates** on the same Load Balancer. It is quite frequent for a company to have multiple web sites. With the Classic Load Balancer, you need one per site if you use different SSL certificates. This is not the case with the Application Load Balancer which can handle multiple SSL certificates. What is an SSL certificate? You need this to encrypt/decrypt your HTTPS requests. For this you buy a certificate from a third party supplier. You can have a single one for multiple hosts, [www.foo.com](http://www.foo.com/) and [www.images.foo.com](http://www.images.foo.com/) but you need a different one for multiple sites like [www.foo.com](http://www.foo.com/) and [www.nofoo.com](http://www.nofoo.com/).

# **Why would you want it?**

Well, there are so many reasons why you would want to use AWS Elastic Load Balancing that the list would be too long. Instead let’s look at it from a different perspective, why would you not want it? In reality, it’s pretty much a must have. You can do without for three reasons:

1. You only have one instance (you could still use it to offload HTTPS encryption/decryption or be prepared for future growth).
2. Your application doesn’t support it.
3. You want to use your own load balancing application.

# **Who uses it (use case)?**

Here are a few made-up examples of who could use AWS Elastic Load Balancing. I insist on the fact that they are MADE-UP!

I’m using Google for the following example because everyone knows it well. Keep in mind that Google has its own Cloud Solution and for this reason would never use the AWS Cloud.

[www.gmail.com](http://www.gmail.com/) certainly have an unimaginable amount of mail servers. To distribute the load on port 25 using the TCP protocol, they would need to use the Classic Load Balancer. [www.google.com](http://www.google.com/) would use an Application Load Balancer for HTTP and HTTPS. Their sites like docs.google.com or plus.google.com would use the host-based routing on an Application Load Balancer.

[www.amazon.com](http://www.amazon.com/) also probably have an unimaginable amount of web server instances. They may be using the Application Load Balancer for HTTP and HTTPS, respectively on port 80 and 443. They might also be off-loading encryption and decryption of HTTPS requests to the Load Balancer.

What about a more reasonable sized example? Let’s take a company [www.foo.com](http://www.foo.com/) that sells cameras. They could have 3 web server instances running behind an Application Load Balancer for HTTP and HTTPS requests. You don’t need to have hundreds of instances to use a Load Balancer. Once you have at least two instances, which you should always have, then a Load Balancer is a solution for you. As we saw earlier, you could also just have one.

# **A little bit about security**

You have a **Security Group** for your Load Balancer. You can allow traffic as per your wishes and everything else is denied. A best practice for a website is to allow only HTTP and HTTPS traffic.

You can use the **AWS WAF** (Web Application Firewall) with the Application Load Balancer to secure even more your instances. Application and hardware firewalls go a step further than Security Groups. On top of allowing and denying traffic, they block certain types of attacks. In the case of a website, applicative attacks are on port 80 and 443 (HTTP and HTTPS), they wouldn’t be blocked by a Security Group.

Using **HTTPS or TCP/SSL** connections encrypt your data in transit giving an extra layer of security.

# **Any limits?**

There are obviously more limits in regards to the two Load Balancers, but these are the important ones for what is covered in this article.

![](https://miro.medium.com/v2/resize:fit:875/1*FZBPDd-u3M329GHja-CMzw.png)

# **How much does it cost?**

Pricing depends on the location, it is based on the cost to AWS for a specific location. So here we will look at pricing in Frankfurt. Pricing is provided in US dollars, due to varying exchange rates let’s stay with this.

**Classic Load Balancer**

- $0.030 per hour the Load Balancer is up and running
- $0.008 per GB of data processed by the Load Balancer

Let’s look at an example of this. Take a website running 5 instances. The total amount of GB processed by the Load Balancer is 75 GB for the month.

- $0.030 x 720 hours (30 days) = $21.60
- $0.008 x 75 GB = $0.06

Total monthly cost for this Classic Load Balancer is **$21.66**.

**Application Load Balancer**

When it comes to pricing, AWS didn’t go down the simple route for this Load Balancer. The pricing models are often quite complicated making it more difficult to get a price for a desired infrastructure. Before giving you a price for this Load Balancer we need to go through some theory.

LCU (Load Balancer Capacity Unit) is just a metric used to calculate the price. So part of the pricing is based on LCUs per hour. To calculate the LCU you have four different elements to look at. Note that you are charged only for the one with the highest LCU (why make it simple!):

1. New connections per second. 1 LCU is 25 connections per second.
2. Active connections per minute. 1 LCU is 3000 active connections per minute.
3. Data processed in Mbps. 1 LCU is 2.22 Mbps per hour.
4. Number of rules processed per second. 1 LCU is 1000 rules per second. (we didn’t look into rules, so just take this as is). The first 10 are free. Request rate X (number of rules processed — 10)

Let’s look at an example taken directly from the AWS web site.

1. 1 new connection per second = 1 / 25 = 0.04 LCU
2. 120 active connections per minute = 120 / 3000 = 0.04 LCU
3. 2.4 Mbps data processed per hour = 2.4 / 2.22 = 1.08 LCU
4. 250 rules per second = 250 / 1000 = 0.25 LCU (How did we get to 250? 5 requests per second x (60 rules — 10 free) = 250 rule evaluations)

Now, note that you don’t add all the LCUs like you might expect, you actually just take one, the highest and then calculate the cost with that value.

Again let’s use Frankfurt for pricing:

- $0.0270 per hour the Load Balancer is up and running
- $0.008 per LCU-hour

In this example the price is as following:

- $0.0270 x 720 hours (30 days) = $19.44
- The maximum LCU is 1.08 (data processed). $0.008 x 1.08 = $0. 00864 X 720 hours (30 days) = $6.22

Total monthly cost for this Application Load Balancer is **$25.66**.

So now, you try it!

# **You’re interested? Where to go from here?**

Did I poke your curiosity? Do you want more? Start with getting your staff trained or you could work with an AWS Certified Solutions Architect, and guess what, that’s what I am J. Damn, now you know why I wrote this article. Whether you are new to the AWS Cloud or you already have services, you need to go through the following steps:

1. Analyze your requirement’s
2. Provide a solution
3. Prepare a plan
4. Go through with the plan

And that’s it; you will then be using AWS Elastic Load Balancing.

# **You want more?**

This section is a bit more advanced and doesn’t contain a detailed explanation of all the concepts. There are details you don’t really need to understand both Load Balancers, it just extra information for those who are curious and want more.

## -Both Load Balancers-

Your instances don’t need public IP addresses; all is done using **private IPs**.

The Load Balancer needs to be in the **same VPC** across all Availability Zones and in a **single subnet** within an Availability Zone.

If you are using the Load Balancer in conjunction with **Auto Scaling**, Auto Scaling will automatically register the new instances with the Load Balancer.

As time passes, your Elastic Load Balancer may need to **scale up**. IPs are changed automatically and DNS, which has a TTL set to 60 seconds, is updated.

**Keep-alive** is supported on back-end connections by default. This keeps the back-end connections opened.

**Load Balancer nodes**, wonder what they are? They are actually the instances on which the AWS Elastic Load Balancers are. Yes, the Load Balancers are instances.

## -The Classic Load Balancer-

You can set the duration of the **sticky session** cookie.

## -The Application Load Balancer-

Supports **IPV6**.

Instances are called **targets** and groups of instances that are part of the same load balancing scheme are part of a **target group**.

**Rules** are associated with a listener. They tell the Load Balancer how to route requests to the targets in one or more target groups. Each rule consists of:

- Priority (lowest to highest) (default rule has lowest)
- Action (only “forward”)
- Optional host condition (multiple domains for single Load Balancer)
- Optional path condition

Support for **container-based** applications using Amazon ECS (EC2 Container Service). Containers are like having multiple servers on an instance. Each container runs applications independently of other containers. When launching a container, it is automatically registered with the Load Balancer. The Application Load Balancer support dynamic host port mapping. Understanding container-based applications is out-of-scope of this article.

**Access logs** are stored in compressed format.

The Application Load Balancer **outperforms** the Classic Load Balancer.

---

## TL;DR

[AWS Elastic Load Balancer (ELB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) automatically distributes your incoming traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones. It monitors the health of its registered targets, and routes traffic only to the healthy targets. Elastic Load Balancing scales your load balancer as your incoming traffic changes over time. It can automatically scale to the vast majority of workloads.

## **ELB** Types

- [Application Load Balancer (ALB)](https://medium.com/awesome-cloud/aws-application-load-balancer-alb-overview-introduction-to-amazon-alb-what-is-aws-alb-b5280f625153)
- [Network Load Balancer (NLB)](https://medium.com/awesome-cloud/aws-network-load-balancer-nlb-overview-introduction-to-amazon-nlb-what-is-aws-nlb-elb-837749c20063)
- Gateway Load Balancer (GWLB)
- Classic Load Balancer (CLB)

> [Difference between Application load balancer and Network load balancer](https://medium.com/awesome-cloud/aws-difference-between-application-load-balancer-and-network-load-balancer-cb8b6cd296a4)

## ELB **Schemes**

- Internet-facing: _ELB nodes have public IP addresses._
- Internal: _ELB nodes have private IP addresses._

> Both internet-facing and internal load balancers route requests to your targets using private IP addresses. Therefore, your targets do not need public IP addresses to receive requests from an internal or an internet-facing load balancer.

## ELB Target Type**s**

ELB distribute incoming traffic to:

- Instances _(EC2, EC2 with Auto Scaling, Containers with ECS)_
- IP addresses _(VPC Subnets, RFC 1918 CIDR, On-premises with Direct Connect or Site-to-Site VPN)_
- ==Lambda functions== _(for ALB type)_

## ELB Components Architecture

![](https://miro.medium.com/v2/resize:fit:694/0*JUHxEyD1Kxx_CcYJ.png)

ELB Components Architecture (Ref: [AWS Docs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html))


---

![](https://miro.medium.com/v2/resize:fit:875/1*SEuuFedWjZP2R8nI2TY00g.png)

1. _Give your Load balancer some meaningful name e.g., my-alb-demo_
2. _You need to select Scheme(it can be Internet-facing(An internet-facing load balancer routes requests from clients over the internet to targets. Requires a public subnet) or Internal(An internal load balancer routes requests from clients to targets using private IP addresses))_
3. _IP address type(Can be IPv4 or Dualstack(Includes IPv4 and IPv6 addresses))_

![](https://miro.medium.com/v2/resize:fit:875/1*DkWomnWsGUTvfz8ZMghvzA.png)

- _Select the VPC and availability zone_

![](https://miro.medium.com/v2/resize:fit:875/1*E3MO0qqU4IHbeyVCISBeGA.png)

- _Under Listeners and routing, define the port and protocol on which the load balancer must listen. Each Application_
- _Load Balancer needs at least one listener to accept traffic._

![](https://miro.medium.com/v2/resize:fit:875/1*5Wsq9zoK9QrHzR1jHAhlDw.jpeg)

- _Click on the Target group. Target group defines the logical grouping of the targets._

![](https://miro.medium.com/v2/resize:fit:875/1*s01kOULRS_jkKo2gZFoTiw.png)

![](https://miro.medium.com/v2/resize:fit:875/1*W4rkCwZODy1z6yJJx_DUbg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*W4rkCwZODy1z6yJJx_DUbg.png)

- _Click on Next at the bottom of the screen_

![](https://miro.medium.com/v2/resize:fit:875/1*nh8X23maS9csS4A5-kI3RQ.jpeg)

- _Click on Create target group_

![](https://miro.medium.com/v2/resize:fit:875/1*3Witt8B-4YxbZPTpo75aeA.png)

- _Go back to the ALB console and select the target group you have just created. Click on Create load balancer at the bottom of the screen._

![](https://miro.medium.com/v2/resize:fit:875/1*3Witt8B-4YxbZPTpo75aeA.png)