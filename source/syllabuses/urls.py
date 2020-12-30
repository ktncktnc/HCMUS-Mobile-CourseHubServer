from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:syllabus_id>/', views.get_syllabus, name = 'result')
]