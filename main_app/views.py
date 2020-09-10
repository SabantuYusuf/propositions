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
    propositions = Proposition.objects.all().order_by('number')
    context = {
        'propositions': propositions
    }
    return render(request, 'index.html', context)


def show(request, proposition_id):
    side_bar_proposition_numbers = Proposition.objects.all().order_by('number')
    proposition = Proposition.objects.get(id=proposition_id)
    if request.method == "POST":
        if "noteAddYes" in request.POST: #checking if there is a request to add a vote note
            print: 'yes'
            # # title = request.POST["description"] #title
			# VoteNote = VoteNote(number=number)
			# VoteNote.save() #saving the todo 
			# return redirect("/") #reloading the page
        else:
            print: 'no'
            # # title = request.POST["description"] #title
			# VoteNote = VoteNote(number=number)
			# VoteNote.save() #saving the todo 
			# return redirect("/") #reloading the page

    context = {
        'proposition': proposition,
        'side_bar_proposition_numbers': side_bar_proposition_numbers,
    }
    return render(request, 'show.html', context)

