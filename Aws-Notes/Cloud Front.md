
Amazon CloudFront is a **content delivery web service(CDN)**. It integrates with other AWS Cloud services to give developers and businesses an easy way to distribute content to users across the world with low latency, high data transfer speeds, and no minimum usage commitments.

# Amazon CloudFront Basics:

There are three core concepts that you need to understand to start using CloudFront: distributions, origins, and cache control.

**1.Distributions:** To use Amazon CloudFront, you start by creating a distribution, which is identified by a DNS domain name. To serve files from Amazon CloudFront, you simply use the distribution domain name in place of your website’s domain name; the rest of the file paths stay unchanged.

**2.** **Origins:** When you create a distribution, you must specify the DNS domain name of the origin — the Amazon S3 bucket or HTTP server — from which you want Amazon CloudFront to get the definitive version of your objects (web files).

**3. Cache-Control:** Once requested and served from an edge location, objects stay in the cache until they expire or are evicted to make room for more frequently requested content.

# AWS CloudFront Advanced Features:

**Dynamic Content, Multiple Origins, and Cache Behaviors:** Serving static assets, such as described previously, is a common way to use a CDN.

- An Amazon CloudFront distribution, however, can easily be set up to serve dynamic content in addition to static content and to use more than one origin server.
- You control which requests are served by which origin and how requests are cached using a feature called cache behaviors.
- A cache behavior lets you configure a variety of Amazon CloudFront functionalities for a given URL path pattern for files on your website.
- For example see below figure One cache behavior applies to all PHP files in a web server (dynamic content), using the path pattern *.php, while another behavior applies to all JPEG images in another origin server (static content), using the path pattern *.jpg.

![](https://miro.medium.com/v2/resize:fit:875/1*qN9GktOGXQKe4UUzXhQCgQ.png)

Delivering static and dynamic content

# How AWS CloudFront Delivers the content?

![](https://miro.medium.com/v2/resize:fit:748/1*biX0OgpCzOJzLonmi2MZHA.png)

1. The _Client_ access a website and requests an object to download.
2. The _DNS_ routes user request to AWS CloudFront.
3. AWS _CloudFront_ connects to its nearest _edge locations_ in order to serve the user request.
4. At edge location, AWS CloudFront looks for the requested cache file and if it is not there it compares the requirements with the specifications and shares it with the respective _server_.
5. The server responds by sending the files back to the CloudFront edge locations.
6. Then CloudFront shares the file or request with the client.

# **Benefits of AWS CloudFront:**

![](https://miro.medium.com/v2/resize:fit:875/1*VWP3QPru7eYlpNlByxKdQQ.jpeg)

Uses of CloudFront

1. Cost-Effective
2. Time-Saving
3. Content Privacy
4. Highly Programmable
5. Geo-Targeting
6. Accelerates static website content delivery.
7. Serve on-demand on live streaming videos.

# Companies using CloudFront

![](https://miro.medium.com/v2/resize:fit:596/1*UTg_4Caq-IE4aiKesYSVEw.png)

Companies using CloudFront

- Jio Saavn: It uses Amazon CloudFront to deliver 15 petabytes of audio and video to its subscribers globally.
- Sky News: It uses the service in order to unify the content for faster distribution to subscribers.
- Discovery Communication: It uses the service for delivering API, Static assets, and dynamic content.
- Tv1EU: The service helps in improving latency and performance which results in the fastest delivery of content.
# CloudFront Components

There are multiple components in AWS CloudFront

1. **CF Origin** — The source location of your content
2. **CF Distribution** — The configurable unit of CloudFormation
3. **Edge Locations** — The local cache of your data
4. **Regional Edge Caches** — A larger version of an Edge location, which sits between the origin and an typical Edge location primarily to improve the performance.

# CloudFront Caching Process

There are multiple steps involved in CloudFront caching process (See Figure 02).

On the diagram (Figure 02) you can see two users from the same region are trying to access a single file from the Origin (S3). There are two Edge cache locations having connected a single Regional Edge cache in the same region. Each user points to separate Edge cache locations.

![](https://miro.medium.com/v2/resize:fit:875/1*5_Y7ZhcRdRkLVuh_wR5vPg.png)

Figure 02 — The CloudFront Architecture

Step 1: The user request is landed on the closest Edge location. The process checks the requested resource (image) is available at the Edge location.

Step 2: If the content is available, it returns the successful response with the requested image. This is a **“Cache Hit”** scenario.

Step 3: If it is not available at the Edge location, the process requests it from the Regional Edge location. This is a “**Cache Miss**” scenario. If it is available it sends the image back to the requester.

Step 4: If not, it requests it from the AWS origin

Step 5 and 6: The process returns the image back to the requester.

Step 7: Another user tries to retrieve the same image, which the first user tried. The second user gets it from a different Edge location close to his access.

Step 8: Since the second Edge location does not have the image file (since it was copied only to the first Edge location before), it tries to get it from the Regional Edge location, which the first user also used. (Remember that multiple Edge location can share the same Regional Edge location).

Step 9 and 10: Since the Regional Edge location already has it, it returns the image file back to the second user.

# CloudFront Behaviors

Behavior is a configuration within an AWS CF Distribution (See Figure 03).

A distribution can have many behaviors which are configured with a path pattern. If requests match that pattern, that particular behavior is used, if not the default behavior is taken into consideration.

CloudFront Behaviors control much of the Origins, TTL, protocol policies and privacy settings within CloudFront.

![](https://miro.medium.com/v2/resize:fit:875/1*E_Vfl13-lNOlojqwZkdLsQ.png)

Figure 03 — CloudFront Behaviors

# The TTL

TTL is the time an object stays or active at an Edge location and by default the TTL value is 24 hours.

Even if you have a new copy of the file being requested at the Origin, if the request comes within the TTL to Edge location, the Edge location returns the file copy at the Edge location back to the client.

Once the file expires (exceeding the TTL) then it will look at the file at the origin to see whether file has got changed compared to the edge location copy.

**If it is not changed** → It will return **304 Not Modified** response.

**If it is changed** → It will return **200 OK** response and will copy the new copy to the Edge location and will return the same to the client.  
Minimum and Maximum TTL can be specified at the object level.

# Cache Hit Ratio

The ratio of requests served from edge locations (rather than the origin) is known as the cache hit ratio.

The more requests from edge locations, the better the performance.The ratio is higher the better.

## Maximizing the Cache Hit Ratio

The following strategies can be set to maximize the cache hit ratio

1. Specifying the cache duration — Using Cache Control max-age directive. The shorter the duration, more frequently CF forwards another request to your origin to determine whether the object has changed and if so to get the latest origin version.
2. Caching based on the query string parameters — Maintaining a consistent naming convention in the query string can reduce multiple calls to the origin.
3. Caching based on the Cookie values — Creating a separate cache behaviors for static (.css files) and dynamic content (.js files) and configure CF to forward cookies only for the dynamic content (.js).
4. Caching based on Request Headers — Use only specific header for caching rather using all headers.
5. Remove Accept-Encoding Header — when compression is not needed.

# Content Invalidations

You can remove files from your origin that you no longer want to be included in your CloudFront distribution. However, CloudFront will continue to show viewers content from the edge cache until the files expire.

Cache invalidations do occur at the distribution level and applied to all edge locations involved in. If you want to remove a file right away, you must do one of the following:

1. Invalidate the file (See Figure 04)
2. Use file versioning — When you use versioning, different versions of a file have different names that you can use in your CloudFront distribution, to change which file is returned to viewers.

![](https://miro.medium.com/v2/resize:fit:875/1*Sj5DQB2DV0szgtuNuliiMg.png)

Figure 04 — Invalidating a File

# Alternate Domains and SSL

Once a CloudFront Distribution is created for an Origin, it will generate a CloudFront specific public DNS for you (**https:://xxxxxxx.cloudfront.net**). This is the “Default Domain” it creates for you (See Figure 05).

![](https://miro.medium.com/v2/resize:fit:875/1*0URAIaOWSPu-7p4DQS6_EQ.png)

Figure 05 — The Default Domain

If we are planning to use a CloudFront distribution with one of our production level domains (as Alternate Domains), then we need to use **AWS Certification Manager (ACM)** or any other SSL certificate provider to create a valid legitimate SSL certificate.

Make sure to use **us-east-1 (N.Virginia)** while creating the AWS Certificate when you use ACM (This is a restriction when you use ACM with a global service such as CF. However if you use ACM with other services such as ALB, you are required to generate the certificate in the same region of the service you are in).

You cannot use Self Signed Certificates with CloudFront and only certificates issued by a Trusted Certification Authority (CA) such as Verisign, Comodo, Digicert, Semantec or AWS ACM (Certificate Manager) are allowed.

There are two connections while creating a secure connection to multiple origins via CloudFront.

1. Client -> CloudFront
2. CloudFront → Origin (Native or Custom)

See Figure 06 for the above explanation.

![](https://miro.medium.com/v2/resize:fit:875/1*zwOJDra3DF8Vc1ey4qGX0w.png)

Figure 06 — Invoking multiple origin types via CloudFront Edges

# Securing the Origin via CloudFront

As you know, CloudFront Edge locations sits between the origin and the client. This architecture allows any user to access both the origin and the CF edge locations via public URLs. This is not secure and not a better practice.

Therefore, CloudFront can implement multiple ways to prevent this.

1. Restricting S3 origins using Origin Access Identities (OAI)s.
2. Restricting custom origins using custom headers
3. Restricting custom origins using firewalls
4. Geo-restrictions

## 1.0 Restricting S3 Access with Origin Access Identity (OAI)

To restrict access to content that you serve from Amazon S3 buckets, follow these steps.

1. Create a special CloudFront user called an **Origin Access Identity (OAI)** and associate it with your distribution.
2. Configure your S3 bucket permission so that CloudFront can use the OAI to access the files in your bucket and serve them to your users. Make sure that users can’t use a direct URL to the S3 bucket to access a file there.

> OAI is a type of identity, which can be associated with CF distributions. In this scenario CF becomes the OAI.

![](https://miro.medium.com/v2/resize:fit:875/1*4xktPd7MI-6-y9V-FHIC2g.png)

Figure 07 — Securing S3 via OAI

After you take these steps, users can only access your files through CloudFront and not directly from the S3 bucket. An AWS Account can have up to 100 CloudFront OAIs.

You may refer to my article on this topic [here](https://crishantha.medium.com/securing-s3-with-origin-access-identity-oai-via-cloudfront-147467eae8aa).

## 2.0 Restricting custom origins using custom headers

A customer header is injected at the edge location to the request and the origin will serve the request only if the custom header is present in the request (See Figure 08).

![](https://miro.medium.com/v2/resize:fit:811/1*GVNWhIsgfh89Ag1I90kteQ.png)

Figure 08 — Securing the custom origin with a custom header

## 3.0 Restricting custom origins using firewalls

If neither OAI nor custom headers are applied, you can use a firewall to secure the origins from malicious attacks. This is possible while restricting and specifying the access only to the edge location IP range (See Figure 09).

![](https://miro.medium.com/v2/resize:fit:875/1*yDK3J2Z32zUCyKwDWaZZwg.png)

Figure 09 — Securing the custom origin with a Web Application Firewall

## 4.0 Geo Restrictions

By default CF caches your data to all of the edge locations unless you specify specifically to a set of regions (North America, Europe, Asia, Middle East or Africa) using the list given while creating the CF distributions (See Figure 10).

![](https://miro.medium.com/v2/resize:fit:744/1*Qx9CdxTgz7q_x_U9BbFQ2w.png)

Figure 10 — Selecting your Edge location regions

If you need to restrict / allow the access to one single location, you can still achieve this by enabling the **Geo-restriction mode**. With CF Geo-restriction mode you can restrict / allow to a “**Country”** only. CF uses a **Geo-IP Database** for this purpose to track the user location.

However, if you need to restrict / allow access to any other attribute other than the “country”, you need to use a **3rd party Geo-location mechanism**. These **3rd party Geo-locations** are basically managed by a compute function, which is attached to a Geo-location database and other sources, which can give more information about the user.