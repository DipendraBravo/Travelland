from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def destination(request):
    return render(request, 'pages/destination.html')


def signin(request):
    return render(request, 'pages/signin.html')

def signup(request):
	return render(request,'pages/signup.html')