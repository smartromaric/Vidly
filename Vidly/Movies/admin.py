from django.contrib import admin
from .models import Genre, Movie


# Register your models here.

class AdminGenre(admin.ModelAdmin):
    list_display = ("id", "name")


class AdminMovie(admin.ModelAdmin):
    list_display =("genre","dispo")
    exclude = "date_created",
    list_editable = "dispo",

admin.site.register(Genre,AdminGenre)
admin.site.register(Movie,AdminMovie)

