# S3-Pre-signed-URL
Generates a temporary (pre-signed) URL for secure file access from S3.
pip install boto3
generate_presigned_url(
    bucket='my-bucket',
    key='secure/file.zip',
    expiration=600
)

