from django.shortcuts import render,redirect
from .forms import Contactform,Registrationform, ProfileupdateForm,UserupdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import xhtml2pdf.pisa as pisa
from orders.models import Order
from django.template.loader import get_template
from product.models import Product
from django.http import HttpResponse
from shop.util import *

def home(request):
    # print(request.session.get('first_name','unknown'))
    content={
        "home":"home page"
    }
    return render(request,'shop/home.html',content)


def contact(request):
    if request.method=='POST':
        form=Contactform(request.POST)
        form.save()
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        form = Contactform()
    return render(request,'shop/contact.html',{'form': form})



def register(request):
    if request.method == 'POST':
        f =Registrationform(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully!, Now you are able to login')
            return redirect('login')
    else:
        f =Registrationform()
    return render(request, 'shop/reg.html', {'form': f})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserupdateForm(request.POST, instance=request.user)
        p_form = ProfileupdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserupdateForm(instance=request.user)
        p_form = ProfileupdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'shop/profile.html', context)


def some_view(request):
        template = get_template('shop/pdf.html')
        queryset = Product.objects.all()

        context = {'bd': queryset,
                   'vd': Order
                   }
        html = template.render(context)
        pdf = render_to_pdf('shop/pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


# def some_view(request):
#     # Create the HttpResponse object with the appropriate PDF headers.
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment'
#     filename="charge.pdf"
#
#     # Create the PDF object, using the response object as its "file."
#     p = canvas.Canvas(response)
#
#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100, "Hello world.")
#
#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()
#     return response
#




# @login_required
# def profile(request):
#     u_form=UserupdateForm(request.user)
#     p_form=ProfileupdateForm(request.user.profile)
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#
#
#     return render(request,'shop/profile.html',context)







def testhome(request):
    context = {}
    template = "donotuse.html"
    return render(request, template, context)






# def user_login(request):
#     if request.method == 'POST':
#         f =LoginForm(request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request, 'Login successfully')
#             return redirect('logout')
#     else:
#         f =LoginForm()
#     return render(request, 'shop/login.html', {'form': f})
#
# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#     return redirect('home')
# def index(request):
#     return render(request,'shop/index.html')
#
# @login_required
# def special(request):
#     return HttpResponse("You are logged in !")
#
# @login_required
# def account(request):
#     return render(request,'shop/account.html')



#
# def login_page(request):
#     form=Loginform(request.POST or None)
#     context = {
#         "form": form
#     }
#     print('user logged in')
#     if form.is_valid():
#         print(form.cleaned_data)
#         username=form.cleaned_data.get('username')
#         password=form.cleaned_data.get('password')
#         user = authenticate(request, username=username, password=password)#authenticate is checks the username and password is correct or not and if user and password is not ok it gives error
#         print(user)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             # context['form']:Loginform
#             ...
#             return redirect('/login')
#         else:
#             # Return an 'invalid login' error message.
#             ...
#         print('error')#login usename and password is not use that it will be occured
#
#     return render(request,'shop/login.html',context)
#
#
# def register_page(request):
#     form=Registrationform(request.POST or None)
#     context = {
#         "form": form
#     }
#     print('Signeed in')
#     if form.is_valid():
#         print(form.cleaned_data)
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         email = form.cleaned_data.get('email')
#         c_password=form.cleaned_data.get('c_password')
#         new_user=authenticate(request, username=username, password=password,email=email,c_password=c_password)
#         print(new_user)
#
#
#     return render(request,'shop/reg.html',context)
#
#
#
#

#
#
# def register_page(request):
#     if request.method == 'POST':
#         form = Registrationform(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = Registrationform()
#     return render(request,'shop/reg.html',{'form': form})
