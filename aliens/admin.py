from django.contrib import admin
from aliens.models import Alien


class alienView(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(Alien, alienView)
