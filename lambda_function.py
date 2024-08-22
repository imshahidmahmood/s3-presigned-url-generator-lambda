import json
import boto3

def lambda_handler(event, context):

    s3_client = boto3.client('s3')
    
    # Extract bucket name, object key, and expiration time from the JSON payload in the event
    try:
        payload = json.loads(event['body'])
        bucket_name = payload.get('bucket_name')
        object_key = payload.get('object_key')
        expiration = payload.get('expiration', 3600)  # Default expiration time: 3600 seconds (1 hour)
    except (json.JSONDecodeError, TypeError) as e:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid JSON payload')
        }

    if not bucket_name or not object_key:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: bucket_name and object_key are required')
        }
    
    try:
        # Generate the pre-signed URL
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_key},
            ExpiresIn=expiration
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'url': presigned_url})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error generating pre-signed URL: {str(e)}')
        }

