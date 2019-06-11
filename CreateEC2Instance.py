import json
import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    # TODO implement
    try:
        instances = ec2.create_instances(
            ImageId='ami-0c6b1d09930fac512',
            InstanceType='t2.micro',
            KeyName='aws-eb',
            MaxCount=1,
            MinCount=1,
            SecurityGroupIds = ['sg-0855b142d52729a79']
        )
        instance = instances[0]
        #instance.wait_until_running()
        #instance.load()
        #info = "Instance is successfully created and public ip is " + instance.public_ip_address
        info = "Instance is successfully created and instance id is "+ instance.id
        return {
            'statusCode': 200,
            'body': json.dumps(info)
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 200,
            'body': "There was an issue while creating machine"
        }

