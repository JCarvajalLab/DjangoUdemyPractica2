from django.shortcuts import render
from django.http import HttpResponseNotFound

def index(request):
    try:
        return render(request, 'minilibrary/minilibrary.html', {
            "text": "Hola desde la vista",
            "name": "Jordan"
        })
    except Exception:
        return HttpResponseNotFound("Pagina no encontrada")