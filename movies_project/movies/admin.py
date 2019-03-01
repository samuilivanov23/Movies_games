from django.contrib import admin
from .models import Celebrity, Movie

#class MovieInline(admin.TabularInline):
#   model = Movie

#class CelebrityInline(admin.TabularInline):
#    model = Celebrity
'''
class CelebrityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['first_name', 'last_name', 'age', 'typeof']})
    ]
    #inlines = [MovieInline]
    list_display = ('first_name', 'last_name', 'age')
    list_filter = ['first_name', 'last_name', 'age', 'typeof']
    search_fields = ['first_name', 'last_name', 'age', 'typeof']

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['title']}),
        ('Description', {'fields' : ['description']}),
        ('More information', {'fields' : ['genre', 'rating']})
    ]
    #inlines = [CelebrityInline]
    filter_horizontal = ('celebrities', )
    list_display = ('title', 'genre', 'rating')
    list_filter = ['genre', 'rating']
    search_fields = ['title', 'genre', 'rating']

'''

#class MovieInline(admin.TabularInline):
#   model = Movie

#class CelebrityInline(admin.TabularInline):
#    model = Celebrity

class CelebrityAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'typeof')
    search_fields = ['first_name', 'last_name', 'age', 'typeof']
    #inlines = [MovieInline]
    
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'rating')
    search_fields = ['title', 'genre', 'rating']
    filter_horizontal = ('celebrities', )

admin.site.register(Celebrity, CelebrityAdmin)
admin.site.register(Movie, MovieAdmin)
