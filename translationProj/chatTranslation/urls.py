from django.urls import path
from . import views
urlpatterns = [
    path('chatTranslation/', views.chatTranslation, name='chatTranslation'),
    path('chatTranslation/signup', views.signup, name='signup'),
    path('chatTranslation/login', views.login, name='login'),
]
