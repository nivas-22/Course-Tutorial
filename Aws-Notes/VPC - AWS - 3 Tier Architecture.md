
![[Pasted image 20240126192104.png]]


>[!Important]- Why we kept Application Servers In Public ? 
>
> 1. In Real-time, We have  Interact with API's calling SAAS Package 
> 2. Download Package from internet

>[!FAQ]- How to Access AWS Services within VPC ?
>1. VPC Endpoint Gateway - This service makes Privately access the servers, but within VPC AZ.
>2. Using NAT Gateway - This also makes us to connect the servers but high charge for DATA Processing.

***
## **36 Regions with 102 Availability Zones** 

1 Region == Multiple AZ's


##  Aws Account --> 5 VPC's --> **A region can only have one default VPC**. Although you can have up to five VPCs in a region, only the initial VPC that AWS creates for you can be the default VPC.

## Subnets  ---> 200 per VPC 


----
#### Routing  VS Firewall :

- Routing is how to route the Packet from source to destination.
- Firewall means whether the packet is allow to go destination, after it reaches the destination.
- It is all about allow the traffic inside the interface or stop the interface

****

**Route Table** : 
		1. Contains rules to route traffic from IN/Out of Subnets.
		2. Main Route Table is at VPC level
		3. Custom Route table at Subnet level
**Subnets** : 

1. Public Subnet : 
     *  Has route for internet.
     * Instances with Public Ip can communicate to Internet.
     * Ex : NAT, Web servers, Load Balancer

| **Destination** | **Target** |
| ---- | ---- |
| 10.10.0.0/16 | local |
| 0.0.0.0/0 | igw |

2. Private Subnet:
     * No Route to Internet
     * Instance receive private Ips
     * Use NAT for Instances to have Internet Access
     * Ex : Database, App Server
     
| **Destination** | **Target** |
| ---- | ---- |
| 10.10.0.0/16 | local |

## **Security Groups** :

1. Security Groups
2. Network Access control list (NACL)


SG : 
1. It is most basic Native and Important Firewall for EC2 Instances (ENI) Elastic Network Interface.
2.  It has Inbound and Outbound rules
3. It has only ALLOW rules. Does not support BLOCK rules
4. Authorizes traffic from both IP4 and IP6 traffic
5. Single Security group can be attached to Multiple instances
6. Single instances can have Multiple SG.

NACL : Network Access Control List 

1. works at subnet level - Automatically Applied to all Instances.
2. Contains allow and deny rules - Rules are Numbered.
3. Rules are Evaluated in the order of rule numbers (1 to 32766)
4. Default NACL allows both Inbound and Outbound traffic
5.  **NACL are a great way of blocking a specific IP at subnet level**

NACL rules :

![[Pasted image 20240127201553.png]]


| **Security Group** | **NACL** |
| :--: | :--: |
| 1. Implement at EC2 level | 1. Implemented at Subnet level |
| 2.  Supports only Allow rules | 2. Supports only Allow and Deny rules |
| 3. Stateful - Return traffic is Allowed | 3. stateless - Return traffic is needs to be authorised in Outbound rules |

-----------------------

# **NAT Gateway** :

1. AWS Managed NAT - Network Address Translation, Higher Bandwidth, Better Availability, no admin
2. Pay by the Hour for usage and Bandwidth (Based on sending data via Nat gateway)
3. 5 Gbps of Bandwidth with Auto Scaling up to 100 Gbps.
4. No Security groups. - Bcoz it maintained by AWS.
5. NACL at Subnet level applies to NAT gateway.
6. Supported protocols : TCP, UDP, and ICMP
7. use ports 1024 - 65535 for Outbound connection.
8. For Outbound Internet access, NAT is connected with Public subnet so that it can communicate with the internet.
9. NAT gateway should be allocated elastic IP.

![[Pasted image 20240127210714.png]]

                     [This Architecture is wrong]

# High Availability - NAT Gateway:

![[Pasted image 20240127210828.png]]


## Nat Instance :

1. Must be in Public Subnet
2. Must Have Public  or Elastic IP
3. Should be launched using AWS Provided NAT AMIs
4. **Disable Source/Destination check
5. Security group inbound rules to allow https/ or ICMP (ping) traffic from private subnets.
![[Pasted image 20240220191737.png]]