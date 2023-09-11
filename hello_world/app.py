import json
import boto3

# Define the S3 bucket name where you want to upload data
s3_bucket_name = 'sqs-s3s'

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Print the received event
    print("Received event:", json.dumps(event))

    # Extract the message from the SQS event
    sqs_message = event['Records'][0]['body']

    # Define the S3 object key (file name)
    s3_object_key = 'your-prefix/' + sqs_message + '.txt'  # Modify as needed

    # Upload data to S3
    s3_client.put_object(
        Bucket=s3_bucket_name,
        Key=s3_object_key,
        Body=sqs_message
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Data uploaded to S3 successfully"
        })
    }