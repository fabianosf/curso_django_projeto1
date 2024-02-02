from django.shortcuts import render
from django.http import HttpResponse



# aqui tenho um dicionario context: 
# depois renderizar no template
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Fabiano Freitas',
        'idade': '43',
        'cidade':'Rio de Janeiro',
        'pais':'Brazil',
    })


def contato(request):
    return render(request, 'recipes/contato.html')

def sobre(request):
    return HttpResponse('SOBRE')





