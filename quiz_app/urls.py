from django.urls import path
from .import views



urlpatterns = [
    path('',views.home_view,name="home"),
    path('list',views.list_view,name="list"),
    path('<id>',views.detail_view,name="detail"),
    path('add_vote/',views.add_vote,name="add_vote"),
]