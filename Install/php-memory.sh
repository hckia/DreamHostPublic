#!/bin/bash
currentuser=$(whoami)
phpversion=$1
if [[ "$currentuser" == "root" ]]; then
        echo "Run this as the FTP user and not root"
        exit
fi
cd ~
if [[ ! "$phpversion" =~  ^[5]+(\.[3-9]+)?$ ]]; then
        echo "Please enter a version of PHP you wish to install this for. For example ./php-memory.sh 5.5"
        exit
fi
echo "Creating phprc directories for PHP $phpversion"
mkdir -p /home/$currentuser/.php/$phpversion
echo "adding information to phprc"
echo “memory_limit = 128M” >> /home/$currentuser/.php/$phpversion/phprc
echo “upload_max_filesize = 64M” >> /home/$currentuser/.php/$phpversion/phprc
echo “post_max_size = 64M” >> /home/$currentuser/.php/$phpversion/phprc
echo “max_execution_time = 500” >> /home/$currentuser/.php/$phpversion/phprc
echo “max_input_time = 500” >> /home/$currentuser/.php/$phpversion/phprc
echo "Killing all running PHP $phpversion processes"

killall php"${phpversion//.}".cgi
echo "PHP memory upgrade complete."
