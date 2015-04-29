#!/bin/bash
#a=`cat Documents/data.txt | wc -l`
#a=`expr $a - 2`
#sudo tcpdump -vvvn -i any -c 2 dst port 2400 -w con_log &
sudo tcpdump -vvvn -i any -c 2 dst port 2400 -w con_log &
#sudo tcpdump -vvvn -i any dst port 2400 -w - | tee con_log | tcpdump -r - &
