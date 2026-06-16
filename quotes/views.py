from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

days_of_week = {
    "Lunes":"Comenzando la semana",
    "Martes":"Falta poco para que termine la semana",
    "Miercoles":"Hoy se sale temprano, eso es bueno",
    "Jueves":"Hoy es viernes chico, no queda nada",
    "Viernes":"Desde hoy se comienza a descanzar",
    "Sabado":"Este es el mejor dia",
    "Domingo":"Domingo de ONE PIECE",
}

def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day > len(days):
        return HttpResponseNotFound("El dia no existe")
    redirect_day = days[day-1]
    return HttpResponseRedirect(f"/quotes/{redirect_day}")

def days_week(request, day):
    try:    
        day_formatted = day.capitalize()
        quote_text = days_of_week[day_formatted]
        return HttpResponse(quote_text)
    except KeyError: return HttpResponseNotFound("Hoy no es un buen dia xD\nTu pagina no se encuentra disponible")

    # def days_week(request, day):
#     # Convertir a formato título (primera letra mayúscula, resto minúscula)
#     day_formatted = day.capitalize()
#     quote_text = days_of_week.get(day_formatted, "Día no válido")
#     return HttpResponse(quote_text)