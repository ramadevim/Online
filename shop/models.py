from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Contact(models.Model):
  name=models.CharField(max_length=100)
  email=models.EmailField()

class Register(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()


class Login(models.Model):
    name=models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username


    def save(self,**kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)