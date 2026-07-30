from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Book
from django.db.models import Q

def index(request):
    try:
        books = Book.objects.all()
        query = request.GET.get("query_search")

        if query:
            books = books.filter(
                Q(title__icontains=query) | Q(author__name__icontains=query)
            )

        return render(request, 'minilibrary/minilibrary.html', {
            "books": books,
            "query": query
        })
    except Exception:
        return HttpResponseNotFound("Pagina no encontrada")