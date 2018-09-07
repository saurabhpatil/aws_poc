import boto3


def save_file(bucket, file_name, data_bytes):
    s3 = boto3.client('s3')

    return s3.put_object(
        Bucket=bucket,
        Key=file_name,
        Body=data_bytes
    )


def get_file(bucket, file_name):
    s3 = boto3.client('s3')

    response = s3.get_object(
        Bucket=bucket,
        Key=file_name
    )

    return response['Body'].read()


def get_url(bucket, file_name):
    s3 = boto3.client('s3')

    params = {'Bucket': bucket, 'Key': file_name}
    return s3.generate_presigned_url('get_object', Params=params, ExpiresIn=expires)