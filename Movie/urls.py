from django.contrib import admin
from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	path('',views.index,name='index'),
#	path('<int:id>/movie_detail',views.movie_detail,name='movie_detail'),
	path('ratings/', views.Ratings_List.as_view()),
	path('watched/', views.Watched_Serializer_View.as_view()),
	path('movies_list/',views.movies_list,name='movies_list'),
	path('watched_list/',views.watched_list,name='watched_list'),
	path('movies_list/Movie/movie/<int:id>/',views.movie_detail,name='movie_detail'),

]


urlpatterns = format_suffix_patterns(urlpatterns)