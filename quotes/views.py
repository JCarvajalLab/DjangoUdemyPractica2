from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

days_of_week = {
    "Lunes":"Comenzando la semana",
    "Martes":"Falta poco para que termine la semana",
    "Miercoles":"Hoy se sale temprano, eso es bueno",
    "Jueves":"Hoy es viernes chico, no queda nada",
    "Viernes":"Desde hoy se comienza a descanzar",
    "Sabado":"Este es el mejor dia",
    "Domingo":"Domingo de ONE PIECE",
}

def index(request):
    list_items = ""
    days = list(days_of_week.keys())

    for day in days:
        day_path = reverse("day-quote", args=[day])
        list_items += f"<li><a href=\"{day_path}\">{day}</a></li>"
    response_html = f"<ul>{list_items}</ul>"
    return HttpResponse(response_html)

def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day > len(days):
        return HttpResponseNotFound("<h1>El dia no existe</h1>")
    redirect_day = days[day-1]
    redirect_path = reverse("day-quote", args=[redirect_day])
    return HttpResponseRedirect(redirect_path)

def days_week(request, day):
    try:    
        day_formatted = day.capitalize()
        quote_text = days_of_week[day_formatted]
        return HttpResponse(quote_text)
    except KeyError: return HttpResponseNotFound("Hoy no es un buen dia xD\nTu pagina no se encuentra disponible")