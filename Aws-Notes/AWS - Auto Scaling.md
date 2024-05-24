
**What is Auto Scaling?**

Auto Scaling is a service that automatically manages and adjusts compute resources to maintain a consistent performance of applications, whether it involves scaling up or scaling down the resources. This is exactly what you can infer from the name of the service. The AWS Auto scaling service ensures that there are sufficient resources or instances to run the application successfully.

The AWS auto scaling service will scale up the servers when they become overloaded due to the increased load on the application by adding more servers with exactly the same configurations.

**Benefits of Auto Scaling**

Improved fault tolerance  
High resource availability  
Improved cost management  
High resource dependability  
The resources’ high degree of adaptability

**Enabling Auto Scaling in AWS**

In order to create auto scaling in AWS, there are two main steps.  
1. Making a launch configuration must come first.  
2. The next step is to establish an AWS auto scaling group.

**Steps to create Launch Configuration**

Navigate to the following page to create a launch configuration.

![](https://miro.medium.com/v2/resize:fit:874/1*lAplj3DTUW3YxjJywge6jw.png)

To create the launch configuration, we must fill in the details.

![](https://miro.medium.com/v2/resize:fit:840/1*lJp2LiUM5QGIIRf-GzL2JA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*2ooGJlxINh4JWMRIMz7-Bg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*Rs2bDA7EmTeigJytQKtJRA.png)

The launch configuration was successfully created.

**Steps to create Auto Scaling Group**

Once the launch configuration has been created, select it and then click action, then create auto scaling group.

![](https://miro.medium.com/v2/resize:fit:834/1*ksc5iWwAmpy4_xoP7PIkEg.png)

It is a seven-step process that must be completed in order to establish an auto scaling group.

**Step 1:** Once the launch configuration is created, select it and click on action and then click on create auto scaling group.

![](https://miro.medium.com/v2/resize:fit:635/1*9p513UkDPZ1pb1yX0S0eng.png)

**Step 2:** Select all of the availability zones in that VPC so that when there is an increase in load, the instance will be distributed across the availability zones.

![](https://miro.medium.com/v2/resize:fit:669/1*7VVep5vNXaMj69dVkUn9EQ.png)

**Step 3:** Special cases in selecting the availability zone are when we must restrict the availability zones due to data policy. We are currently operating without a load balancer, and health checks have a grace period of 150 seconds.

![](https://miro.medium.com/v2/resize:fit:643/1*G12vCfm8t0X5iRmnjkxSRw.png)

![](https://miro.medium.com/v2/resize:fit:875/1*f6-2FQ2OOjzOMN50B7j5QQ.png)

**Step 4:** We must choose the minimum and maximum capacity of the instance that will be created. The scaling policy comes next, where we must decide which type of scaling policy to use, for example, an increase in CPU utilisation of approximately 50% will result in the creation of a new instance. Similarly, we have several scaling policies to choose from.

![](https://miro.medium.com/v2/resize:fit:770/1*CO0hpUpKchN3R8XRhd5ghg.png)

![](https://miro.medium.com/v2/resize:fit:748/1*gRUHYNuTxTaPSQb2-82DYg.png)

**Step 5 & 6:** We can customise the auto scaling group by adding notifications and tags.

**Step 7:** We must review the details that we filled out previously before launching the auto scaling group.

![](https://miro.medium.com/v2/resize:fit:838/1*PdbYJAzR4_wy6V5XvFNxwQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*mCA6tJway9mt9jhJJake4A.png)

Because we specified a minimum of one instance for the auto scaling group, it was created automatically.

![](https://miro.medium.com/v2/resize:fit:875/1*B6SQGLH-6k06Yvv_ZzJRyQ.png)

Now I’m attempting to increase the load above 50%, as per our definition in the auto scaling, the instance must be created when the load exceeds 50%. I’m connecting to the server to increase the load; the commands to do so are listed below.

yum install [https://dl.fedoraproject.org/pub/epel/7Server/x86_64/Packages/e/epel-release-7-14.noarch.rpm](https://dl.fedoraproject.org/pub/epel/7Server/x86_64/Packages/e/epel-release-7-14.noarch.rpm) -y

yum install stress -y

After installing the above- mentioned packages, run the commands listed below.

sudo stress — cpu 80

![](https://miro.medium.com/v2/resize:fit:875/1*Fy7zUWf0-WhtrvKl0sUx9Q.png)

As the load increases, so will the number of instances, as we have set the maximum to four.

![](https://miro.medium.com/v2/resize:fit:875/1*GqxPeupwjDY4JbiPKB7QKA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*bauafcwRv4jQCQyff9LYkA.png)

Because the load is at its peak, all four instances have been created. The auto scaling rule has resulted in the creation of a maximum of four instances

