#first a new library must be implemented
#pip install FileChunkIO
#then create an EXECUTABLE python file (permissions 700) with the following code... (remove everything before the line)
#!/usr/bin/env python
import math, os
import boto, args.publickey
from filechunkio import FileChunkIO

#Connect to S3
c = boto.connect_s3("publickey", "secretkey", host="objects.dreamhost.com")
b = c.get_bucket("bucketname")

#Add parse arguments
parser.add_argument('-sp','--sourcepath',required=True, help="source path to sync to DreamObjects bucket")

sourcepath = args.sourcepath

#file info
source_path ='sourcepath'
source_size = os.stat(source_path).st_size

#Create a multipart upload request
mp = b.initiate_multipart_upload(os.path.basename(source_path))

#set a chunk size (feel free to change this)
chunk_size = 100000
chunk_count = int(math.ceil(source_size / float(chunk_size)))

#send the file parts using FileChunkIO to create a file-like object
#that points to a certain byte range within the original file. We set
#bytes to never exceed the original file size.
for i in range(chunk_count):
        offset = chunk_size * i
        bytes = min(chunk_size, source_size - offset)
        with FileChunkIO(source_path, 'r', offset=offset,bytes=bytes) as fp:
           mp.upload_part_from_file(fp,part_num=i +1)

#Finish the upload
mp.complete_upload()

#from the command line, type ./chunk_test.py -sp fileYouWish to upload.

