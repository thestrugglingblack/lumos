import os
import boto3


def download_files():
    bucket = os.getenv('AWS_S3_BUCKET')
    client = boto3.client('s3')

    files = client.list_objects(Bucket=bucket)
    if 'Contents' in files:
        for file in files['Content']:
            file_name = file['Key']

            local_file_path = os.path.join('data', file_name)

            client.download_file(bucket, file_name, local_file_path)