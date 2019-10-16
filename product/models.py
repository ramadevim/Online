from django.db import models
from django.urls import reverse

#
# class Category(models.Model):
#     name = models.CharField(max_length=200,db_index=True)
#     slug = models.SlugField(max_length=200, db_index= True, unique=True)
#
#     class Meta:
#         ordering = ("name",)
#         verbose_name = "category"
#         verbose_name_plural = "categories"
#
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse("shop:product_list_by_category",args=[self.slug])
#

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True)
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=20,default=99.9)
    image = models.ImageField(upload_to = "products/%y/%m/%d",blank=True,default='pic.jpg')
    featured = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)



    def __str__(self):#it is showing your products list wise means if your not giving this the product objects is showing like product_object1 and peoduct_object2 like wise so we just add this it showing with in the product how many objects is represnt
        return self.title

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse("product:product_detail", args=[self.id,self.slug])#appname:view name,url




