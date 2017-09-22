import tinys3
import sys

AWS_ACCESS_KEY_ID = sys.argv[1]
AWS_SECRET_ACCESS_KEY = sys.argv[2]
bucket_name = sys.argv[3]

conn = tinys3.Connection(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,tls=True,endpoint='ap-southeast-1.amazonaws.com')

f = open('test.txt','rb')
print conn.upload('test1.txt',f,bucket_name)
print conn.get('test1.txt',bucket_name)