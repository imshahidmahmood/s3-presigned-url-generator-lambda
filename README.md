# S3 Pre-Signed URL Generator Lambda

This AWS Lambda function generates pre-signed URLs for objects stored in Amazon S3. The function is highly configurable and accepts the S3 bucket name, object key, and expiration time as part of the JSON payload.

## Features

- **Dynamic S3 Bucket Name**: The bucket name can be specified in the request payload.
- **Dynamic Object Key**: Supports generating URLs for any object, including those in nested folders.
- **Custom Expiration**: Allows specifying the expiration time for the pre-signed URL in seconds.

## How It Works

This Lambda function uses the AWS SDK for Python (Boto3) to generate pre-signed URLs. The URL allows temporary access to an S3 object, and it can be used within the specified expiration time.

## Request Payload

The Lambda function expects a JSON payload with the following fields:

- `bucket_name` (string, required): The name of the S3 bucket.
- `object_key` (string, required): The key (path) of the S3 object.
- `expiration` (integer, optional): The expiration time for the pre-signed URL in seconds. Defaults to 3600 seconds (1 hour) if not provided.

### Example JSON Payload

```json
{
  "bucket_name": "your-bucket-name",
  "object_key": "folder/subfolder/your-s3-object-key",
  "expiration": 10
}
```
## Deployment

To deploy this Lambda function, you can use the AWS Management Console, AWS CLI, or Infrastructure as Code tools like AWS CloudFormation or Terraform.

## IAM Role Permissions
Ensure the Lambda function has the necessary IAM permissions to generate pre-signed URLs:

```json
{
    "Effect": "Allow",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::your-bucket-name/*"
}
```
Replace your-bucket-name with the actual bucket name or use a wildcard * to grant access to all buckets.

## Testing
### Using Postman
Method: POST
URL: https://your-api-id.execute-api.region.amazonaws.com/stage/resource
Body:
Choose raw.
Select JSON.
Provide the JSON payload as described above.

## Example Response

```json
{
  "url": "https://s3-region.amazonaws.com/your-bucket-name/folder/subfolder/your-s3-object-key?AWSAccessKeyId=XYZ&Signature=ABC&Expires=1234567890"
}

```
The response contains a pre-signed URL that allows access to the specified S3 object.

## Error Handling

The function returns the following status codes:

- 200 OK: Successfully generated the pre-signed URL.
- 400 Bad Request: Missing bucket_name or object_key, or invalid JSON payload.
- 500 Internal Server Error: An error occurred while generating the pre-signed URL.