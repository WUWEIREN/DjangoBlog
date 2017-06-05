from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def hello(request):
    return HttpResponse('<html><body>Hello World</body></html>')


def user(request):
    return render(request, 'user.html')


def login(request):
    if 'name' and 'pwd' in request.POST:
        name = request.POST['name']
        pwd = request.POST['pwd']
        if name == 'nn':

            return redirect(reverse('user'))
    return render(request, 'index.html')
