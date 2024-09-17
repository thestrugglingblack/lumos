import os
import boto3
from dotenv import load_dotenv

cwd = os.getcwd()

env_path = os.path.join(cwd, '.env')
load_dotenv(env_path)
bucket = os.getenv('AWS_S3_BUCKET')

def download_files():
    print('Downloading files...in download-file')
    # Create the 'data/' directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
        print(f"Directory data/ created.")
    else:
        print(f"Directory data/ already exists.")

    # Initialize the S3 client
    client = boto3.client('s3')

    # List objects in the specified S3 bucket
    files = client.list_objects_v2(Bucket=bucket)

    # Check if the bucket contains any files
    if 'Contents' in files:
        for file in files['Contents']:
            file_name = file['Key']

            # Check if the file is a CSV
            if file_name.endswith('.csv'):
                # Create the full path for the file in the 'data/' directory
                fp = os.path.join('data', os.path.basename(file_name))

                print(f'Downloading {file_name} to {fp}')

                # Download the file from S3 to the 'data/' directory
                client.download_file(bucket, file_name, fp)
                print(f'File {file_name} downloaded successfully.')

    else:
        print(f"No files found in bucket {bucket}.")