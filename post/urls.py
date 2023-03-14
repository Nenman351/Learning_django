from django.urls import path
from . import views

urlpatterns = {
    path('hello/', views.hello, name=' hello'),
    path('greet/', views.greet, name=' greet'),
    path('play/', views.play, name=' play'),
    path('learn/', views.learn, name="learn"),
}
