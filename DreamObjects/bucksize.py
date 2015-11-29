#Programmatically calculate the total size of your bucket, by iterating over all your objects
import  boto

c = boto.connect_s3("your public key", "your secret key", host="objects.dreamhost.com")
b = c.get_bucket("your bucket name")

s = 0
for o in b.list():
    s += o.size

#show you the file size in MegaBytes if it’s too small to be legible in GigaBytes.
print str(s * 1.0 / 1024 ** 2) + " MB\n" 
#Shows you the file size in GigaBytes
print str(s * 1.0 / 1024 ** 3) + " GB"
