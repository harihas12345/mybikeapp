import logging
import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

def generate_presigned_url(bucket_name, object_name, expiration_in_seconds):
    """
    Generates a presigned URL for an S3 object.

    Args:
        bucket_name (str): The name of the S3 bucket.
        object_name (str): The name of the S3 object.
        expiration_in_seconds (int): The number of seconds the presigned URL is valid for.

    Returns:
        dict: A dictionary containing the presigned URL, or None if an error occurred.
    """
    try:
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration_in_seconds,
            HttpMethod='GET'        
        )
        return {'presigned_url_str': presigned_url}
    except ClientError as e:
        logging.error(e)
        return None

def lambda_handler(event, context):
    bucket_name = "report-XXXXXXXXXXXX-YYYYMMDD"
    object_name = "report.html"
    expiration_in_seconds = 120

    response = generate_presigned_url(bucket_name, object_name, expiration_in_seconds)
    return response