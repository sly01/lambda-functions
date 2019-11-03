import json
import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    # TODO implement
    try:
        message = event['message']
        phone_number = event['phone_number']
        response = sns.publish(Message=message, PhoneNumber=phone_number)
        print(response)
        return {
            'statusCode': 200,
            'body': json.dumps("SMS has been sent successfully")
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 200,
            'body': json.dumps('There was an issue while sending sms')
        }