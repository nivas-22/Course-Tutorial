

![[Pasted image 20240224085046.png]]

When you create a record, you choose a routing policy, which determines how Amazon Route 53 responds to queries:

- **Simple routing policy** — Use for a single resource that performs a given function for your domain, for example, a web server that serves content for the example.com website.
- **Weighted routing policy** — Use to route traffic to multiple resources in proportions that you specify.
- **Latency routing policy** — Use when you have resources in multiple AWS Regions and you want to route traffic to the region that provides the best latency.
- **Failover routing policy** — Use when you want to configure active-passive failover.
- **Geolocation routing policy** — Use when you want to route traffic based on the location of your users.
- **Geoproximity routing policy** — Use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another.
- **Multivalue answer routing policy** — Use when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random.

## **Simple Routing Policy**

![](https://miro.medium.com/v2/resize:fit:875/0*FPFopCbPx1990nlR)

Amazon Route 53 — Simple Routing Policy

Simple Routing Policy is the most basic routing policy defined using an A record to resolve to a single resource always without any specific rules. For instance, a DNS record can be created to resolve the domain to an ALIAS record that routes the traffic to an ELB load balancing a set of EC2 instances.

## **Weighted Routing Policy**

![](https://miro.medium.com/v2/resize:fit:875/0*TrK0aNKVkXOqefT1)

Amazon Route 53 — Weighted Routing Policy

Weighted Routing Policy is used when there are multiple resources for the same functionality and the traffic needs to be split across the resources based on some predefined weights.

## **Latency Routing Policy**

![](https://miro.medium.com/v2/resize:fit:875/0*DRv3YAgbX2RhNYZm)

Amazon Route 53 — Latency Routing Policy

Latency Routing Policy is used when there are multiple resources for the same functionality and you want Route 53 to respond to DNS queries with answers that provide the best latency i.e. the region that will give the fastest response time.

## **Failover Routing Policy**

![](https://miro.medium.com/v2/resize:fit:875/0*MZY6EwU1i-tPKdzE)

Amazon Route 53 — Failover Routing Policy

Failover Routing Policy is used to create Active/Passive set-up such that one of the site is active and serve all the traffic while the other Disaster Recover (DR) site remains on the standby. Route 53 monitors the health of the primary site using the health check.

## **Geolocation Routing Policy**

![](https://miro.medium.com/v2/resize:fit:875/0*lC2uBYsexGfwVpwF)

Amazon Route 53 — Geolocation Routing Policy

Geolocation Routing Policy is used to route the traffic based on the geographic location from where the DNS query is originated. This policy allows to send the traffic to resources in the same region from where the request was originated i.e. it allows to have site affinity based on the location of the users.

## Geoproximity Routing Policy (Traffic Flow Only)

![](https://miro.medium.com/v2/resize:fit:754/1*6GcYFwCTWJ6096usx9l9gQ.png)

Amazon Route 53 — Geoproximity Routing Policy (source AWS docs)

Geoproximity routing lets Amazon Route 53 route traffic to your resources based on the geographic location of your users and your resources. You can also optionally choose to route more traffic or less to a given resource by specifying a value, known as a _bias_. A bias expands or shrinks the size of the geographic region from which traffic is routed to a resource. To use geoproximity routing, you must use Route 53.

## Multivalue Answer Routing Policy

![](https://miro.medium.com/v2/resize:fit:875/0*FPFopCbPx1990nlR)

Amazon Route 53 —Multivalue Answer Routing Policy

Multivalue answer Routing Policy is like Simple Routing Policy but it can return multiple values, such as IP addresses for your web servers, in response to DNS queries. You can specify multiple values for almost any record, but multivalue answer routing also lets you check the health of each resource, so Route 53 returns only values for healthy resources. ==It’s not a substitute for a load balancer, but the ability to return multiple health-checkable IP addresses is a way to use DNS to improve availability and load balancing.==

---
# **What is Route 53?**

Amazon Route 53 is not just a name; it's a highly available and scalable DNS web service by AWS. It transforms your user-friendly domain into an IP address, effortlessly directing traffic worldwide.

**Why Route 53?**

- **Highly available:** Redundancy across global data centers ensures non-stop availability.
    
- **Scalable:** Handles colossal DNS queries, perfect for your skyrocketing website.
    
- **Flexible:** Take control with routing options like weighted, geolocation, and failover routing.
    
- **Secure:** Defend against attacks with DNSSEC support.
    
- **Cost-effective:** Pay-as-you-go pricing keeps it budget-friendly.
    
- **Integrations:** Seamlessly syncs with AWS services, simplifying infrastructure management.
    

 **Key Features**

- **Domain Registration:** Grab new domains or transfer existing ones effortlessly.
    
- **DNS Record Mastery:** Manage A records, CNAME records, MX records, and more.
    
- **Routing Policies:** Tailor your website's traffic flow with precision.
    
- **Health Checks:** Keep tabs on your website's well-being.
    
- **Resolver Magic:** Resolve DNS queries for on-premises and VPC resources.
    
- **DNS Firewall:** Fortify your website against DNS-based attacks.
    

**Main Functions of Route 53**

1. **DNS Management:**
    
    - **Domain Registration:** Route 53 allows you to register new domain names or transfer existing ones. This involves the process of acquiring and managing domain names, associating them with the appropriate IP addresses, and configuring other DNS settings.
        
    - **DNS Hosting:** Route 53 provides a highly scalable and reliable DNS hosting service. It allows you to create and manage DNS records for your domain, such as A (Address) records, CNAME (Canonical Name) records, MX (Mail Exchange) records, and more.
        
2. **Traffic Management:**
    
    - **Routing Policies:** Route 53 offers various routing policies that enable you to control how traffic is distributed to your resources. These policies include:
        
        - **Simple Routing:** Directs traffic to a single resource.
            
        - **Weighted Routing:** Distributes traffic based on assigned weights to different resources.
            
        - **Latency-Based Routing:** Routes traffic to the resource with the lowest network latency for the end user.
            
        - **Geolocation-Based Routing:** Directs traffic based on the geographic location of the user.
            
        - **Multivalue Answer Routing:** Returns multiple IP addresses in response to DNS queries, and Route 53 randomly selects one of the IP addresses to return
            
        - **Failover Routing:** Redirects traffic from unhealthy resources to healthy ones.
            
    - **Health Checks:** Route 53 can perform health checks on your resources and automatically adjust routing based on the health of those resources.
        
3. **Availability Monitoring:**
    
    - **Health Checks:** Route 53 allows you to configure health checks for your resources. It regularly sends requests to your endpoints, such as web servers, to verify their availability and responsiveness.
        
    - **Failover:** Based on health check results, Route 53 can automatically reroute traffic from unhealthy resources to healthy resources, improving the overall availability and reliability of your applications.
        
4. **Domain Registration:**
    
    - **Domain Registration:** Route 53 provides the capability to register new domain names or transfer existing ones, allowing you to manage your domains within the AWS ecosystem.

These functions collectively make Amazon Route 53 a versatile and integral service for managing domains, DNS, and traffic routing in the AWS cloud environment.

**How DNS Works**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1702116923419/a5734986-bcef-46e7-bce0-9f7eefa390d7.png?auto=compress,format&format=webp)

**AWS DNS:**

1. Generic Level Domain- .com, .org, .net

2. Geographic Level Domain- .in, .us, .cn

**Functions of Route 53**

**A.** Register a domain.

**B.** As a DNS, it routes Internet traffic to the resources for your domain.

**C.** Check the health of your resources.

- Route 53 sends automated requests over the Internet to a resource ( can be a web server) to verify that the server is reachable, functional, or available.
    
- You can choose to receive notification when a resource becomes unavailable and choose to route Internet traffic away from unhealthy resources.
    

**D.** You can use Route 53 for any combination of these functions:

- For example, you can use Route 53 both to register your domain name and to route Internet traffic for the domain.
    
- or you can use Route 53 to route Internet traffic for a domain that you registered with another domain register.
    

**E.** When you register a domain with route 53, the service automatically makes itself the DNS service for the domain by doing the following: -

- It creates a hosted zone that has the same name as your domain.

**F.** It assigns a set of four name servers to the hosted zone, unique to the account

- when someone uses a browser to access your website, these name servers inform the browser where to find your resources, such as a web server or an Amazon S3 bucket.

**G.** It gets the name servers from the hosted zone and adds them to the domain.

**H.** AWS Supports: Generic top-level domain & Geographic top-level domain.

**Registering Domain with Route 53**

- You can register a domain with Route 53.
    
- If the TLD is included on the supported TLD list. If the TLD is not included, you can't register the domain with Route 53.
    

**Using Route 53 as your service**

- You can use Route 53 as the DNS service for any domain, even if the TLD for the domain is not included on the supported TLD list.
    
- Note: Each Amazon Route 53 account is limited to a maximum of 500 hosted zones and 10,000 resource records. You can increase this limit by requesting to AWS
    

**Steps to Configure Route 53**

- You need to register a domain. This can be route 53 or another DNS register, but then you. Connect to your domain name in that register to Route 53.
    
- Create a hosted zone on Route 53. This is done automatically if you register your domain using Route 53. - Inside the hosted zone, you need to create a record-set
    

**Delegate to Route - 53**

- This step connects everything and make it work
    
- Connect the domain name to the Route 53 hosted zone. This is called delegation.
    
- Update your domain registrar with the correct name servers for your Route 53 hosted zone.
    
- No other customer-hosted zone will share this delegation set with you.
    
- Doing this means the Route 53 DNS service will be serving traffic for the domain of the hosted zone.
    
- If you registered your domain with a different registrar, you need to configure the route 53 NS servers list in your registrar DNS database for your domain.
    

**If you are using another domain provider and you did all the changes:**

- When you migrate from one DNS provider to another for an existing domain, this change can take up to 48 hours to be effective.

- This is because name server DNS records are typically cached across the DNS system globally on the Internet for up to 48 hours (TTL) Periods.

**Transferring a domain to Route 53**

- You can transfer a domain to Route 53 if the TLD is included on the following list. - If the TLD is not included. You cannot transfer the domain to Route 53.

- For most, you need to get an authorization code from the current registrar to transfer a domain.

**Route 53 – Hosted Zones**

1. A route 53 hosted zone is a collection of records for a specified domain.
    
2. You create a hosted zone for a domain and then you create a record to tell the Domain Name System how you want traffic to be routed for that domain.
    
3. A hosted Zone is a container that holds information about how you want to route traffic for a domain and its subdomain.
    
4. You can create public (internet) hosted zones or private (Internet DNS) hosted zones.
    
5. For each public hosted zone that you create Amazon Route 53 automatically creates a name server (NS) record and a start of authority (SOA) record don't change these records.
    
6. Route 53 automatically creates a name server record with the same name as your hosted zone.
    
7. It lists the four name servers that are the authoritative name servers for your hosted zone.
    
8. Do not add, change or delete name servers in this record.
    
9. When you create a hosted zone, Amazon Route 53 automatically creates a name server ( NS ) records and a start of authority record (SOA) for the zone.
    
10. The NS record identifies the four name servers that you give to your registrar or your DNS service so that DNS queries are routed to Route 53 name servers.
    
11. Route 53 assigns a unique set of four name servers (known collectively as a delegation set) to each hosted zone that you create Example:
    

ns - 1337.awsdns-39.com

ns-895.awsdns-47.net

ns-428.awsdns-53.org

ns-1597.awsdns-07-co.uk

**Route 53 – Authoritative DNS**

1. Once you update the Route 53 NS setting with your domain registrar to include the Route 53 name servers, route 53 will be responsible for responding to DNS queries for the hosted zone.
    
2. This is true whether you have a functioning website or not.
    
3. Route 53 will respond with information about the hosted zone whenever someone types the associated domain name in a web browser.
    
4. You can create more than one hosted zone with the same name and add different records to each hosted zone.
    
5. Route 53 assigns 4 name servers to every hosted zone.
    
6. The name servers are different for each of them.
    
7. When you update your registrar's name server records, be careful to use the route 53 name servers for the correct hosted zone- the one that contains the records that you want route 53 to use when responding to queries for your domain.
    
8. Route 53 never returns values for records in other hosted zones which you have the same name
    

**Route 53 hosted zone default entries**

Inside the hosted zone, by default, you have two entries.
1. NS Entry: Contains the unique sets of name servers for this hosted zone.
2. SOA Entry: Contains information about the hosted zone.

**_If you are currently using another DNS service and you want to migrate to Amazon Route 53._**

1. Start by creating a hosted zone.
    
2. Route 53 automatically assigns the delegation sets the four name servers to your hosted zone.
    

To ensure that the DNS routes queries for your domain to the route 53 name servers.

- Update your registrar's or your DNS service's NS records for the domain to replace the current name servers with the names of the four Route 53 name servers for your hosted zone.
    
- The method that you use to update the name server records depends on which registrar or DNS service you are using.
    
- Some registers only allow you to specify name servers using IP addresses. They don't allow you to specify fully qualified domain names.
    
- If your registrar requires the use of IP addresses. You can get the IP addresses for your name servers using the dig utility (for Mac, Linux) and nslookup (go to the cmd and type this command for Windows)
    

**Transferring a domain between accounts within AWS.**

- Transferring a domain to a different AWS account.
    
- If you registered a domain using one AWS account and you want to transfer the domain to another AWS account, You can do so by contacting the AWS support center and requesting the transfer.
    

**Migrating a hosted zone to a different account.**

- If you are using Route 53 as the DNS service for the domain, Route 53 does not transfer the hosted zone when you transfer a domain to a different AWS account.
    
- If a domain registration is associated with one account and the corresponding hosted zone is associated with another account, neither domain registration nor DNS functionality is affected.
    
- The only effect is that you will need to sign in to the Route 53 console using one account to see the domain and sign in using the other account to see the hosted zone.
    

**Supported DNS record types by Route 53**

1. A record: Address record
    
    - Maps Domain name to IP address -  IN A 5.5.5.5
    
2. AAAA Record - IPv6 Address record maps domain name to an IPv6 address
    
    -  IN AAAA 2002: b768: 1
    
3. CNAME Record (Canonical Record): Maps an alias to a hostname
    
    - Web IN CNAME 
    
4. NS Record: Name server Record - used delegating zone to a nameserver xyz.com IN NS nsl.xyz.com
    
5. SOA Record: Start of Authority Record
    
6. MX Record: Mail exchange - defined where to deliver mail for user@ a domain name.
    
7. NS records define which name server is authoritative to a particular zone or domain name and point you to other DNS servers.
    
8. A/AAAA are a called host records like business cards.
    
9. CNAME is an alternative record or an alias for another record. Helpful in redirection or if you want to hide details about your actual servers from the users
    

**State of Authority (SOA)**

The State of Authority (SOA) record in DNS (including in Amazon Route 53) provides essential information about the domain and the zone. It is a critical record in a DNS zone file and includes details about the domain's primary authoritative DNS server, the email of the domain administrator, domain serial number (used for versioning), timers for refreshing and expiring the zone data, and more.

Here is an example of an SOA record:


```
example.com.   SOA   ns1.example.com. admin.example.com. (
                    2023112201 ; serial number
                    7200       ; refresh period in seconds
                    3600       ; retry period in seconds
                    1209600    ; expire time in seconds
                    86400      ; minimum TTL (Time to Live) in seconds
                  )
```

Explanation of the fields:

**example.com** : The domain to which this SOA record belongs.
    
- **SOA**: The record type, indicating that this is a State of Authority record.
    
- **ns1.example.com** : The primary authoritative DNS server for the domain.
    
- http://admin.example.com: The email address of the domain administrator.
    
- **2023112201**: The serial number. It typically increases each time the zone file is updated.
    
- **7200**: Refresh period in seconds. This is how often secondary servers check with the primary server for updates.
    
- **3600**: Retry period in seconds. If a secondary server can't contact the primary server during the refresh period, it retries after this interval.
    
- **1209600**: Expire time in seconds. If a secondary server can't refresh the zone within this period, it considers its data stale.
    
- **86400**: Minimum TTL (Time to Live) in seconds. This is the default TTL for the domain, affecting how long DNS records are cached by other DNS servers.
    

The SOA record is crucial for maintaining the consistency and accuracy of the DNS information within a zone. It serves as a sort of "control panel" for the zone, and changes to the zone often involve updating the SOA record. In Amazon Route 53, you don't typically need to manually edit the SOA record, as the service manages it automatically. It's generated and updated based on changes you make to the hosted zone through the Route 53 console, API, or other management tools.

**CNAME Record Type**

- A CNAME value element is the same format as a domain name
    
- The DNS protocol does not allow you to create a CNAME record for the top node of a DNS namespace, also known as the zone apex (or root domain)
    
- Example. If you register the DNS name [xyz.com](http://xyz.com/), the zone apex is [xyz.com](http://xyz.com/). You cannot create a. CNAME record for [xyz.com](http://xyz.com/).
    
- However, you can create CNAME records for [www.xyz.com](http://www.xyz.com/)., [support.xyz.com](http://support.xyz.com/) and so on
    
- In addition, if you create a CNAME record for a subdomain. You cannot create any other records for that subdomain. For example, if you create a CNAME record for [www.xyz.com](http://www.xyz.com/) You cannot create any other records for which the value of the name field is [www.xyz.com](http://www.xyz.com/).
    

**What is Alias Record**

An ALIAS record is a virtual host record type that is used to point one domain name to another one, almost the same as a CNAME. The important difference is that ALIAS can coexist with other records on that name. An ALIAS record can also be used if you wish to alias the root domain to another service (which you cannot do with a CNAME record).

**Route-53: Routing Policies**

When you create a Record, you choose a routing policy, which determines how Amazon Route 53 responds to queries.

There are 7 routing policies.

1. Simple Routing (Default)
    
2. Failover Routing
    
3. Geo Location Routing
    
4. Latency Based Routing
    
5. Multi-Value Answer Routing
    
6. Weighted Routing
    

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1702120207693/a31e2ddf-9b4f-40fb-9561-529cd220df40.png?auto=compress,format&format=webp)

**A. Simple Routing:** At the heart of Route 53 lies simplicity. The Simple Routing policy directs traffic to a single resource, making it perfect for straightforward setups. Imagine the elegance of seamlessly connecting users to your primary server:

```
example.com.   A   192.0.2.1
```

**B. Failover Routing:**

Active Server ----If active server fails ---->> Passive Server

- Here the Requests come to the active server until it got failed, If it got failed then the request will transfer to the passive servers.
    
- Failover routing lets you route traffic to a resource when the resource is healthy if the main resource is not healthy, then route traffic to a different resource.
    
- The Primary and secondary records can route traffic to anything from an Amazon S3 bucket that is configured as a website to a complex tree of records
    
- Failover routing policy is applicable for Public hosted zones only
    

```
example.com.   A   192.0.2.1 (Primary)
               A   203.0.113.1 (Secondary)
```

**C. Geo Location Routing:**

Geo Location routing lets you choose the resources that serve your traffic based on the geographic location of your users i.e. the location that DNS queries originate from. e.g. You may have a presence in Europe and Asia. Now you want users in Asia to be served in Asia and those in Europe to be served by servers in Europe.

**Benefits**:

- You can localize your content and present some or all of your website in the language of your users.
    
- You can also use geolocation routing to restrict distribution of content to only the locations in which you have distribution rights.
    
- you can specify geographic locations by continent, by country or by state in the United States.
    
- If you create separate records for overlapping geographic regions e.g. one record for north America and one for Canada- priority goes to the smallest geographic region (Canada).
    
- Geolocation works by mapping IP address to locations. However, some IP address are not mapped to geographic location.


```
example.com.   A   192.0.2.1 (US)
               A   203.0.113.1 (Europe)
```

**D.** **Latency Based Routing:**

- If your application is hosted in multiple amazon EC2 regions, you can improve performance for users by serving their request from the Amazon EC2 region that provide the lowest latency.
    
- To use latency-based routing, you create latency records for your resources in multiple EC2 regions.
    
- When Amazon route 53 receives a DNS Query for your domain or subdomain:
    
    - It determines which amazon EC region you have created latency record for
        
    - Determine which regions gives lowest latency to users
        
    - Then select a latency record for that region
        
        - For e.g.:
            
            - Suppose you have ELB in US east and in Asia Pacific (Mumbai) region.
                
            - You created a latency record for each load balancer
                
            - Here's what happens when a user in London enters the name of your domain in a browser.
                
            - DNS routes the request to a Route 53 Name server.
                
            - Route 53 refers to its data on latency between London and the Mumbai region and between London and the North Virginia.
                
            - If latency is lower between London and North Virginia, route 53 respond to the query with the IP address for the North Virginia LB
                

**E. Multivalue Answer Routing Policy:**

- Use when you route 53 to respond to DNS queries with up to 8 healthy record selected at Random.
    
- Multi value answer routing let you configure Amazon route 53 to return Multiple Values. Such as IP addressed for your webserver, in response to DNS queries you can specify multiple values for almost any record, but multivalued answer routing also lets you check the health of each resource. So, route 53 returns only values for healthy resources. It's not a substitute for a load balancer. but the ability to return multiple health checkable IP addresses is a way to use DNS to improve availability and load balancing

```
example.com.   A   192.0.2.1
               A   203.0.113.1
               A   198.51.100.1
```

**F. Weighted Routing Policy:**

- Weighted Routing Policy let you associate multiple resources with a single domain name or subdomain name, and choose how much traffic is routed to each resource.
    
- This can be useful for a variety of purposes, including load balancing and testing new versions of software.
    
- Weights can be assigning any number from 1 to 255.
    
- Weighted routing policy can be applied when there is multiple resource that perform the same function for e.g. webserver serving the same website.
    
- To configure weighted routing. You create records that have the same name and type for each of your resources.
    
    - Amazon route 53 sends traffic to a resource based on the weight that you assign to the record as a proportion of the total weight for all records in the group.
        
    - for example: suppose [www.xyz.com](http://www.xyz.com/) has three resource record sets with weights of 1(20%), 1 (20%), and 3 (60%) (sum=5)
        
    - On average, route 53 selects each of the first two resource record set one-fifth of the time, and returns the third resource record set three-fifth of the time.


```
example.com.   A   192.0.2.1   (Weight: 10)
               A   203.0.113.1 (Weight: 5)
```

These routing policies provide flexibility in managing traffic distribution based on various factors such as location, latency, health of resources, and more. The choice of which policy to use depends on your specific requirements and the desired behavior for your application or service.

**Conclusion ✨**

As we draw the curtains on this exploration, Amazon Route 53's routing policies emerge as the virtuoso of DNS management and traffic orchestration. Whether you're seeking simplicity, performance optimization, or fortification against failures, Route 53 offers a rich ensemble of tools to elevate your digital symphony.

So, step onto the conductor's podium, harness the power of Route 53, and conduct a masterpiece in the grand concert hall of the internet! 🌐🎶