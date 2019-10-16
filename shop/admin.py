from django.contrib import admin
from .models import Login,Contact,Register,Profile
# Register your models here.
admin.site.register(Login)
admin.site.register(Contact)
admin.site.register(Register)
admin.site.register(Profile)