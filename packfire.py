import os

dfile = open("data.txt","r")
# line  = dfile.readline()
arr = []

for line in dfile:
	arr.append(line)

arr.pop(len(arr)-1)

for i in xrange(2,len(arr)):	
	sip,sport,tip,tport,protcl,packs = map(str,arr[i].split(";"))
	# print sip,sport,tip,tport,protcl,packs

	protcl = protcl.lower()
	packs = str(int(packs)-28)		# Accounting for the space occupied by the IPv4 header
	data = int(packs) * "x"			# Arbitrary data

	cmd = "sudo sendip -p ipv4 -is " + sip
	if protcl == "tcp":
		cmd += (" -p tcp -ts " + sport + " -td " + tport)
	elif protcl == "udp":
		cmd += (" -p udp -us " + sport + " -ud " + tport)
	cmd += (" -d " + data + " -v "+ tip)

	print cmd
	os.system(cmd)