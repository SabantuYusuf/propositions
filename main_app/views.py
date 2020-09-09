from django.shortcuts import render, redirect


# Add the following import
from django.http import HttpResponse
from .models import Proposition

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def start(request):
    return redirect('show', proposition_id=1)

def index(request):
    return render(request, 'index.html')

def show(request, proposition_id):
    side_bar_proposition_numbers = Proposition.objects.all().order_by('number')
    proposition = Proposition.objects.get(id=proposition_id)
    
    context = {
        'proposition': proposition,
        'side_bar_proposition_numbers': side_bar_proposition_numbers,
    }
    return render(request, 'show.html', context)

