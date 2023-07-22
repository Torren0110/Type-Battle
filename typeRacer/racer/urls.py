from django.urls import path, include
from .views import home, addPassage

urlpatterns = [
    path('', home, name='home'),
    path('solo-mode/', include('solo_mode.urls')),
    path('multi-mode/', include('multi_mode.urls')),
    path('add-passage/', addPassage, name='addPassage')
]