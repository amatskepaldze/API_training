from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookNamesSerializer
from .models import Routes, Book
from .forms import AddBook


def main_page(request):
    routes = Routes.objects.all()
    books = Book.objects.all()
    if request.method == 'POST':
        form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = AddBook() 
    
    context = {'routes' : routes, 'books' : books, 'form' : form}
    return render(request, 'main/newindex.html', context)

class Book_api(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookNamesSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BookNamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# @api_view(['GET'])
# def books_api(request):
#     books = Book.objects.all()
#     serializer = BookNamesSerializer(books, many=True)
#     return Response(serializer.data)

def current_route(request, route):
    data = {
        'number_of_route' : route
    }
    return render(request, 'main/current_route.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Старница не найдена</h1>')  #td красивая html страница для 404