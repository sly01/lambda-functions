import json
import boto3

ec2 = boto3.resource('ec2')


def lambda_handler(event, context):
    # TODO implement
    instance_list = []
    for instance in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]):
        instance_info = instance.id+" - "+instance.public_ip_address
        instance_list.append(instance_info)
    instance_list = json.dumps(instance_list)
    return {
        'statusCode': 200,
        'body': instance_list
    }

