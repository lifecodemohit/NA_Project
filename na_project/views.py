from django.shortcuts import render
from django.http import HttpResponse
from na_project.models import *
import subprocess
import os

# Create your views here.
def index(request) :
	context = ""
	if request.method == 'POST':
		s_info = source_info(ip=request.POST.get('s_ip'),ip_yn=request.POST.get('s_ip_yn'),ip_v=request.POST.get('s_ip_v'),port=request.POST.get('s_port'),port_yn=request.POST.get('s_port_yn'),port_v=request.POST.get('s_port_v'))
		t_info = target_info(ip=request.POST.get('t_ip'),ip_yn=request.POST.get('t_ip_yn'),ip_v=request.POST.get('t_ip_v'),port=request.POST.get('t_port'),port_yn=request.POST.get('t_port_yn'),port_v=request.POST.get('t_port_v'))
		info = information(protocol=request.POST.get('protocol'),protocol_yn=request.POST.get('protocol_yn'),protocol_v=request.POST.get('protocol_v'),packet_size=request.POST.get('packet_size'),doc_file = request.FILES['documentFile'])
		s_info.save()
		t_info.save()
		info.save()
		# file = open("data.txt", "a")
		# file.write(request.POST.get('s_ip')+";"+request.POST.get('s_ip_yn')+";"+request.POST.get('s_ip_v')+";"+request.POST.get('s_port')+";"+request.POST.get('s_port_yn')+";"+request.POST.get('s_port_v')+";"+request.POST.get('t_ip')+";"+request.POST.get('t_ip_yn')+";"+request.POST.get('t_ip_v')+";"+request.POST.get('t_port')+";"+request.POST.get('t_port_yn')+";"+request.POST.get('t_port_v')+";"+request.POST.get('protocol')+";"+request.POST.get('protocol_yn')+";"+request.POST.get('protocol_v')+";"+request.POST.get('packet_size')+"\n")
		# file.close()	
		os.system('sudo bash ./control.sh')
		# subprocess.call(['./control.sh'])
		list1 = ["Hello"]
		context = {'list1':list1};
		return render(request, 'index.html', context) 
	else:
		list1 = ["Bie"]
		#os.system('sudo bash ./tcpdump.sh')
		context = {'list1':list1};
		return render(request, 'index.html', context)