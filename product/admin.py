from django.contrib import admin
from .models import Product
# Register your models here.


class AdminProduct(admin.ModelAdmin):#slug field is showing in admin side
    list_display = ['__str__','slug']
    class Meta:
      model=Product


admin.site.register(Product,AdminProduct)