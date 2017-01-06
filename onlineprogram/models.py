from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.



class project_category(models.Model):
	categories    =     models.CharField(max_length=220)
	image         =     models.FileField(blank=True,null=True)


	def __str__(self):

		return str(self.categories)


class Project(models.Model):
	user          =   models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	category      =   models.ForeignKey(project_category, on_delete=models.CASCADE) 
	title         =   models.CharField(max_length=200,unique=True)
	cost          =   models.CharField(max_length=20,default='free')
	image         =   models.FileField()
	Description   =   models.TextField()
	Course_period =   models.CharField(max_length=220)
	Publish       =   models.DateField(auto_now=False, auto_now_add=False, blank=True)
	Update        =   models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp     =   models.DateTimeField(auto_now=False, auto_now_add=True)



	def __str__(self):
		return str(self.title)

class Upload(models.Model):
	category_upload  =  models.ForeignKey(project_category,on_delete=models.CASCADE,blank=True,null=True)
	title_upload     =  models.ForeignKey(Project,on_delete=models.CASCADE,blank=True,null=True)
	Content          =  models.CharField(max_length=220)
	Video            =  models.FileField()
	Publish          =  models.DateField(auto_now=False, auto_now_add=False,blank=True)
	timestamp        =  models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return str(self.title_upload)

class Enroll(models.Model):
	name=models.CharField(max_length=220,null=True,blank=True)
	project=models.CharField(max_length=220,null=True,blank=True)


	def __str__(self):
		return str(self.name)
		


