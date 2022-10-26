from django.shortcuts import redirect, render

from microblogs.forms import SignUpForm
from microblogs.models import User


def home(request): #request is object created by django containing all infromation recieved by http request.
   return render(request,'home.html')

def feed(request): 
   return render(request,'feed.html')

def sign_up(request):
   if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
         User.objects.create_user(
            form.cleaned_data.get('username'),
            first_name = form.cleaned_data.get('first_name'),
            last_name = form.cleaned_data.get('last_name'),
            email = form.cleaned_data.get('email'),
            bio = form.cleaned_data.get('bio'),
            password = form.cleaned_data.get('password'),
         )
         return redirect('feed')
   else:
      form = SignUpForm()
   return render(request,'sign_up.html',{'form': form})