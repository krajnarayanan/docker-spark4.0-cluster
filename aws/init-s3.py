import boto3
import os

# Create an S3 client that connects to LocalStack
s3_client = boto3.client(
    's3',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    endpoint_url='http://localhost:4566' # Must use the Docker service name
)

def create_bucket(bucket_name):
    """Creates an S3 bucket if it doesn't already exist."""
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' already exists.")
    except Exception:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created.")

if __name__ == '__main__':
    create_bucket('data-bucket-1')
    create_bucket('data-bucket-2')
    s3_client.upload_file("./data/AAPL.csv", "data-bucket-1", "aapl" )
