import os
import boto3
from botocore.client import Config

class S3Client:
    def __init__(self, bucket_name=None, base_path="./"):
        self.bucket_name = bucket_name or os.getenv("S3_BUCKET_NAME")
        if not self.bucket_name:
            raise ValueError("bucket_name is None")

        self.base_path = os.path.abspath(base_path)
        self.s3 = boto3.client('s3',
            endpoint_url=os.getenv("S3_ENDPOINT_URL"),
            aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("S3_SECRET_KEY"),
            config=Config(signature_version="s3v4"),
        )

    def list(self, prefix=""):
        response = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix.rstrip("/"))
        return [obj['Key'] for obj in response.get('Contents', [])]

    def download(self, prefix):
        files = self.list(prefix)
        for s3_key in files:
            relative_path = os.path.relpath(s3_key, prefix).lstrip("/")
            local_path = os.path.join(self.base_path, prefix, relative_path)
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            self.s3.download_file(self.bucket_name, s3_key, local_path)
            print(f"Downloaded {s3_key} to {local_path}")

    def upload(self, subdir, prefix):
        dir_path = os.path.join(self.base_path, subdir)
        for root, _, files in os.walk(dir_path):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, self.base_path).lstrip("/")
                s3_key = os.path.join(prefix, relative_path).replace("\\", "/")
                self.s3.upload_file(local_path, self.bucket_name, s3_key)
                print(f"Uploaded {local_path} to s3://{self.bucket_name}/{s3_key}")