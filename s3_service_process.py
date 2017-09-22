import sys
import Pyro4
import tinys3

@Pyro4.expose
class S3ApiService(object):
    def upload_file(self,aws_id,aws_key,aws_bucket,filenm,filepath):
        conn = tinys3.Connection(aws_id,aws_key,tls=True,endpoint='ap-southeast-1.amazonaws.com')
        f = open("{0}/{1}".format(filepath,filenm),'rb')
        return conn.upload(filenm,f,aws_bucket)
        

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(S3ApiService)   # register the greeting maker as a Pyro object
ns.register("s3_service_process", uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls