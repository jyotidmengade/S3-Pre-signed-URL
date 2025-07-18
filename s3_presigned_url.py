import boto3

def generate_presigned_url(bucket, key, expiration=3600):
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket, 'Key': key}, ExpiresIn=expiration)
    print(f"Presigned URL: {url}")

# generate_presigned_url('my-bucket', 'uploads/sample.txt')
