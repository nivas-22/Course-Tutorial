import boto3
import os

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=os.environ.get('REGION', 'ap-south-1'))

    action = event.get('action')  # e.g. "start", "stop", "terminate", "create"
    instance_id = os.environ.get('INSTANCE_ID')
    ami_id = os.environ.get('AMI_ID')

    if not action:
        return {'statusCode': 400, 'body': 'Missing action in event input'}

    try:
        if action == 'create':
            if not ami_id:
                return {'statusCode': 400, 'body': 'AMI_ID not set in env variables'}
            
            response = ec2.run_instances(
                ImageId=ami_id,
                InstanceType=os.environ.get('INSTANCE_TYPE', 't2.micro'),
                MinCount=1,
                MaxCount=1,
                SubnetId=os.environ.get('SUBNET_ID'),
                SecurityGroupIds=[os.environ.get('SECURITY_GROUP_ID')],
                TagSpecifications=[
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                            {'Key': 'Name', 'Value': os.environ.get('TAG_NAME', 'LaunchedByLambda')}
                        ]
                    }
                ]
            )
            new_id = response['Instances'][0]['InstanceId']
            print(f"Created EC2 instance: {new_id}")
            return {'statusCode': 200, 'body': f"Created instance: {new_id}"}

        elif action == 'start':
            ec2.start_instances(InstanceIds=[instance_id])
            return {'statusCode': 200, 'body': f"Started instance: {instance_id}"}

        elif action == 'stop':
            ec2.stop_instances(InstanceIds=[instance_id])
            return {'statusCode': 200, 'body': f"Stopped instance: {instance_id}"}

        elif action == 'terminate':
            ec2.terminate_instances(InstanceIds=[instance_id])
            return {'statusCode': 200, 'body': f"Terminated instance: {instance_id}"}

        else:
            return {'statusCode': 400, 'body': f"Unknown action: {action}"}

    except Exception as e:
        print(f"Error during {action}: {e}")
        return {'statusCode': 500, 'body': str(e)}
