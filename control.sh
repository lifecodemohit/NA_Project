#!/bin/bash

# sudo nohup tcpdump -vvvn -i any dst port 2400 -w con_log
# gnome-terminal -e "sudo tcpdump -vvvn -i any dst port 2400 | python ./packfire.py"
a=`cat Documents/data.txt | wc -l`
a=`expr $a - 3`
sudo tcpdump -vvvn -c 1 -i any dst net 192.168.53.36 -w con_log &
sleep 2 
sudo python ./packfire.py
sudo rm -rf Documents/data.txt
#sudo cp con_log con1_log
#k=`ps aux | grep 'tcpdump' | awk '{print $2}' | head -1`
#sudo kill $k
#sudo tcpdump -vvvn -i any dst port 2400 -w - | tee con_log | tcpdump -r - &
#sshpass -p "mohit1995" scp -r lifecodemohit@192.168.53.36:/home/lifecodemohit/con14_log ./
#ps aux | awk '/tcpdump/ {print "sudo kill -INT "$2}' | bash
#k=`ps aux | grep 'tcpdump' | awk '{print $2}' | head -1`
#sudo kill $k
#tcpdump -w - | tee somefile | tcpdump -r