#this script is to migrate from one bucket to another
import boto
c = boto.connect_s3("ACCESSKEY", "SECRETKEY", host="objects.dreamhost.com")
b = c.get_bucket("BUCKETNAME")

sourcebucket = c.get_bucket('SOURCEBUCKET')
destbucket = c.get_bucket('DESTINATIONBUCKET')

sourcebucketlist = [o for o in sourcebucket.list(prefix="path/to/source/directory")]

while len(sourcebucketlist):
	newfilename = sourcebucketlist.name.replace("path/to/source/directory", "path/to/destination/directory")
	destbucket.copy_key(newfilename, sourcebucket.name, sourcebucketlist[0].name)
	len(sourcebucketlist)
	sourcebucketlist = sourcebucketlist[1:]
