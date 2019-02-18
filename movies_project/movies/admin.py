from django.contrib import admin
from .models import Director, Movie

class MovieInline(admin.TabularInline):
    model = Movie

class DirectorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['first_name', 'last_name', 'age']})
    ]
    inlines = [MovieInline]

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['title', 'director']})
    ]

admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie, MovieAdmin)
