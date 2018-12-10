from django.shortcuts import render
import requests

# Create your views here.
from frontend.forms import BuscarForm


def index(request):
    if request.method == "POST":
        form = BuscarForm(request.POST)
        if form.is_valid():
            busqueda =form.cleaned_data['buscar']
            response = requests.get('http://127.0.0.1:8000/backoffice/api/v1/estacionamiento/?nombre=' + busqueda)
    else:
        response = requests.get('http://127.0.0.1:8000/backoffice/api/v1/estacionamiento/')

    data = response.json()

    ctx = {'estacionamiento': data}
    return render(request, 'index.html', ctx)


def detail(request, pk):
    response = requests.get('http://127.0.0.1:8000/backoffice/api/v1/estacionamiento/' + str(pk))
    data = response.json()

    ctx = {'estacionamiento': data}
    return render(request, 'detail.html', ctx)