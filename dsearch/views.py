from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from film.models import categories,actors,Director,origin,categories_film
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db import connection
import csv
# Create your views here.
import time
import faiss
import numpy as np
import pandas as pd
import pickle
#from bert_score import score
from googletrans import Translator
from sentence_transformers import SentenceTransformer
import json

def getmoviedef():
    movies = pd.read_csv('movies.csv')
    #df2 = movies[["movieId","Release Year","Title" ,"Origin/Ethnicity" ,"Director","Cast","Genre","Plot"]]
    df = movies[['Title','Plot']]
    return df

def fetch_movie_info(dataframe_idx):
    df = getmoviedef()
    info = df.iloc[dataframe_idx]
    meta_dict = {}
    meta_dict['Title'] = info['Title']
    meta_dict['Plot'] = info['Plot'][:500]
    return meta_dict

def search(query, top_k, index, model):
    t = time.time()
    query_vector = model.encode([query])
    top_k = index.search(query_vector, top_k)
    top_k_ids = top_k[1].tolist()[0]
    top_k_ids = list(np.unique(top_k_ids))
    results =  [fetch_movie_info(idx) for idx in top_k_ids]
    return results


def translatorsearch1(query):
    translator = Translator()
    if ('\u0600' <= query <= '\u06FF' or
            '\u0750' <= query <= '\u077F' or
            '\u08A0' <= query <= '\u08FF' or
            '\uFB50' <= query <= '\uFDFF' or
            '\uFE70' <= query <= '\uFEFF' or
            '\U00010E60' <= query <= '\U00010E7F' or
            '\U0001EE00' <= query <= '\U0001EEFF'):
        res = translator.translate(query)
        result = res.text
         #print('yes')
    else:
        result = query

    return result


def finallsearch(query):
    #loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
    #print((loaded_model))
    resfinal = translatorsearch1(query)
    model = SentenceTransformer('msmarco-distilbert-base-dot-prod-v3')
    index = faiss.deserialize_index(np.load("test.npy"))
    print(index)
    t = time.time()
    query_vector = model.encode([query])
    top_k = index.search(query_vector, 4)
    top_k_ids = top_k[0].tolist()[0]
    top_k_ids = list(np.unique(top_k_ids))
    results = [fetch_movie_info(idx) for idx in top_k_ids]
    #results = search(resfinal, top_k=5, index=index, model=model)
    #ranked_results_bert = []
    #ref = [resfinal]
    #for cand in results:
     #   P, R, F1 = score([cand['Plot']], ref, lang='en')
       # ranked_results_bert.append({'Title': cand['Title'], 'Score': F1.numpy()[0]})

    return results


class searchApi(APIView):
    def get(self, request):
        print(str(a))
        query = "فيلم أكشن قائم على الذكاء الاصطناعي"
        #movies = pd.read_csv('example_file.csv')
        #print(movies)
        #ranked_results = finallsearch('فيلم أكشن قائم على الذكاء الاصطناعي')
        resfinal = translatorsearch1(query)
        model = SentenceTransformer('msmarco-distilbert-base-dot-prod-v3')
        index = faiss.deserialize_index(np.load("test.npy"))
        print(index)
        t = time.time()
        print(1)
        query_vector = model.encode([query])
        print(2)
        top_k = index.search(query_vector, 4)
        print(top_k)
        print(3)
        top_k_ids = top_k[1].tolist()[0]
        print(4)
        top_k_ids = list(np.unique(top_k_ids))
        print(5)
        print(top_k_ids)
        results = [fetch_movie_info(idx) for idx in top_k_ids]
        print(6)
        #results = search(resfinal, top_k=5, index=index, model=model)
        #ranked_results_bert = sorted(ranked_results, key=lambda x: x['Score'], reverse=True)
        print(type(results))
        Maxfilm = list(results)
        print(7)
        print(type(Maxfilm))
        print(Maxfilm)
        newMax = json.dumps(Maxfilm)
        print(8)
        print(newMax)
        return Response(newMax)