#!/bin/bash

mkdir dumpdir
date_of_dump=$(date +"%m%d%Y")

for i in /home/USERNAME/*
do
        if [ -d "$i" ] || [$i -ne "logs"]
        then
                tar --create --file=${i}${date_of_dump}.tar.gz $i
                mv ${i}${date_of_dump}.tar.gz /home/USERNAME/dumpdir
        fi
done

cd dumpdir

mysqldump --opt --user=DBUSER --password=DBUSERPASS --host=DBHOST  > $date_of_dump"_backup".sql

cd ..

boto-rsync -a'ACCESSKEY' -s'SECRETKEY' --endpoint='objects.dreamhost.com' --workers=0 $'/home/USERNAME/dumpdir' $'s3\072//BUCKETNAME/dumpdir'

rm -fr dumpdir
