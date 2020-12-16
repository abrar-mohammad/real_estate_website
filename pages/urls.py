from django.urls import path
from . import views

urlpatterns = [
    # IMPORT VIEWS, fetch request from the views.__  and do what is written in the views funciton
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),

]
