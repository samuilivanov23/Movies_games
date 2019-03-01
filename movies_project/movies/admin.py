from django.contrib import admin
from .models import Celebrity, Movie

class MovieInline(admin.TabularInline):
    model = Movie

class CelebrityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['first_name', 'last_name', 'age', 'typeof']})
    ]
    inlines = [MovieInline]
    list_display = ('first_name', 'last_name', 'age')
    list_filter = ['first_name', 'last_name', 'age', 'typeof']
    search_fields = ['first_name', 'last_name', 'age', 'typeof']

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['title', 'celebrity']}),
        ('Description', {'fields' : ['description']}),
        ('More information', {'fields' : ['genre', 'rating']})
    ]
    list_display = ('title', 'celebrity', 'genre', 'rating')
    list_filter = ['genre', 'rating']
    search_fields = ['title', 'genre', 'rating']


admin.site.register(Celebrity, CelebrityAdmin)
admin.site.register(Movie, MovieAdmin)
