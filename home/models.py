from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.


class Logo(models.Model):
	sno = models.AutoField(primary_key = True)
	logo = models.CharField(max_length = 200)



class SliderContent(models.Model):
	sno = models.AutoField(primary_key = True)
	heading = models.CharField(max_length = 200)
	content = RichTextField()


	def __str__(self):
		return self.heading


class AfterSliderContent(models.Model):
	sno = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 200)
	content = RichTextField()


	def __str__(self):
		return self.title


class PopularProducts(models.Model):
	sno = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 200)
	price = models.CharField(max_length = 200)
	size = models.CharField(max_length = 200)
	material = models.CharField(max_length = 200)
	slug = models.CharField(max_length = 200 , blank = True)
	color = models.CharField(max_length = 200)
	imglink = models.CharField(blank = True , max_length = 255)
	content = RichTextField()
	time = models.DateTimeField('Created Time', auto_now_add=True, null=True)
	Descriptions = models.TextField(blank = True)
	keyword = models.CharField(max_length = 255 , blank = True)

	def __str__(self):
		return self.title


class LatestProducts_Content(models.Model):
	sno = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 200)
	content = RichTextField()


	def __str__(self):
		return self.title



class About_Content_Heading(models.Model):
	sno = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 200)
	content = RichTextField()


	def __str__(self):
		return self.title




class About_Three_Content(models.Model):
	sno = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 200)
	img = models.CharField(max_length = 200)
	content = RichTextField()


	def __str__(self):
		return self.title		


class About_Content_Paragraph(models.Model):
	sno = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 200)
	content = RichTextField()


	def __str__(self):
		return self.title		


class About_Content_Top_Down(models.Model):
	sno = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 200)
	content = RichTextField()


	def __str__(self):
		return self.title		



class VideoSection(models.Model):
	sno = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 200)
	video_link = models.CharField(max_length = 200)
	content = RichTextField()


	def __str__(self):
		return self.title			

class Location(models.Model):
	sno = models.AutoField(primary_key = True)
	link = models.CharField(max_length = 200)

	def __str__(self):
		return self.link								



class ContactUs(models.Model):
	sno = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 200)
	subject = models.CharField(max_length = 200)
	number = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	message = RichTextField()
	
	def __str__(self):
		return self.name		