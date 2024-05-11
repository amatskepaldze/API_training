from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('api/books', Book_api.as_view(), name='books_api'),
    path('current_route/<slug:route>/', current_route, name='current_route'),  # re_path()
    # path('current_route/', current_route, name='video_page'),
]
