from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("<int:day>", views.days_week_with_number), #/ruta dinamica
    path("<str:day>", views.days_week, name="day-quote"), #/ruta dinamica
]