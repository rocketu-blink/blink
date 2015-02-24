from django.contrib import admin
from models import *


class GenreAdmin(admin.ModelAdmin):
    fields = ['name']

class KeywordAdmin(admin.ModelAdmin):
    fields = ['name']

class ContentTypeAdmin(admin.ModelAdmin):
    fields = ['name']

class SourceTypeAdmin(admin.ModelAdmin):
    fields = ['name']

class PersonTypeAdmin(admin.ModelAdmin):
    fields = ['name']

class PersonAdmin(admin.ModelAdmin):
    fields = ['name','imdb_id','imdb_url','headshot','type']
    search_fields = ['name']

class CharacterAdmin(admin.ModelAdmin):
    fields = ['name','imdb_id','imdb_url','actor']
    search_fields = ['name']

class ContentAdmin(admin.ModelAdmin):
    fields = ['title', 'release_date', 'release_year', 'runtime', 'mpaa_rating', 'budget', 'revenue', 'synopsis', 'imdb_rating','poster','imdb_id','imdb_url','netflix_url','hulu_url','prime_url','genre','director','writer', 'characters','content_type','source_types','keywords']
    search_fields = ['title']


admin.site.register(Genre, GenreAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(ContentType, ContentTypeAdmin)
admin.site.register(SourceType, SourceTypeAdmin)
admin.site.register(PersonType, PersonTypeAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Content, ContentAdmin)