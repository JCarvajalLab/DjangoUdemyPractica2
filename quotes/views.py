from django.http import HttpResponse, HttpResponseNotFound

def days_week(request, day):
    quote_text = None
    if day == "monday":
        quote_text = "Comenzando la semana"
    elif day == "tuesday":
        quote_text = "Quedan pocos dias para descansar"
    else:
        return HttpResponseNotFound("Hoy no es un buen dia xD\nTu pagina no se encuentra disponible")
    
    return HttpResponse(quote_text)