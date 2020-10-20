from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login , logout as auth_logout , authenticate
from home.models import SliderContent,AfterSliderContent,PopularProducts,LatestProducts_Content,About_Content_Heading,About_Three_Content,About_Content_Paragraph, About_Content_Top_Down,VideoSection,Location,ContactUs
from blog.models import Products , Order

# from django.contrib import messages
# from home.models import 
# from blog.models import Blog

# Create your views here.


def home(request):
	allPost1 = SliderContent.objects.all()[::-1]
	allPost2 = AfterSliderContent.objects.all()[::-1]
	allPost3 = PopularProducts.objects.all() [::-1]
	allPost4 = LatestProducts_Content.objects.all()[::-1]
	allPost5 = About_Content_Heading.objects.all()[::-1]
	allPost6 = About_Three_Content.objects.all()[::-3]
	allPost7 = About_Content_Paragraph.objects.all()[::-1]
	allPost8 = About_Content_Top_Down.objects.all()[::-3]
	allPost9 = VideoSection.objects.all()[::-1]
	allPost10 = Location.objects.all()[::-1]
	allPost11 = Products.objects.all()[::-2]
	context = {'allPost1':allPost1 , 'allPost2':allPost2 , 'allPost3':allPost3 , 'allPost4':allPost4 , 'allPost5':allPost5
	, 'allPost6':allPost6 , 'allPost7':allPost7 , 'allPost8':allPost8 , 'allPost9':allPost9, 'allPost10':allPost10, 'allPost11':allPost11}

	if request.method == 'POST':
		name = request.POST['name']
		subject = request.POST['subject']
		message = request.POST['message']
		number = request.POST['number']
		email = request.POST['email']
		contact = ContactUs(name = name , subject = subject , message = message , number = number , email = email)
		contact.save()

	return render(request , "home/index.html" , context)

def blogpost(request , slug):
	allPost1 = PopularProducts.objects.filter(slug = slug).first()
	context = {'post':allPost1}

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

	return render(request , "home/post.html",context)		



def search(request):
	if request.method == 'GET':
		search = request.GET['query']

		if len(search) > 78:
			allPost1 = Products.objects.none()
		else:
			allPostTitle = Products.objects.filter(title__icontains = search)
			allPostContent = Products.objects.filter(content__icontains = search)
			allPosts = allPostTitle.union(allPostContent)
			context = {'allPosts':allPosts, 'search':search}

	return render(request, 'home/search.html',context)	
		


def signup(request):
	if request.method == 'POST':
		username = request.POST['susername']
		fname = request.POST['fname']
		lname = request.POST['lname']
		number = request.POST['number']
		email = request.POST['email']
		pass1 = request.POST['password1']
		pass2 = request.POST['password2']

		# if len(username) > 10:
		# 	# messages.error(request , "username Lenth Must Be Less Then 10 Character")
		# 	return redirect('/home')

		# if username.isalnum():
		# 	# messages.error(request , "Username Should Be Character And Number")		
		# 	return redirect('/home')

		# if pass1 != pass2:
		# 	# messages.error(request , 'Password Not Matched ')	
		# 	return redirect('/home')


		myuser = User.objects.create_user(username , email , pass1)
		myuser.first_name = fname
		myuser.last_name = lname
		myuser.phone_number = number
		myuser.save()
		# messages.success(request ,"Successfully Created Your Account")
		return redirect('/')


def login(request):
	if request.method == 'POST':
		username = request.POST['lusername']
		password = request.POST['lpassword']

		myuser = authenticate(username = username , password = password)
		auth_login(request , myuser)
		# messages.success(request , "Successfully Logged In ")
		return redirect('/home/')

	return redirect("/home/")	
	

def logout(request):
	auth_logout(request)
	# messages.success(request , "Successfully logout Your Account")
	return redirect('/home/')	





