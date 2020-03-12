from django.contrib import admin
from .models import movie,ratings,watched_List
# Register your models here.



admin.site.register(movie)
admin.site.register(ratings)
admin.site.register(watched_List)