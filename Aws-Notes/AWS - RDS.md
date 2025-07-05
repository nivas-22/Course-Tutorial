
Database - Collection of data & handle the data

RDS is makes it easy to setup, scale, operate a relational database in the cloud. It Provides cost efficient and resizable capacity while automating time-consuming administration tasks such as hardware provisioning, database setups, data backups and Patching.

- Structured and Schema based storage
- Physical and Logical Schema (Tables, views and integrity constraints)

1. Relational - Relationship between Tables.
2. Schema - structure in and between tables of data

**On-Premises : Buy , setup, deploy and operate - Man effort**

Key Terms:

- Mastering replica and Cross-Region Replica
- Snapshots
- clustering
- clone
- restore from s3

## AWS Pre-defined Databases:

1. MySQL
2. postgres SQL
3. SQL server
4. ORACLE
5. Amazon Aurora
6. mariaBD

![[Pasted image 20240130205131.png]]

RDS - Structured - My SQL
Unstructured - redshift
semi-structured - dynamo DB

>[!Question]- Why shouldn't you run DB's on EC2 ?
>1. Admin Overhead
>2. Backup  & DR
>3. Ec2 is running in a single AZ.
>4. will miss out feature on AWS DB products.
>5. Skills and setup time to monitor
>6. performance will be slower than AWS Options.

## RDS DB Instance :

- DB connects with a CNAME - (Canonical NAME). RDS uses a standard DB engines.
- The DB can be Optimized for :  **db.m5 general, db.r5 memory, db.t3 burst**
- The storage can be allocated with SSD or magnetic.
- Billing is per instance and hourly rate for that compute. You billed for storage allocated.

---
## <mark style="background: #FF5582A6;">Migrating DB from EC2 to RDS :</mark>

- Step1: Get the dump of your existing DB on EC2
- Step2: Connect to your RDS DB Instance
- Step3: Migrate the DB Dump that you have taken in step1 to RDS
- Step4: Verify the data if available.

---
## RDS High Availability (Multi AZ):

1. RDS Access only via Database CNAME. The CNAME will point at the Primary Instance. You Can't access standby replica for any reason via RDS.
2. The Standby Replica cannot be used for Extra Capacity.
3. Synchronous Replication.

>[!Notes]- Points to Remember
>
>1. Multi AZ feature is not free tier, Extra Infrastructure for Standby.Generally, twice the price.
>2. The Standby replica cannot be accessed directly unless a failure occurs.
>3. Failover is Highly available, not Fault tolerant.
>4. same region
>5. Backups taken from standby (removes performance impacts)
>6. AZ Outage, Primary failure, manual failover, instance type change and software patching.

----
# AWS RDS Masterclass Commands

## Databases on EC2 Instance - Demo
### Begin Configuration :
```bash
sudo su -
yum -y install mariadb105-server.x86_64
systemctl enable mariadb
systemctl start mariadb

```
### Set Environmental Variables
```bash
DBName=ec2db
DBPassword=admin123456
DBRootPassword=admin123456
DBUser=ec2dbuser
```
### Database Setup on EC2 Instance:
```bash
echo "CREATE DATABASE ${DBName};" >> /tmp/db.setup
echo "CREATE USER '${DBUser}' IDENTIFIED BY '${DBPassword}';" >> /tmp/db.setup
echo "GRANT ALL PRIVILEGES ON *.* TO '${DBUser}'@'%';" >> /tmp/db.setup
echo "FLUSH PRIVILEGES;" >> /tmp/db.setup
mysqladmin -u root password "${DBRootPassword}"
mysql -u root --password="${DBRootPassword}" < /tmp/db.setup
rm /tmp/db.setup
```
### Adding some dummy data to the Database inside EC2 Instance:
```bash
mysql -u root --password="${DBRootPassword}"
USE ec2db;
CREATE TABLE table1 (id INT, name VARCHAR(45));
INSERT INTO table1 VALUES(1, 'Virat'), (2, 'Sachin'), (3, 'Dhoni'), (4, 'ABD');
SELECT * FROM table1;
```
### Migration of Database in EC2 Instance to RDS Database:
```bash
mysqldump -u root -p ec2db > ec2db.sql
mysql -h <replace-rds-end-point-here> -P 3306 -u rdsuser -p rdsdb < ec2db.sql
mysql -h <replace-rds-end-point-here> -P 3306 -u rdsuser -p
USE rdsdb
SELECT * FROM table1;
```

---
### Output :

![[Pasted image 20240201122003.png]]

---
### RDS Backups:

- First Snap is Full size of consumed data.
- Manual Snapshots will remain in your AWS account even after the life of the snapshot. These need to be deleted manually.
- **Automatic Snapshots**
- Every 5 Min translation logs are saved to S3. A database can then be restored to a 5 min snapshot in time.
- Automatic cleanups can be anywhere from 0 to 35 days.
- When you delete the database, they can retained but they will expire based on their retention period.

---
## RDS Read - Replicas:

1. Kept in sync using asynchronous replication
2. It is written fully to the primary instance. Once its stored-on disk, it is then pushed to the replica. This means there could be a small lag. These can be created in the same region or a different region. This is a cross-region replication.

---
## RDS Read - Replica - Performance! 

1. 5 Direct Read-replicas per DB instances.
2. Each of these provides an additional instance of read performance
3. This allows  you to scale out read operations for an instance
4. Read-Replicas can chain, but lag will become a problem
5. Can provide global performance improvements.

---

Notes:

Data Identifier - demo-rds-database
Master username - rdsuser
master pass - admin123456

advance configuration :

1. DB name - rdsdb
2. 
