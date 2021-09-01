import json


from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import numpy as np
import pandas as pd
import csv
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sentence_transformers import SentenceTransformer
from rest_framework.views import APIView
from rest_framework.response import Response
from numpy import savetxt
from film.models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


def getmovie():
    movies = pd.read_csv('movies.csv')
    df2 = movies[["movieId", "Title", "Plot", "vote_average"]]
    return df2


def getmovies():
    movies = pd.read_csv('movies.csv')
    return movies


def getrate():
    ratings = pd.read_csv("rate.csv")
    return ratings


def getmerge():
    df2 = getmovie()
    ratings = getrate()
    df = df2.merge(ratings, how="left", on="movieId")
    return df


def getfilm():
    movies = pd.read_csv('movies.csv')
    return movies


class trainingRecomender(APIView):
    def get(self, request):
        df2 = getmovie()
        #newdf = json.dumps(json.loads(df2.to_json(orient='index')), indent=2)
        df2.dropna(axis=0, how='all', inplace=True)
        #df2['index'] = [i for i in range(0, len(df2))]
        #df2 = df2.dropna()
        #bert = SentenceTransformer('bert-base-nli-mean-tokens')
        #sentence_embeddings = bert.encode(df2['Plot'].tolist())
        #similarity = cosine_similarity(sentence_embeddings)
        #savetxt('data.csv', similarity, delimiter=',')
        return Response('name')


def getMean():
    ratings = getrate()
    Mean = ratings.groupby(by="userId", as_index=False)['rating'].mean()
    return Mean


def getRating_avg():
    ratings = getrate()
    Mean = getMean()
    Rating_avg = pd.merge(ratings, Mean, on='userId')
    Rating_avg['adg_rating'] = Rating_avg['rating_x'] - Rating_avg['rating_y']
    return Rating_avg


def getcheck():
    Rating_avg = getRating_avg()
    check = pd.pivot_table(Rating_avg, values='rating_x',
                           index='userId', columns='movieId')
    return check


def getfinal():
    Rating_avg = getRating_avg()
    final = pd.pivot_table(Rating_avg, values='adg_rating',
                           index='userId', columns='movieId')
    return final


def getfinal_movie():
    final = getfinal()
    final_movie = final.fillna(final.mean(axis=0))
    return final_movie


def getfinal_user():
    final = getfinal()
    final_user = final.apply(lambda row: row.fillna(row.mean()), axis=1)
    return final_user


class traningCollaborative1(APIView):
    def get(self, request):
        final_movie = getfinal_movie()
        cosine = cosine_similarity(final_movie)
        savetxt('array.txt', cosine, delimiter=',')
        newcosin = json.dumps(list(cosine))
        return Response(json.loads(newcosin))


class traningCollaborative2(APIView):
    def get(self, request):
        final_user = getfinal_user()
        b = cosine_similarity(final_user)
        savetxt('arrayitem.txt', b, delimiter=',')
        newcosin = json.dumps(list(b))
        return Response(json.loads(newcosin))


def getsimilarity_with_movie():
    cosine = np.loadtxt("array.txt")
    final_movie = getfinal_movie()
    final_user = getfinal_user()
    np.fill_diagonal(cosine, 0)
    similarity_with_movie = pd.DataFrame(cosine, index=final_movie.index)
    similarity_with_movie.columns = final_user.index
    return similarity_with_movie


def getsimilarity_with_user():
    b = np.loadtxt("arrayitem.txt")
    final_user = getfinal_user()
    np.fill_diagonal(b, 0)
    similarity_with_user = pd.DataFrame(b, index=final_user.index)
    similarity_with_user.columns = final_user.index
    return similarity_with_user


def find_n_neighbours(df, n):
    order = np.argsort(df.values, axis=1)[:, :n]
    df = df.apply(lambda x: pd.Series(x.sort_values(ascending=False)
                                      .iloc[:n].index,
                                      index=['top{}'.format(i) for i in range(1, n+1)]), axis=1)
    return df


def getsim_user_30_u():
    similarity_with_user = getsimilarity_with_user()
    sim_user_30_u = find_n_neighbours(similarity_with_user, 30)
    return sim_user_30_u


def getsim_user_30_m():
    similarity_with_movie = getsimilarity_with_movie()
    sim_user_30_m = find_n_neighbours(similarity_with_movie, 30)
    return sim_user_30_m


def Collaborative(user):
    Rating_avg = getRating_avg()
    Rating_avg = Rating_avg.astype({"movieId": str})
    Movie_user = Rating_avg.groupby(
        by='userId')['movieId'].apply(lambda x: ','.join(x))
    check = getcheck()
    Movie_seen_by_user = check.columns[check[check.index == user].notna(
    ).any()].tolist()
    sim_user_30_m = getsim_user_30_m()
    a = sim_user_30_m[sim_user_30_m.index == user].values
    b = a.squeeze().tolist()
    d = Movie_user[Movie_user.index.isin(b)]
    l = ','.join(d.values)
    Movie_seen_by_similar_users = l.split(',')
    Movies_under_consideration = list(
        set(Movie_seen_by_similar_users) - set(list(map(str, Movie_seen_by_user))))
    Movies_under_consideration = list(map(int, Movies_under_consideration))

    score = []
    final_movie = getfinal_movie()
    Mean = getMean()
    movies = getmovies()
    similarity_with_movie = getsimilarity_with_movie()
    for item in Movies_under_consideration:
        c = final_movie.loc[:, item]
        d = c[c.index.isin(b)]
        f = d[d.notnull()]
        avg_user = Mean.loc[Mean['userId'] == user, 'rating'].values[0]
        index = f.index.values.squeeze().tolist()
        corr = similarity_with_movie.loc[user, index]
        fin = pd.concat([f, corr], axis=1)
        fin.columns = ['adg_score', 'correlation']
        fin['score'] = fin.apply(
            lambda x: x['adg_score'] * x['correlation'], axis=1)
        nume = fin['score'].sum()
        deno = fin['correlation'].sum()
        final_score = avg_user + (nume / deno)
        score.append(final_score)
    data = pd.DataFrame(
        {'movieId': Movies_under_consideration, 'score': score})
    top_5_recommendation = data.sort_values(
        by='score', ascending=False).head(5)
    Movie_Name = top_5_recommendation.merge(movies, how='inner', on='movieId')
    Movie_Names = Movie_Name.Title.values.tolist()
    return Movie_Names


def getmaxrating(user_id):
    df = getmerge()
    user_df = df.loc[df["userId"] == user_id]
    usernew = user_df.groupby("Title").agg(
        {"rating": "max", "timestamp": "max"}).sort_values("rating", ascending=False).head(5)
    return usernew.index


def getmaxfilm():
    wibk = getfilm()
    filmMax = wibk.groupby("Title").agg({"vote_average": "max"}).sort_values(
        "vote_average", ascending=False).head(10)
    return filmMax.index


def recommend_movies_based_on_plot(movie_input):
    similarity = np.load("data.npy")

    df2 = getmovie()

    mapping = pd.Series(df2.index, index=df2['Title'])

    movie_index = mapping[movie_input]

    if (type(movie_index) == np.int64):
        similarity_score = sorted(
            list(enumerate(similarity[movie_index])), key=lambda x: x[1], reverse=True)
    else:
        similarity_score = sorted(
            list(enumerate(similarity[movie_index[0]])), key=lambda x: x[1], reverse=True)

    similarity_score = similarity_score[1:10]
    # print(similarity_score)

    # return movie names using the mapping series

    movie_indices = [i[0] for i in similarity_score]

    return (df2['Title'].iloc[movie_indices])


def Based(user_id):
    usernew = getmaxrating(user_id)
    result = []
    for movie_input in usernew:
        # print(movie_input)
        # print(recommend_movies_based_on_plot(movie_input))
        result.append(list(recommend_movies_based_on_plot(movie_input)))

    res = []
    for i in result:
        # print(i)
        for j in i:
            if j not in res:
                res.append(j)
    return list(res)


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        return (a_set & b_set)
    else:
        return "NAN"


def Recomender(user_id):
    maxrating = getmaxrating(user_id)
    if maxrating.size == 0:
        return list(getmaxfilm())
    else:
        res = common_member(Based(user_id), Collaborative(user_id))
        if res == 'NAN':
            return list(Based((user_id)))
        else:
            return list(res)


class getRecomender(APIView):
    def get(self, request, pk):
        result = list(Recomender(0))
        print(type(result))
        newresult = json.dumps(result)
        print(type(newresult))
        return Response(json.loads(newresult))


class getMaxFilm(APIView):
    def get(self, request):
        movies = film.objects.all().values_list('id', 'title', 'description', 'rate')
        newmovies = list(movies)
        print(newmovies)
        # print(movies)
        rating = review_of_film.objects.all().values_list(
            'id', 'times_tamp', 'precent_rate')
        # print(rating)
        Maxfilm = list(getmaxfilm())
        newMax = json.dumps(Maxfilm)
        return Response(json.loads(newMax))


class expertMovie(APIView):
    def get(self, request):
        movies = film.objects.all()
        response = HttpResponse(' ')
        response['Content-Disposition'] = 'attachment; filename=students.csv'
        with open('movies.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
        # writer = csv.writer(response)
            writer.writerow(['movieId', 'Title', 'Plot', 'vote_average'])
            studs = movies.values_list('id', 'title', 'description', 'rate')
            for std in studs:
                print([s for s in std])
                writer.writerow(str(s) for s in std)
        return Response('finall')


class expertRate(APIView):
    def get(self, request):
        rate = review_of_film.objects.all()
        response = HttpResponse(' ')
        response['Content-Disposition'] = 'attachment; filename=students.csv'
        with open('rate.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['userId', 'movieId', 'rating'])
            studs = rate.values_list('users', 'films', 'precent_rate')
            for std in studs:
                print([str(s, 'utf-8') for s in std])
                writer.writerow([str(s, 'utf-8') for s in std])
        return Response('final')
