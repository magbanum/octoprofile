from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', views.get_username, name="profile_page"),
    path('api/top-languages/', views.TopLanguages.as_view(), name="top-languages"),
    path('api/most-starred/', views.MostStarred.as_view(), name="most-starred"),
    path('api/stars-per-languages/', views.StarsPerLanguages.as_view(),
         name="stars-per-languages"),
]
