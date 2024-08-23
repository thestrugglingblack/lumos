import os
import boto3


def download_file(file_name):
    bucket = os.getenv('AWS_S3_BUCKET')

    client = boto3.client('s3')
    client.download_file(bucket, file_name, 'data')
