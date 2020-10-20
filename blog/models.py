from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Products(models.Model):
	sno = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 200)
	price = models.CharField(max_length = 200)
	size = models.CharField(max_length = 200)
	material = models.CharField(max_length = 200)
	slug = models.CharField(max_length = 200,blank = True)
	color = models.CharField(max_length = 200)
	imglink = models.CharField(blank = True , max_length = 255)
	content = RichTextField()
	time = models.DateTimeField('Created Time', auto_now_add=True, null=True)
	slug = models.CharField(max_length = 255)
	Descriptions = models.TextField(blank = True)
	keyword = models.CharField(max_length = 255 , blank = True)

	def __str__(self):
		return self.title


class Order(models.Model):
	sno = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	number = models.CharField(max_length = 200)
	product = models.CharField(max_length = 200,blank = True)
	price = models.CharField(max_length = 200 , blank = True)
	user = models.CharField(max_length =100)
	address = models.TextField()

	def __str__(self):
		return self.name		