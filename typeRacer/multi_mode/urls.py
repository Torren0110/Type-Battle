from django.urls import path, include
from .views import menu, battle, getInfo, postInfo

urlpatterns = [
    path('', menu, name='multi-menu'),
    path('battle/<difficulty>', battle, name='multi-battle'),
    path('getInfo/', getInfo, name='getInfo'),
    path('postInfo/', postInfo, name='postInfo')
]