import sys
import tinys3

class aws_s3_upload:
    def __init__(self,aws_id,aws_key,aws_bucket):
        conn = tinys3.Connection(aws_id,aws_key,tls=True,endpoint='ap-southeast-1.amazonaws.com')
        f = open('/opt/aws_python/test.txt','rb')
        print conn.upload('test1.txt',f,aws_bucket)
        print conn.get('test1.txt',aws_bucket)

c = aws_s3_upload(aws_id,aws_key,aws_bucket)
result = "[" + c.result + "]"