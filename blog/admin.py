from django.contrib import admin
from blog.models import Products,Order

# Register your models here.


admin.site.register((Products,Order)) 
