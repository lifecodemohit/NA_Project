from django.db import models
#python manage.py sqlclear na_project | ./manage.py dbshell
# Create your models here.
class source_info(models.Model):
	ip = models.CharField(max_length=30)
	ip_yn = models.CharField(max_length=30)
	ip_v = models.CharField(max_length=30)
	port = models.CharField(max_length=30)
	port_yn = models.CharField(max_length=30)
	port_v = models.CharField(max_length=30)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.ip

class target_info(models.Model):
	ip = models.CharField(max_length=30)
	ip_yn = models.CharField(max_length=30)
	ip_v = models.CharField(max_length=30)
	port = models.CharField(max_length=30)
	port_yn = models.CharField(max_length=30)
	port_v = models.CharField(max_length=30)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.ip

class information(models.Model):
	protocol = models.CharField(max_length=30)
	protocol_yn = models.CharField(max_length=30)
	protocol_v = models.CharField(max_length=30)
	packet_size = models.CharField(max_length=30)
	doc_file = models.FileField(upload_to='Documents/')
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.protocol
