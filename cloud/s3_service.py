import boto3

class S3Service:
    def __init__(self, bucket_name):
        self._s3 = boto3.client('s3')
        self._bucket_name = bucket_name


    def upload(self, image_filename, bucket_filename):
        self._s3.upload_file(image_filename, self._bucket_name, bucket_filename)
