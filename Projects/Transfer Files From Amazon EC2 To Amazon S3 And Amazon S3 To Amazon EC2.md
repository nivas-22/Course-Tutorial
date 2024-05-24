
**Overview**

The majority of contemporary IT companies now include cloud data storage as a fundamental component. Using Amazon S3, we can always upload and download files in a secure manner.

Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers.

Amazon S3 is an object storage service that stores data as objects in buckets. Amazon S3 provides administrative features that let you streamline, organize, and configure access to your data to meet your specific business, organizational, and compliance needs.

For a range of use cases, customers of all sizes and sectors can utilize Amazon S3 to store and protect any quantity of data, including big data analytics, enterprise applications, IoT devices, websites, mobile applications, backup & recovery, archiving, and data lakes.

**Benefits for uploading or Downloading files from S3:**

- Can upload or download data securely.
- Disaster Recovery
- Scalability
- Low cost
- High Availability

![](https://miro.medium.com/v2/resize:fit:875/1*8noFhENqYIZq1aocbvASGA.png)

**Prerequisites:**

1. S3 bucket to upload or download files.

2. EC2 Instance

3. Check if AWS CLI is installed or not in EC2 Instance.

4. IAM Profile/Role to attach EC2 instance

- Create a new IAM role for EC2 with below permissions or policy based on your use case.

[AmazonS3FullAccess](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAmazonS3FullAccess) (read and write permissions to S3)

[AmazonS3ReadOnlyAccess](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAmazonS3ReadOnlyAccess) (read permissions to S3)

**Uploading Files Amazon EC2 to Amazon S3:**

1. Attach the IAM Role to EC2 instance to get permission to access Amazon Bucket.

2. After attaching the role, Connect to the EC2 instances.

3. First Execute below command to check if AWS cli is instance or not.

- **aws — version**

![](https://miro.medium.com/v2/resize:fit:875/1*D_iRnUnyodFx87DlsOSB4Q.png)

aws cli version

4. Now try to list all the S3 buckets.

- **aws s3 ls**

![](https://miro.medium.com/v2/resize:fit:606/1*9JXaTZRhwma_Jr5lZuARzQ.png)

List all buckets

5. To upload files from EC2 to S3, use below command:

- **aws s3 cp file_name s3://bucket_name**

Or

- **aws s3 cp file_path s3://bucket_name/folder_name**

Eg:

![](https://miro.medium.com/v2/resize:fit:875/1*wkbK3rHy1mGcVgVqKEawcQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*1j4Innrfh7t2dHZE64kWmQ.png)

**Downloading Files from S3 to EC2:**

1. Try to list the S3 bucket from which you want to download the file.

- **aws s3 ls s3://bucket_name**

![](https://miro.medium.com/v2/resize:fit:875/1*6zfQt8IxbwCR9qzuH6Kg9w.png)

2. To upload files from S3 to EC2, use below command:

- **aws s3 cp s3://bucket_name file_name**

Or

- **aws s3 cp s3://bucket_name/folder_name file_path**

Eg:

![](https://miro.medium.com/v2/resize:fit:875/1*tQb5pcE4ik76ap143YsXCw.png)