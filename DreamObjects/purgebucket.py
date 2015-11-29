#WARNING: Below is a script to remove content from a bucket. Proceed with caution.
#(change "path/to/directory/to/delete" to "" to delete all files in a bucket):
import boto

c = boto.connect_s3("publickey", "secretkey", host="objects.dreamhost.com")
b = c.get_bucket("bucketname", validate=True)

l = [o for o in b.list(prefix="path/to/directory/to/delete")] #to purge entire buket leave the prefix variable blank
while len(l):
    s = l[0:1000]
    len(l)
    rs = b.delete_keys(s)
    if len(s) == len(rs.deleted):
        l = l[1000:]

