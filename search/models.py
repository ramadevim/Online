from django.db import models
from product.models import Product
from product.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse

class Tag(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, db_index=True,null=True)
    product=models.ManyToManyField(Product,blank=True)

    def __str__(self):
        return self.title

def tag_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(tag_pre_save_receiver,sender=Tag)