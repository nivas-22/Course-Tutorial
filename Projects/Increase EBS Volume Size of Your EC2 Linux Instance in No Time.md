
**Overview:**

If you are in charge of the technical infrastructure of your company, you will probably need to make changes at some time to accommodate increasing needs. You can extend with the changing needs of the industry frequently means adjusting a company’s technical infrastructure. The good news is that infrastructure adaptation has never been simpler thanks to cloud computing. Resources can now be added or removed rapidly based on the situation.

This was a laborious, time-consuming job that came with extra overhead expenses under the conventional on-premise computing strategy. Fortunately, scaling your resources has never been simpler thanks to cloud technologies. With a few clicks, you can quickly add or remove resources from your cloud infrastructure.

For instance, you can quickly change the size of your EBS volumes on AWS to suit your needs.

**Amazon EC2:**

An EC2 instance is a virtual server. It allows AWS customers to request and set up a computer server in the AWS cloud.

**EBS Volume:**

Virtual data is hosted in segments on an Elastic Block Storage (EBS) Volume. It is similar to a storage drive that can hold different sized data files.

**Architecture:**

![](https://miro.medium.com/v2/resize:fit:875/1*8Hp2m_3Q5MN1TVRzT_WTcA.png)

**Steps to Increase Volume Size of EC2 Linux Instance:**

**a.** **Snapshot Backup:**

Before Modifying the Volume size, we take Snapshot backup. In case if something goes wrong while modifying the volume. We can create new volume out of that snapshot and attach it to the instance.

i. Navigate to EC2 Console.

ii. Click on Volume.

iii. Select the Volume for which you want to increase the size and Click on Actions and Select Create Snapshots.

iv. Provide Description and Add tags and Click on Create Snapshots.

![](https://miro.medium.com/v2/resize:fit:875/1*WTPXEKrL1XCHb_hvbp_8kA.png)

v. Once Snapshot is Available. We can modify the Volume Size

**b.** **Modify Volume Size:**

i. Check filesystem and partition before modifying the size.

![](https://miro.medium.com/v2/resize:fit:875/1*q3p9GhK3utm4Y5hLpFbfFQ.png)

![](https://miro.medium.com/v2/resize:fit:791/1*uUkJKzDUrLLyLeahhHtgWw.png)

ii. Navigate to EC2 Console.

![](https://miro.medium.com/v2/resize:fit:338/1*RbT0y1IRlbgJc3dOF7Sr5w.png)

iii. Select the instance for which you want to increase the volume size. Click on storage tab and click on volume id.

![](https://miro.medium.com/v2/resize:fit:875/1*e4-01A4yIGqP4er0W6CiWw.png)

iv. It redirects to Volume Console.

v. Click on Actions and Select Modify Volume.

![](https://miro.medium.com/v2/resize:fit:875/1*4d_R3dbN5EgtPK5V3HxKcw.png)

vi. Change the size according to your needs and Click on Modify

Eg:

If volume size is 8gb, you want to modify to 30gb.Change the size to 30 gib.

![](https://miro.medium.com/v2/resize:fit:838/1*XzL9EuEGOnVjbF26pkdlug.png)

![](https://miro.medium.com/v2/resize:fit:875/1*kHTM8I8UPFfmHg_gF3TloA.png)

**c.** **Extend File System:**

i. Navigate to EC2 Instance Console.

ii. Connect to the Instance.

iii. Execute below command to list all the filesystems mounted on your disk.

df -h

iv. To lists information about all available or the specified block devices, use below command.

- **sudo growpart /dev/nvme0n1 1**

![](https://miro.medium.com/v2/resize:fit:819/1*D1a2uouxibAplGVKOw20ag.png)

v. To increase the partition size, use the growpart command.

- **sudo growpart /dev/nvme0n1 1**

![](https://miro.medium.com/v2/resize:fit:875/1*pPrcb_8Rwu-OyBEk2DssNg.png)

vi. to extend a file system mounted on `/`, use the following command

- **sudo xfs_growfs -d /**

![](https://miro.medium.com/v2/resize:fit:875/1*Fo2s6xO2AyJo5U5_zG4iMg.png)

vii. Now you can see file system has been extended.

![](https://miro.medium.com/v2/resize:fit:875/1*fo9jH3cqSbGqrindipFFSA.png)