from django.shortcuts import render




# aqui tenho um dicionario context: 
# depois renderizar no template
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Fabiano Freitas',
        'idade': '43',
        'cidade':'Rio de Janeiro',
        'pais':'Brazil',
    })


 




