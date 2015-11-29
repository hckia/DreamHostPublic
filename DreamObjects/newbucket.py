#NOTE: Replace public key and secret key with those found in your panel ( panel > CloudServices > DreamObjects )
#Change the permissions of the file by running the following command…
#chmod 700 create_bucket.py (remove everything before the next line)
#!/usr/bin/env python
import boto, argparse, os

c = boto.connect_s3("public key", "secret key", host="objects.dreamhost.com")

parser = argparse.ArgumentParser()

parser.add_argument('-b', '--bucket', required=True, help="bucket name to be created")

args = parser.parse_args()

bucket = args.bucket

create_bucket = c.create_bucket(bucket)

#We are now ready to create our first bucket from the command line! Type
# --> ./create_bucket.py -b AnAwesomeDreamObjectsBucketName <---
#You can see if this worked by checking your DreamObjects page.

