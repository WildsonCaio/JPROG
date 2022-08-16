from django.shortcuts import render
import requests

def index(request):

    response = requests.get('https://pokeapi.co/api/v2/pokemon/').json()

    
    return render(request, 'pages/index.html', {'response':response})
