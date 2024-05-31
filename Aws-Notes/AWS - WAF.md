

![[Pasted image 20240302073837.png]]

![[Pasted image 20240302074138.png]]


# Introduction

Web applications have become central to business operations, education, communication, and entertainment. However, as their usage has grown, so has the interest of malicious actors looking to exploit vulnerabilities for various nefarious purposes. Protecting these applications is paramount, and one effective tool in the cybersecurity arsenal is a Web Application Firewall (WAF). This article delves into building a basic WAF on Amazon Web Services (AWS), a leading cloud service provider, to shield your web applications from common threats.

# Understanding AWS WAF

When it comes to web application security, AWS WAF stands out as a strong line of defense, designed to safeguard web applications and APIs from common web exploits that could compromise security, affect availability, or consume excessive resources. AWS WAF, integrated within the Amazon Web Services ecosystem, offers a customizable, scalable solution to combat cyber threats.

## What is AWS WAF?

AWS WAF is a cloud-based web application firewall that allows you to create customized rules to block, allow, or monitor (count) web requests based on conditions you define. These conditions include IP addresses, HTTP headers, HTTP body, URI strings, SQL injection, and cross-site scripting (XSS) among others. By defining web ACLs (Access Control Lists), AWS WAF provides fine-grained control over the traffic reaching your applications, ensuring that only legitimate requests are processed.

## Key Features and Capabilities

- **Custom Rules and Filters:** AWS WAF enables the creation of custom rules to target specific attack patterns. This includes rules to filter out SQL injection attacks, XSS attacks, and rules based on geographic location, IP addresses, and more. The flexibility of these rules allows for tailored security postures that match the unique requirements of each application.
- **Managed Rules:** For users who prefer a more hands-off approach or need a quick setup, AWS WAF offers managed rule groups provided by AWS or AWS Marketplace sellers. These rule groups are maintained and updated to protect against common threats and vulnerabilities, such as OWASP Top 10 security risks, without the need for user intervention.
- **Rate-Based Rules:** AWS WAF supports rate-based rules that help mitigate Distributed Denial of Service (DDoS) attacks. These rules track the number of requests from a single IP address over a specified period, allowing you to block or flag IPs that exceed acceptable limits, thus protecting your application from flood attacks.
- **Integration with AWS Services:** AWS WAF seamlessly integrates with other AWS services such as Amazon CloudFront, Amazon API Gateway, and Application Load Balancers. This integration allows for a centralized approach to manage security across multiple entry points to your applications, enhancing your overall security posture with minimal architectural changes.
- **Real-Time Visibility and Monitoring:** With AWS WAF, you gain real-time insights into web traffic and threat patterns. Integration with Amazon CloudWatch provides detailed monitoring and alerts, while AWS WAF logs (available through Amazon Kinesis Firehose) offer comprehensive data on web requests, allowing for thorough traffic analysis and timely response to potential threats.
- **Cost-Effective Pricing:** AWS WAF follows a pay-as-you-go pricing model, where you pay only for what you use based on the number of rules deployed and the number of web requests your application receives. This flexible pricing model makes AWS WAF accessible for businesses of all sizes, ensuring enterprise-level security without significant upfront investment.

## The Importance of AWS WAF in Modern Web Security

The digital landscape is fraught with security challenges, from sophisticated cyber-attacks to automated bots attempting to exploit vulnerabilities. In this context, AWS WAF serves as a important tool in the cybersecurity toolkit, offering strong protection that adapts to the changing tactics of threat actors. By providing the means to inspect and filter incoming traffic, AWS WAF plays a pivotal role in maintaining the integrity, availability, and confidentiality of web applications.

Furthermore, the integration of AWS WAF with other AWS services amplifies its effectiveness, enabling a holistic security strategy that leverages the scalability and flexibility of cloud computing. Whether you’re protecting a simple website or a complex, distributed web application, AWS WAF provides the necessary controls to secure your online presence against an array of web-based threats.

Understanding AWS WAF and its capabilities is the first step towards creating a secure online environment for your applications. With its customizable rules, integration options, and cost-effective pricing, AWS WAF empowers developers and security professionals alike to build resilience against cyber threats, ensuring a safe and reliable user experience.

# Setting Up AWS WAF

Securing your web applications with AWS WAF involves a series of strategic steps designed to tailor the firewall’s protective measures to your specific needs. This section walks you through the setup process, from creating a Web ACL to defining rules and monitoring traffic, ensuring a comprehensive defense strategy against web threats.

## Step 1: Create a Web ACL

The cornerstone of AWS WAF configuration is the Web Access Control List (Web ACL). This acts as a container for the rules that you will define to dictate how incoming traffic should be managed.

- **Navigation:** Begin by logging into the AWS Management Console and navigating to the AWS WAF & Shield service.
- **Web ACL Creation:** Select “Create web ACL” and provide a name that reflects the purpose or the resource it will protect. Choose the AWS resource you want to associate with the Web ACL, such as an Amazon CloudFront distribution or an Application Load Balancer.
- **Configure Settings:** Set the default action to either block or allow requests that do not match any rules. This is a crucial decision as it defines the default stance of your firewall.

## Step 2: Define Conditions

Conditions are the building blocks of AWS WAF rules. They specify the criteria that AWS WAF uses to inspect web requests.

- **IP Conditions:** Create conditions to filter traffic based on IP addresses or ranges. This is particularly useful for allowing traffic from known safe sources or blocking known malicious sources.
- **SQL Injection and XSS Conditions:** Use AWS WAF’s predefined filters to protect against common threats like SQL injection and XSS. These conditions inspect parts of the request, such as the body or query string, for malicious patterns.
- **String and Regex Conditions:** For more granular control, you can define string conditions and regex patterns to match specific content within requests, allowing for the blocking of requests containing suspicious or unauthorized content.

## Step 3: Create Rules

With conditions in place, the next step is to create rules that determine how requests matching these conditions should be handled.

- **Rule Configuration:** Each rule can include one or more conditions. When a request meets all the conditions in a rule, AWS WAF can either allow, block, or count the request. Counting is useful for testing the impact of a rule before enforcing it.
- **Managed Rules:** For efficiency, consider adding managed rules to your Web ACL. AWS provides a variety of managed rule groups, such as the OWASP Top 10 security risks, that are maintained and updated regularly, offering protection against a wide range of vulnerabilities.

## Step 4: Add Rules to the Web ACL

After defining your rules, the next step is to add them to your Web ACL and prioritize them.

- **Rule Priority:** Rules within a Web ACL are evaluated in order based on priority. It’s important to strategically order the rules to make sure that the most important evaluations occur first.
- **Associating Rules:** Add your custom and managed rules to the Web ACL. You can also specify a default action (allow or block) that AWS WAF should apply to requests that do not match any of the rules.

## Step 5: Monitor and Maintain

The final step involves monitoring the traffic and the performance of your AWS WAF rules.

- **AWS CloudWatch Integration:** Utilize AWS CloudWatch to set up custom alarms and monitor metrics related to the traffic passing through your WAF. This can help identify anomalies or spikes in traffic that could indicate a potential attack.
- **Logging:** Enable AWS WAF logging to record data about the traffic that is inspected. Logs can be sent to Amazon S3, Amazon CloudWatch Logs, or Amazon Kinesis Data Firehose, providing valuable insights for further analysis or compliance purposes.
- **Regular Reviews:** Cyber threats are constantly evolving, necessitating regular reviews and updates of your WAF configurations. Stay informed about new vulnerabilities and adjust your rules as needed to maintain optimal protection.

# Implementing Basic Protection Strategies

In the world of web application security, implementing basic protection strategies is crucial. AWS WAF provides a range of options to safeguard your applications against common threats. In this section, we’ll explore how to protect against SQL Injection, mitigate Cross-Site Scripting (XSS) attacks, and use rate-based blocking to defend against DDoS attacks, including practical examples of how to set up these protections.

## Protecting Against SQL Injection

SQL injection is a widespread attack where attackers insert malicious SQL code into web inputs to manipulate your database. AWS WAF can help prevent these attacks by inspecting elements like query strings, headers, and body.

Here’s an example of how you could set up a rule in AWS WAF to block common SQL injection patterns:

import boto3  
  
client = boto3.client('wafv2')  
  
response = client.create_rule(  
    Name='SQLInjectionRule',  
    MetricName='SQLInjectionRuleMetric',  
    DefaultAction={'Type': 'BLOCK'},  
    VisibilityConfig={  
        'SampledRequestsEnabled': True,  
        'CloudWatchMetricsEnabled': True,  
        'MetricName': 'SQLInjectionRuleMetric'  
    },  
    Statement={  
        'SqliMatchStatement': {  
            'FieldToMatch': {'AllQueryArguments': {}},  
            'TextTransformations': [{  
                'Priority': 0,  
                'Type': 'URL_DECODE'  
            }]  
        }  
    }  
)

In this example, we create a rule named `SQLInjectionRule` that blocks requests matching SQL injection patterns found in all query arguments.

## Mitigating Cross-Site Scripting (XSS) Attacks

XSS attacks involve injecting malicious scripts into otherwise benign and trusted websites. AWS WAF helps combat XSS by inspecting the parts of requests that could contain scripts.

Below is a sample rule to mitigate XSS attacks:

response = client.create_rule(  
    Name='XSSAttackRule',  
    MetricName='XSSAttackRuleMetric',  
    DefaultAction={'Type': 'BLOCK'},  
    VisibilityConfig={  
        'SampledRequestsEnabled': True,  
        'CloudWatchMetricsEnabled': True,  
        'MetricName': 'XSSAttackRuleMetric'  
    },  
    Statement={  
        'XssMatchStatement': {  
            'FieldToMatch': {'AllQueryArguments': {}},  
            'TextTransformations': [{  
                'Priority': 0,  
                'Type': 'URL_DECODE'  
            }]  
        }  
    }  
)

This `XSSAttackRule` inspects all query arguments for XSS patterns and blocks requests that match these patterns.

## Rate-Based Blocking

Rate-based rules help protect against DDoS attacks and brute force login attempts by tracking the number of requests from an IP address over a specified period.

Here’s how to set up a rate-based rule:

response = client.create_rate_based_rule(  
    Name='RateLimitRule',  
    MetricName='RateLimitRuleMetric',  
    RateKey='IP',  
    RateLimit=2000, # Number of requests per 5-minute period per IP  
    MatchPredicates=[],  
    ChangeToken='YOUR_CHANGE_TOKEN'  
)

This `RateLimitRule` limits the number of requests from an IP address to 2000 every 5 minutes, effectively blocking IPs that exceed this threshold.


----

_[Highly Configurable and Scalable, Cloud Native web application Layer-7 firewall giving you the first line of defense.]_

There are **many security threats** that exist today in a typical enterprise distributed application.

1. **DDoS**: Flood Attacks (SYN Floods, UDP Floods, ICMP Floods, HTTP Floods, DNS Query Floods), Reflection Attacks
2. **Application Vulnerabilities**: SQL Injections, Cross Site Scripting (XSS), Open Web Application Security Project (OWASP), Common Vulnerabilities and Exposures (CVE)
3. **Bad Bots**: Crawlers, Content Scrapers, Scanners and Probes

Out of these, AWS WAF can be used to handle security threats such as SQL injections, Cross Site Scripting (XSS) in a typical web application.

The web application HTTP requests, can be routed via AWS WAF and then will be forwarded to either one of the AWS services.

1. AWS CloudFront (A Global Service)
2. AWS API Gateway (A Regional Service)
3. AWS Application Load Balancer (A Regional Service)

Logging and Monitoring of WAF are handled by _Kinesis Firehose_ and _CloudWatch_ respectively.

![](https://miro.medium.com/v2/resize:fit:736/1*lEIhC0e8x4KG6jNV1Iwp9w.png)

Figure 1 — WAF Filtering and Monitoring HTTP requests

## Web ACL

When WAF associating any of the above three AWS services, it associates with a Web ACL. A Web ACL is a fundamental component of WAF, which defines a set of rules for any of these services (See Figure 2).

![](https://miro.medium.com/v2/resize:fit:656/1*Z_xmcMCqzL-7sBTHxuhmgQ.png)

Figure 2 — Conditions, Rules and Web ACLs

As mentioned, a Web ACL is a collection of **rules**. A rule is a collection of **conditions** (See Figure 3).

![](https://miro.medium.com/v2/resize:fit:564/1*O7QNy7ITJ05hit0LC4Ko5g.png)

Figure 3- WAF with Web ACLs

## How to create a Web ACL in WAF?

In order to demonstrate the WAF capability, it is always good to go through a simple scenario that can showcase its capability. Here, I am going to block a CloudFront distribution, which I created sometime ago. So, if you are trying this out, please make sure you have one of the services (CloudFront, API Gateway or ALB) is created already before trying this out.

> P.Note: You can try out one of my [blogs](https://medium.com/@crishantha/connecting-your-website-securely-via-aws-route-53-cloudfront-and-acm-eb442ede7ef5) get an understanding of how to create your own CloudFront distribution on AWS [3]. Probably that can help you if you are not familiar with CloudFront.

**Task 1:** **Describe a Web ACL and associate it to AWS resources**

Go to AWS WAF → Web ACLs → Click _Create Web ACL_ button (See Figure 4).

![](https://miro.medium.com/v2/resize:fit:875/1*OXsf8gv0V9XLp2HDepAj8w.png)

Figure 4

Give a name to Web ACL and associate a Resource Type to it. Here we are associate a CloudFront distribution (See Figure 5), which I have already created before. You can attach this to not only CloudFront but ALB and API Gateway as well.

P.Note: If you select a CloudFront, then you need to select “Global” as the scope since it is a Global service. If you select either ALB ot API Gateway, you will have to select a region where the associate resource is located.

![](https://miro.medium.com/v2/resize:fit:875/1*H88jObqrxkD-bAqWFtn0Uw.png)

Figure 5

Click _Add AWS Resources_ button to associate the CloudFront Distribution that you created before (See Figure 6).

![](https://miro.medium.com/v2/resize:fit:875/1*8-fU0Wam5joByYxF3m_FrQ.png)

Figure 6

Click _Next_ button and you will get another page to add your rules to Web ACL. We will skip this for the moment allowing us to do it at a later stage.

Select _Allow_ for Web ACL Action as well.

(P.Note: Web ACL Action defines what you are going to do when the defined rule is active)

Leave _Set Rule Priority_ as it is and click _Next._

Leave _Configure Metrics_ and click _Next_.

Finally review your selections and click _Create Web ACL_ button.

The above will create a Web ACL without any rules. You can go back to Web ACL link and you will see the below. Make sure not to select a region and select _Global (CloudFront)_ in the top drop down to see your created Web ACL (See Figure 7).

![](https://miro.medium.com/v2/resize:fit:875/1*jUV7RQs3-HHwE6eQfDCfxA.png)

Figure 7

However, even if you see a created Web ACL, CloudFront propagation for this update will take a bit of time. You can see it if you visit the CloudFront console page. Give a little bit of time finish the CloudFront propagation before you start the next step.

**Task 2: Add a Condition to block my IP address**

Go to AWS WAF → IP Sets → Click _Create IP Set_ button.

Select IPV4 and give your IP address with /32 as the postfix. If you are not sure how to get your network’s public IP, you may type “What is my IP” on Google. It is that simple (See Figure 8).

![](https://miro.medium.com/v2/resize:fit:829/1*dZZBJmH8UYPjX97JW5Y-Dg.png)

Figure 8

**Task 3: Add a Rule to the created condition**

In order to create a rule, you need to create a Rule Group.

Go to AWS WAF → Rule Group → Click _Create Rule Groups_ button (See Figure 9)

![](https://miro.medium.com/v2/resize:fit:875/1*Fv0C1WNCaBzQwnp9qiaK5g.png)

Figure 9

Click _Next →_ Click _Add Rule_ button → Set the following parameters to create a Rule

Rule Name → _MyRule_

If a Request → Select _Matches the requirement_

Statement (Inspect)→ Select _Originates from an IP Address In_

Statement (IP Set) → Select the IP Set that you created in Task 2

Action → Select _Block_

Click _Next_

Select the _Rule Priority_. This is not required here since you have only one rule.

Finally review your selections and click _Create Rule Group_ to confirm your rule settings.

**Task 4: Add the created Rule Group / Rule to the Web ACL**

Go to AWS WAF → Web ACL → Select the _Web ACL_ that you have created → Click _Rules_ tab (See Figure 10).

![](https://miro.medium.com/v2/resize:fit:875/1*1wjd-2A0ki8eci-tinmKUw.png)

Figure 10

You can see the Web ACL still does not have its rules attached.

Click _Add Rules_ button drop down → Select _Add my own rules and rule groups_

![](https://miro.medium.com/v2/resize:fit:875/1*8LVSopZu3yvbHd91UgvhAA.png)

Figure 11

Give a name for the rule that you are specifying here (See Figure 11).

[P.Note: I strongly feel the new WAF UI has some issues related its fields. This is a good example of having to define Rule name twice. Once under the Rules Group and once under Web ACL rule attachments.]

Select the Rules Group that you created from the drop down and click _Add rule_ button and then click _Save_.

Now you can see the added rule is attached to the Web ACL.

Now it is time to browse the web URL that you have blocked for your IP. If all fine, it will be similar to below screen (See Figure 12).

![](https://miro.medium.com/v2/resize:fit:875/1*V1zejuXE8q1qqvFiqkOhrQ.png)

Figure 12

If you want to remove the blocking, you can go to the Web ACL and delete the related Rule and try the web link again. After a few refresh attempts, you will get your site back.
# Conclusion

Securing web applications is important in today’s digital landscape, and AWS WAF offers a powerful tool to protect against common web threats. By understanding AWS WAF’s capabilities, setting it up effectively, and implementing basic protection strategies, you can safeguard your applications from attacks such as SQL injections, XSS, and DDoS. Regularly revisiting and updating your WAF configurations is essential to adapt to evolving threats. Embrace AWS WAF to make sure your web applications remain secure, reliable, and trustworthy.



![image](https://github.com/nivas-22/Course-Tutorial/assets/122221537/6b0ca5e1-4dd5-49a7-ae45-fa569d11c564)
