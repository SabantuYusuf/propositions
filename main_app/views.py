from django.shortcuts import render, redirect
from .models import Proposition
# Add the following import
from django.http import HttpResponse, HttpResponseRedirect

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
    
    if request.method == 'POST':
        print(request.POST['proposition'])

        # selected_option = request.POST['proposition']
        selected_option = request.POST.get('proposition', False);
        if selected_option == 'yes':
            proposition.yes_count += 1
        elif selected_option == 'no':
            proposition.no_count += 1
        else:
            return HttpResponse(400, 'Invalid Form') 
        
        proposition.save()

        return redirect('index')
        # return HttpResponseRedirect(request.path_info)

    context = {
        'proposition': proposition,
        'side_bar_proposition_numbers': side_bar_proposition_numbers,
    }
    return render(request, 'show.html', context)

