#!/bin/bash

if [ "$1" == "" ]
then
echo "You dumbass forgot to provide ip address"
echo "Ex usage: ./ipsweep.sh 192.168.0"

else
for ip in `seq 1 254`; do
    ping $1.$ip -c 1 | grep "64 bytes" | cut -d " " -f 4| tr -d ":" &
done
fi
