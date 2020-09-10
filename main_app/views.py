from django.shortcuts import render, redirect
from .models import Proposition
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def start(request):
    return redirect('show', proposition_id=1)

def index(request):
    return render(request, 'index.html')

# def index(request):
#     proposition = Proposition.whatIs.object.all()
#     context = {
#         'Proposition': proposition
#     }
#     return render(request, 'proposition')



def show(request, proposition_id):
    proposition = Proposition.objects.get(id=proposition_id)
    context = {
        'proposition': proposition,
    }
    return render(request, 'show.html', context)

