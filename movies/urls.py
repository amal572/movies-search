"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from movies.views import get
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('' , get),
    path('admin/', admin.site.urls),
    path('user/', include('user.url')),
    path('category/', include('categories.url')),
    path('film/', include('film.url')),
    path('actors/', include('actors.url')),
    path('interact/', include('interact.url')),
    path('review/', include('review.url')),
    path('search/', include('search.url')),
    path('director/', include('director.url')),
    path('actorfilm/', include('actorfilm.url')),
    path('origin/', include('origin.url')),
    path('categoriesfilm/', include('categoriesfilm.url')),
    path('Recomender/', include('Recomender.url')),
    path('dsearch/', include('dsearch.url')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
