from django.urls import path
from Jonathan import views

urlpatterns = [
    path("", views.home, name="home"),
]
