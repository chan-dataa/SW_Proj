from django.urls import path
from pro import views
urlpatterns = [
    path('', views.index,name = 'index'),
]
