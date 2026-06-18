from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prhases/', include("quotes.urls")),
    path('landings/', include("landing.urls")),
]