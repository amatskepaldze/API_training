from django import forms
from django.db import models
from .models import Author, Book

# class AddBook(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.FloatField()
#     available_amount = forms.IntegerField()
#     author = forms.ModelChoiceField(queryset=Author.objects.all())

class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'price', 'available_amount', 'author']
        