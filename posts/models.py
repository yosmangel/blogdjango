from django.db import models

# Create your models here.

class Post(models.Model):
	titulo= models.CharField(max_length=150)
	contenido=models.TextField()
	timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado=models.DateTimeField(auto_now_add=False, auto_now=True)


	def __unicode__(self): #Python3 __str__
		return self.titulo

