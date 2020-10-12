from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [

    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
