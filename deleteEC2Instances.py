import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # TODO implement
    try:
        response = ec2.terminate_instances(
            InstanceIds=[
                event['instanceID']
                ]
            )
        return {
            'statusCode': 200,
            'body': json.dumps("Machine termination successful")
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 200,
            'body': json.dumps('There was an issue while removing instance')
        }

