from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:discussion_id>/', views.get_discussion, name = 'result')
]