from django.urls import path
from .views import test_view,detail_view


urlpatterns = [
    path('', test_view),
    path('<id>', detail_view , name="detail"),
]
