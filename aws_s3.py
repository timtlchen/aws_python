import boto
import boto.s3
import sys, getopt
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = sys.argv[1]
AWS_SECRET_ACCESS_KEY = sys.argv[2]
bucket_name = sys.argv[3]

#bucket_name = AWS_ACCESS_KEY_ID.lower() + '-dump'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)


bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)

testfile = "test.txt"
print("Uploading file to Amazon S3 bucket")

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


k = Key(bucket)
k.key = 'my test file'
k.set_contents_from_filename(testfile, cb=percent_cb, num_cb=10)