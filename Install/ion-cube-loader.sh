#!/bin/bash
currentuser=$(whoami)
phpversion=$1
if [[ "$currentuser" == "root" ]]; then
        echo "Run this as the FTP user and not root"
        exit
fi
cd ~
if [[ ! "$phpversion" =~  ^[5]+(\.[3-9]+)?$ ]]; then
        echo "Please enter a version of PHP you wish to install this for. For example ./ion-cube-loader.sh 5.4"
        exit
fi
echo "Downloading & unpacking ioncube"
mkdir ioncube
cd ioncube
wget http://downloads2.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.bz2
tar jxf ioncube_loaders_lin_x86-64.tar.bz2 -C $HOME
rm ioncube_loaders_lin_x86-64.tar.bz2
echo "Creating phprc directories for PHP $phpversion"
mkdir -p /home/$currentuser/.php/$phpversion
echo "Appedning zend_extension = /home/$currentuser/ioncube/ioncube_loader_lin_$phpversion.so to phprc file. A phprc file will be created if none exists."
echo "zend_extension = /home/$currentuser/ioncube/ioncube_loader_lin_$phpversion.so" >> /home/$currentuser/.php/$phpversion/phprc
echo "Killing all running PHP $phpversion processes"

killall php"${phpversion//.}".cgi
