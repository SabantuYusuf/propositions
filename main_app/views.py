from django.shortcuts import render, redirect


# Add the following import
from django.http import HttpResponse
from .models import Proposition

# Define the home view
def home(request):
<<<<<<< HEAD
    # return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
=======
>>>>>>> master
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def start(request):
    return redirect('show', proposition_id=1)

def profile(request):
    return render(request, 'profile.html')
    # shows if you are going to vote yes/no on each of the propositions

def index(request):
    return render(request, 'index.html')

def show(request, proposition_id):
    proposition = Proposition.objects.get(id=proposition_id)
    context = {
        'proposition': proposition,
    }
    return render(request, 'show.html', context)

