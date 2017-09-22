import Pyro4
import sys

class s3_client_process:
    def upload(self,aws_id,aws_key,aws_bucket,filenm,filepath):
        s3_server_process = Pyro4.Proxy("PYRONAME:s3_service_process")    # use name server object lookup uri shortcut
        print(s3_server_process.upload_file(aws_id,aws_key,aws_bucket,filenm,filepath))

c = s3_client_process.upload(aws_id,aws_key,aws_bucket,filenm,filepath)
result = "[" + c.result + "]"