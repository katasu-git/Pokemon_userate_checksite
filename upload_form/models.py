from django.db import models
from datetime import datetime

class FileNameModel(models.Model):
    file_name = models.CharField(max_length = 50)
    upload_time = models.DateTimeField(default = datetime.now)

class pokeinfo(models.Model):
    pokename = models.CharField(max_length=10,null=True,blank=True)
    pokerate = models.CharField(max_length=10,null=True,blank=True)
    waza1 = models.CharField(max_length=10,null=True,blank=True)
    waza2 = models.CharField(max_length=10,null=True,blank=True)
    waza3 = models.CharField(max_length=10,null=True,blank=True)
    waza4 = models.CharField(max_length=10,null=True,blank=True)
    waza5 = models.CharField(max_length=10,null=True,blank=True)
    waza6 = models.CharField(max_length=10,null=True,blank=True)
    waza7 = models.CharField(max_length=10,null=True,blank=True)
    waza8 = models.CharField(max_length=10,null=True,blank=True)
    #waza9 = models.CharField(max_length=10,null=True,blank=True)
    #waza10 = models.CharField(max_length=10,null=True,blank=True)
    #waza11 = models.CharField(max_length=10,null=True,blank=True)
    #waza12 = models.CharField(max_length=10,null=True,blank=True)
    wazarate1 = models.CharField(max_length=10,null=True,blank=True)
    wazarate2 = models.CharField(max_length=10,null=True,blank=True)
    wazarate3 = models.CharField(max_length=10,null=True,blank=True)
    wazarate4 = models.CharField(max_length=10,null=True,blank=True)
    wazarate5 = models.CharField(max_length=10,null=True,blank=True)
    wazarate6 = models.CharField(max_length=10,null=True,blank=True)
    wazarate7 = models.CharField(max_length=10,null=True,blank=True)
    wazarate8 = models.CharField(max_length=10,null=True,blank=True)
    #wazarate9 = models.CharField(max_length=10,null=True,blank=True)
    #wazarate10 = models.CharField(max_length=10,null=True,blank=True)
    #azarate11 = models.CharField(max_length=10,null=True,blank=True)
    #wazarate12 = models.CharField(max_length=10,null=True,blank=True)
