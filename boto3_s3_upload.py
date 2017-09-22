import sys
import os
from boto3.s3.transfer import S3Transfer
import boto3

class boto3_s3_upload:
    def __init__(self,aws_id,aws_key,aws_bucket,filenm,filepath):
        client = boto3.client('s3', aws_access_key_id=aws_id,aws_secret_access_key=aws_key)
        os.chdir(filepath)
        transfer = S3Transfer(client)
        transfer.upload_file(filenm, aws_bucket, filenm)
        self.result="OK"

c = boto3_s3_upload(aws_id,aws_key,aws_bucket,filenm,filepath)
result = "[" + c.result + "]"