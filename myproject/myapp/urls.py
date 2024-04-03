from django.urls import path
from . import views

urlpatterns = [
    path('star/', views.star, name='star'),
    path('main/' , views.main , name='main'),
    path('firefly/' , views.firefly , name='firefly'),
    path('' , views.home , name='home'),
]
