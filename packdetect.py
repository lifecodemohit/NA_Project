import os

dfile = open("data.txt","r")

line = map(str,dfile.readline().split(";"))
val = map(str,dfile.readline().split(";"))
k=0

cmd = "tcpdump -r con_log -n "

if line[0] == "Yes" or line[1] == "Yes":
	cmd += "src "
	if line[0] == "Yes":
		cmd += ("net " + val[k])
		k+=1
	if line[1] == "Yes":
		cmd += ("port " + val[k])
		k+=1

if line[2] == "Yes" or line[3] == "Yes":		
	cmd += "dst "
	if line[2] == "Yes":
		cmd += ("net " + val[k])
		k+=1
	if line[3] == "Yes":
		cmd += ("port " + val[k])
		k+=1

if line[4] == "Yes":
	cmd += val[k]
	k+=1

print cmd