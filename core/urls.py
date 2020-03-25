from django.urls import path
from .views import index, semester, questions

urlpatterns = [
    path('', index, name='index' ),
    path('sem', semester),
    path('ques', questions)
]