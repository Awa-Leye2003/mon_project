 # pages/urls.py
from django.urls import path
from .views import homePageView  # Assurez-vous que views.py existe
urlpatterns = [
    path('', homePageView, name='home')  # Assurez-vous que la fonction homePageView est bien définie
]
