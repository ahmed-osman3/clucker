from django.shortcuts import render

from microblogs.forms import SignUpForm


def home(request): #request is object created by django containing all infromation recieved by http request.
   return render(request,'home.html')

def sign_up(request):
   form = SignUpForm()
   return render(request,'sign_up.html',{'form': form})