from django.urls import path
from .import views



app_name="quiz"
urlpatterns = [
    path(''    , views.home_view   , name="home"),
    path('list', views.list_view   , name="list"),
    path('<id>', views.detail_view , name="detail"),
]
