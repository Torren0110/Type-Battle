from django.contrib import admin
from .models import Lobby, Player, PlayerProgress

# Register your models here.
admin.site.register(Lobby)
admin.site.register(Player)
admin.site.register(PlayerProgress)