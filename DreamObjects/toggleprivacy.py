import boto
c = boto.connect_s3("ACCESSKEY", "SECRETKEY", host="objects.dreamhost.com")
b = c.get_bucket("BUCKETNAME")

#Change all objects in a bucket to public / private
for o in b.list():
	o.set_acl('public-read')

#Instead of "public-read", you can use "private" to set all objects private.
