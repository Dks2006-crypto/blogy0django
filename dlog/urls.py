from django.urls import path, include
from .import views

app_name = 'dlog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<slug:slug>/', views.details, name='details')
]