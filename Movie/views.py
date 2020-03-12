# Create your views hereMovieGenre.
from .models import movie,ratings,watched_List
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .serializers import Ratings_Serializer,Watched_Serializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import FeedbakcForm 
import random
import pandas as pd
import numpy as np
from django.forms import model_to_dict
from UserProfile.models import User
from scipy.sparse.linalg import svds

def recommendations_using_svd(userid):
    pallobjs = [ model_to_dict(pallobj) for pallobj in ratings.objects.all()] 
    rating_df = pd.DataFrame(pallobjs)
    movies_df = [ model_to_dict(pallobj) for pallobj in movie.objects.all()] 
    movies_df = pd.DataFrame(movies_df)
    n_users = rating_df.UserId.unique().shape[0]
    n_movies = rating_df.MovieID.unique().shape[0]
    Ratings = rating_df.pivot(index = 'UserId', columns ='MovieID', values = 'rating').fillna(0)
    # print(Ratings)
    R = Ratings.as_matrix()
    userid=userid-1
    user_ratings_mean = np.mean(R, axis = 1)
    Ratings_demeaned = R - user_ratings_mean.reshape(-1, 1)
    U, sigma, Vt = svds(Ratings_demeaned, k = 3)
    sigma = np.diag(sigma)
    all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
    preds = pd.DataFrame(all_user_predicted_ratings, columns = Ratings.columns)
    df=preds
    a=df.iloc[[userid]]
    b=Ratings.iloc[[userid]]
    a=a.values[0].tolist()
    m1=list(df.columns.values)
    d1={}
    for m in range(1,len(m1)):
        d1[a[m]]=m1[m]

    b=b.values[0].tolist()
    recommendations=[]
    for i in range(len(b)):
        if b[i] == 0:
            recommendations.append(a[i])
    user_recommendations=sorted(set(recommendations),reverse=True)
    num_to_select = 5                           # set the number to select here.
    recommended_items = random.sample(user_recommendations, num_to_select)
    l1=[]
    for item in recommended_items:
        i1=d1[item]
        l1.append(i1)

    return l1

class Ratings_List(APIView):
    def get(self, request, format=None):
        rs = ratings.objects.all()
        serializer = Ratings_Serializer(rs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Ratings_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #mymodel.objects.filter(first_name__icontains="Foo", first_name__icontains="Bar")
            obj='review submited successfully'
            return Response(obj, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Watched_Serializer_View(APIView):
    def get(self, request, format=None):
        rs = watched_List.objects.all()
        serializer = Watched_Serializer(rs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Watched_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            obj='add to watched list successfully'
            return Response(obj, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    if request.user.is_authenticated:
        genre=request.user.favorite_genre
        print(type(genre))
        movies=movie.objects.filter(MovieGenre=str(genre))
        if request.user.age_group == '18-30':
            amovies=movie.objects.filter(MovieGenre="Action")
        elif request.user.age_group == '31-41':
            amovies=movie.objects.filter(MovieGenre="Romance")
        else:
            amovies=movie.objects.filter(MovieGenre="Comedy")
        movies=list(movies)+list(amovies)
        user_interest_recommendations=set(movies)
        num_to_select = 5                           # set the number to select here.
        recommended_items = random.sample(user_interest_recommendations, num_to_select)
        movies=recommended_items
        userid=request.user.id
        rmovies=[]
        rateduser=ratings.objects.filter(UserId=userid)
        if len(rateduser)>0:
            recommendations=recommendations_using_svd(userid)
            for r in recommendations:
                movie1=movie.objects.filter(MovieID=r)
                rmovies.append(movie1[0])

    else:
        movies=movie.objects.all()
        rmovies=[]
    return render (request,'index.html',{"movies":movies,"rmovies":rmovies})

def movies_list(request):
	movies=movie.objects.all()
	return render (request,'movies.html',{"movies":movies})

def movie_detail(request,id=None):    
    instance = get_object_or_404(movie,id=id)
    return  render (request,"movie_detail.html" , {'instance' : instance})



def watched_list(request):
	if request.user.is_authenticated:
		userid=request.user.id
		movies=watched_List.objects.filter(UserId=str(userid))
		print(movies)
	else:
		movies=['there is no watched movies',]
	return render (request,'watchedlist.html',{"movies":movies})
