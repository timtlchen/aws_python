import sys
import os
import tinys3

class aws_s3_upload:
    def __init__(self,aws_id,aws_key,aws_bucket,filenm,filepath):
        conn = tinys3.Connection(aws_id,aws_key,tls=True,endpoint='ap-southeast-1.amazonaws.com')
        os.chdir(filepath)
        f = open(filenm,'rb')
        conn.upload(filenm,f,bucket=aws_bucket,close=True,expires=3600)
        #conn.get(filenm,aws_bucket)        
        return "OK"

c = aws_s3_upload(aws_id,aws_key,aws_bucket,filenm,filepath)
result = "[" + c.result + "]"