from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    # return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>About</h1>')

def profile(request):
    return render(request, 'profile.html')
    # shows if you are going to vote yes/no on each of the propositions

def index(request):
    return HttpResponse('<h1>Propositions Index Page</h1>')

def show(request):
    return HttpResponse('<h1>Proposition Show Page</h1>')

