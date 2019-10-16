from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView,ListView
from product.models import Product
# Create your views here.

class searchview(ListView):
    template_name = 'view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(searchview,self).get_context_data(**kwargs)
        context['query']=self.request.GET.get('q')
        return context


    def get_queryset(self):
        request=self.request
        method_dict=request.GET
        query=method_dict.get('q',None)
        print(query)
        if query is not None:
         lookups=(Q(title__icontains=query)|
                  Q(desc__icontains=query)|
                  Q(price__icontains=query)|
                  Q(tag__title__icontains=query))
         return Product.objects.filter(lookups).distinct()
         # return Product.objects.all()
        # return Product.objects.filter(title__iexact='Shirts')


# class FooView(ListView):
#     template_name = 'foo.html'
#     queryset =Product.objects.all()
#

def searchviews(request):
    return HttpResponse("hi")