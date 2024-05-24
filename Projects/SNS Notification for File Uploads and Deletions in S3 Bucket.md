
**Introduction:**

In this blog, we are going to learn how we can receive an SNS email notification whenever any object is uploaded or removed from AWS S3 bucket.

Amazon S3 is a highly specialized file storage system. Similar to file folders, Amazon S3 buckets allow you to store, retrieve, backup, and access things.

There are four different categories of objects that cause events. Put, Post, Copy, Multipart Upload, Remove, Replicate, and Restore are some of their verbs. As a result, anytime any of the events happen in our S3 bucket, a notification is published to a topic, where subscribers can access the messages.

Amazon Simple Notification Service (Amazon SNS) organizes and controls the transmission of messages to clients or endpoints that have subscribed to them.

You can add subscribers to an SNS subject and then publish messages to all of those subscribers.

**Architecture:**

![](https://miro.medium.com/v2/resize:fit:1250/1*avUQWm8fpCJYaeXkT3ww5g.png)

**Steps:**

**a.** **Creating S3 bucket:**

i. Navigate to S3 Console.

![](https://miro.medium.com/v2/resize:fit:875/1*H-bXgyKgjMDPHv5W6PR_lw.png)

ii. Click on Create bucket.

iii. Enter Bucket name, choose on AWS Region where you want to create bucket and click on Create.

![](https://miro.medium.com/v2/resize:fit:875/1*Hpl3VFjzvmu4Cl5L74sTjg.png)

**b.** **Create SNS Notification:**

i. Navigate SNS Console.

![](https://miro.medium.com/v2/resize:fit:875/1*bSVuTFubxCQ53cViV45J2A.png)

ii. Click on Create topic.

iii. Choose topic type as Standard, Enter topic Name and Description.

![](https://miro.medium.com/v2/resize:fit:813/1*3Ny45wDFZ96oyQCv6h7c3Q.png)

iv. In access policy, Choose Basic Method and Specify Publishers and Subscribers as “Everyone” and click on Create topic.

![](https://miro.medium.com/v2/resize:fit:875/1*hfS32Nw7HjznU_3aMeO7Ww.png)

**c. Subscribe to SNS Topic:**

i. Once SNS topic created, in Subscription tab, Click on Create Subscription.

![](https://miro.medium.com/v2/resize:fit:875/1*soPUqCbA3IMjmiCYP-ztWg.png)

ii. Select Protocol as Email and Enter Email address in Endpoint and Click on Create.

![](https://miro.medium.com/v2/resize:fit:875/1*C3lntD38j9dh9AivsMmiEQ.png)

iii. After subscription is created, you can see status as “Pending Acceptance”.

![](https://miro.medium.com/v2/resize:fit:875/1*ovjTOt9FpDeL7LUfzdud0A.png)

iv. You will receive Mail to Email address provided in the previous step to confirm Subscription.

![](https://miro.medium.com/v2/resize:fit:875/1*clplIwvwjZeRwyRKHl3OJg.png)

v. Once you confirm, Subscription status is confirmed. Now Subscribed Email address will start receiving mails.

![](https://miro.medium.com/v2/resize:fit:875/1*qdgpXnYMlRSZaqLhwck0gw.png)

**d.** **Create S3 Event:**

i. Navigate to S3 Console.

ii. Choose the bucket for which you wish to configure the notifications.

iii. In Properties tab, click on create event notification.

![](https://miro.medium.com/v2/resize:fit:875/1*Zve0gq9gvst-mnAL4fxOow.png)

iv. Enter Event name, choose Event types as Object creation and Object removal, Destination as SNS topic and Specify SNS topic by choosing SNS topic from the list or by providing SNS topic ARN and Click on Save changes.

![](https://miro.medium.com/v2/resize:fit:875/1*wZZIsz2voqDuJUD3LqWgcw.png)

**e.** **Test:**

An email will be sent to your subscribed email address if you try to upload or delete any files from that S3 bucket

**Upload:**

![](https://miro.medium.com/v2/resize:fit:875/1*0lTSdyN16-GamN87MZku1w.png)

![](https://miro.medium.com/v2/resize:fit:875/1*w3jSKEigQB3-DzF_KCmg_g.png)

**Deletion:**

![](https://miro.medium.com/v2/resize:fit:875/1*YsLBwfUQlm0NxvzTPutxPA.png)