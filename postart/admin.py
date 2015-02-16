from string import join
import os
from os.path import join as pjoin
from django.db import models
from django.contrib import admin
from postart.models import Album, Image, Tag, Author
from django.conf import settings
from PIL import Image as PImage
from django.contrib.auth.models import User


class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title"]
    
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "first_name", "last_name", "email","headshot"]
    def save_model(self, request, obj, form, change):
        obj.author = request.author
        obj.save()

class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]

class ImageAdmin(admin.ModelAdmin):
    # search_fields = ["title"]
    list_display = ["__unicode__", "title", "author", "rating", "size", "tags_","created","authors_"]
    list_filter = ["tags", "albums", "author"]

    def save_model(self, request, obj, form, change):
        obj.author = request.author
        obj.save()

admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Author,AuthorAdmin)

# Register your models here.
