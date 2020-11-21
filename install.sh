#!/bin/bash

#-------------------------
#Spps Setup Script
#-------------------------

dnf_var=$(which dnf)
aptget_var=$(which apt-get)
python3_var=$(which python3)
pip3_var=$(which pip3)

if [ "$EUID" -ne 0 ]; then
	printf "Please run as root\n"
	exit;
fi

if [ ! -z $python3_var ] && [ ! -z $pip3_var ]; then
	printf "### install dependencies for sppscan\n"
	pip3 install -r requirements.txt
	
elif [ ! -z $dnf_var ]; then
	printf "### installing python3 and python3-pip ... please wait\n"
	dnf install python3 python3-pip -y
	printf "### install dependencies for sppscan\n"
	pip3 install -r requirements.txt

elif [ ! -z $aptget_var ]; then
	printf "### installing python3 and python3-pip ... please wait\n"
	apt-get install python3 python3-pip -y
	printf "### install dependencies for sppscan\n"
	pip3 install -r requirements.txt

else
	printf "Could not install python3 or python3-pip\nPlease install manually\n"

fi

if [ ! -e "./sppscan" ]; then
	ln -s "./src/spps.py" "./sppscan"
fi

printf "\n\n# Start Simple Python Port Scanner with ./sppscan\n"
