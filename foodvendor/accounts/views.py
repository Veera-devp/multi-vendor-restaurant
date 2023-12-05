from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from django.contrib import messages
from vendor.forms import VendorForm
# Create your views here.

def registerUser(request):
      if request.method == 'POST':
            print(request.POST)
            form = UserForm(request.POST)
            if form.is_valid():
                  # password = form.cleaned_data['password']
                  # user = form.save(commit=False)
                  # user.set_password(password)
                  # user.role = User.CUSTOMER
                  # user.save()

                  first_name = form.cleaned_data['first_name']
                  last_name = form.cleaned_data['last_name']
                  username = form.cleaned_data['username']
                  email = form.cleaned_data['email']
                  password = form.cleaned_data['password']
                  user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                  user.role=User.CUSTOMER
                  user.save()
                  messages.success(request,'Your account has been registered succefully')
                  return redirect('registerUser')
            else:
                  print('Invalid Form')
                  print(form.errors)
      else:
            form = UserForm()
      form = UserForm()
      context = {
            'form':form,
      }
      return render(request,'accounts/registerUser.html',context)


def registerVendor(request):
      form = UserForm()
      v_form = VendorForm()

      context = {
            'form':form,
            'v_form':v_form,
      }
      return render(request,'accounts/registerVendor.html',context)