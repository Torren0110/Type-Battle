from django.urls import path, include
from .views import menu, battle

urlpatterns = [
    path('', menu, name='solo-menu'),
    path('battle/<difficulty>', battle, name='solo-battle'),
    path('battle/', menu)
]