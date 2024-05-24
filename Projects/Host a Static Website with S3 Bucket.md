
**Introduction:**

A static website consists of web pages with fixed content that does not change based on user interactions or input.

Static websites are built with HTML, CSS, and JavaScript files. These files contain the structure, styling, and interactivity of the web pages. Content on static websites is typically pre-defined and doesn’t change frequently.

Since static websites consist of simple files, they are easy to deploy. You can host them on various platforms, including web servers, content delivery networks (CDNs), or cloud storage services like Amazon S3.

Amazon Simple Storage Service (Amazon S3) is an object storage service provides performance, security, and scalability that are unmatched in the market.

Using Amazon S3 (Simple Storage Service) to host a website offers several advantages:

- **Scalability:** S3 is highly scalable, capable of handling traffic spikes without any manual intervention. It can serve a virtually unlimited number of requests per second.
- **Cost-effective:** S3 offers a pay-as-you-go pricing model, meaning you only pay for the storage and bandwidth you use. For low to moderate traffic websites, the cost can be significantly lower compared to traditional web hosting services.
- **Reliability:** Amazon S3 is designed for durability and availability. It stores multiple copies of your data across multiple servers and data centers, ensuring high availability and durability.
- **Performance:** S3 is optimized for serving static content like HTML, CSS, JavaScript, images, and videos quickly and efficiently. Amazon’s global network of edge locations also helps in delivering content to users with low latency.
- **Security:** S3 provides various security features such as access control lists (ACLs), bucket policies, and integration with AWS Identity and Access Management (IAM). You can control who can access your website content and how they can access it.
- **Ease of use:** Setting up a website on S3 is relatively simple and can be done through the AWS Management Console or programmatically via APIs. You don’t need to worry about managing servers, scaling infrastructure, or dealing with complex configurations.
- **Content distribution:** You can easily integrate Amazon CloudFront, AWS’s content delivery network (CDN), with your S3 bucket to distribute your website content globally, improving performance for users across the world.

**Architecture:**

![](https://miro.medium.com/v2/resize:fit:875/1*NZb5m9tOZkMzu0l0iVDS5Q.png)

**Steps:**

**1.** **Create S3 Bucket:**

a. Navigate to S3 console.

![](https://miro.medium.com/v2/resize:fit:875/1*BwX1JfpIUTdBC0vKUvZFiQ.png)

b. Click on Create Bucket.

![](https://miro.medium.com/v2/resize:fit:875/1*8f-vb8XKG-ZnMcY5w3UsdQ.png)

c. Select AWS Region, Bucket type as “General Purpose”. Enter Bucket Name.

d. In Object Ownership, Select ACLs enabled.

![](https://miro.medium.com/v2/resize:fit:875/1*29iOuOlrGImpRs0TAE9RmQ.png)

e. Disable Block all public access and Click on Create bucket.

![](https://miro.medium.com/v2/resize:fit:875/1*KVc-9cfkpGqhhcfxdBtjeg.png)

![](https://miro.medium.com/v2/resize:fit:875/1*qO0Au6g9KqDaNy6uxPJfeA.png)

**2.** **Enable Static Website:**

a. In Properties tab -> Static website hosting, Click on Edit.

![](https://miro.medium.com/v2/resize:fit:875/1*zjiIBO74c5iUacd3yaDENA.png)

![](https://miro.medium.com/v2/resize:fit:875/1*pgstct4bxbwAnmEGaTiYqA.png)

b. Enable Static website hosting and Select Host type as “Host a static website”, Index document as “index.html” and Click on Save Changes.

![](https://miro.medium.com/v2/resize:fit:875/1*USQ9J2zMubbRo_VoawKSmg.png)

**3.** **Upload the file:**

a. In objects tab, Click on Upload.

![](https://miro.medium.com/v2/resize:fit:875/1*UCeu1iNV9s9uOB8wGSrpYQ.png)

b. Click on Add files and add required Html files and Click on Upload.

![](https://miro.medium.com/v2/resize:fit:875/1*BLEaqIvmKV04R_gl9P2K3g.png)

**4.** **Make Object Public:**

a. In Objects tab, Select the files and Click on Actions.

![](https://miro.medium.com/v2/resize:fit:875/1*UX8gSESY1jDF2XRhj3ZYOA.png)

b. Select “Make public using ACL” and Click on Make public.

![](https://miro.medium.com/v2/resize:fit:875/1*LVRRLM36-z-ZpeVDNV2qfw.png)

**5.** **Output:**

a. Click on Index.html file.

b. In Properties tab, we can see object Url.

![](https://miro.medium.com/v2/resize:fit:875/1*GpJTnHbDRKoRPU1rccvMeQ.png)

c. We can access website using that object URL from browser.

![](https://miro.medium.com/v2/resize:fit:875/1*S9CdRi5fDz2miz4B8El31g.png)

**Conclusion:**

AWS S3 static website hosting is a productive and affordable option for both individuals and enterprises. You may quickly and simply set up your own static website by following the step-by-step instructions in this AWS S3 website hosting tutorial.