from django.contrib import admin
from .models import Director, Movie

class MovieInline(admin.TabularInline):
    model = Movie

class DirectorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['first_name', 'last_name', 'age']})
    ]
    inlines = [MovieInline]
    list_display = ('first_name', 'last_name', 'age')
    search_fields = ['first_name', 'last_name', 'age']

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['title', 'director']}),
        ('Description', {'fields' : ['description']}),
        ('More information', {'fields' : ['genre', 'rating']})
    ]
    list_display = ('title', 'director', 'genre', 'rating')
    list_filter = ['genre', 'rating']
    search_fields = ['title', 'genre', 'rating']


admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie, MovieAdmin)
