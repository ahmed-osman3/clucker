from django.shortcuts import render


def home(request): #request is object created by django containing all infromation recieved by http request.
   return render(request,'home.html')