from django.shortcuts import render
from blog.models import Products ,Order
from django.contrib import messages

# Create your views here.

def blog(request):
	allPost1 = Products.objects.all()[::-1] 
	context = {'allPost1':allPost1}
	return render(request , "blog/blog.html",context)

def blogpost(request , slug):
	allPost1 = Products.objects.filter(slug = slug).first()
	context = {'post':allPost1}

	return render(request , "blog/blog-single.html",context)	


def finish(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		number= request.POST['number']
		address= request.POST['address']
		price = request.POST['price']
		product = request.POST['slug']
		user = request.POST['user']

		order = Order(name = name , email = email , number = number , address = address , product = product , price = price, user=user)
		order.save()
	
	return render(request ,"home/finish.html")	
