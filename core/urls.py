from django.urls import path
from .views import index, semester, questions, search_results

urlpatterns = [
    path('', index, name='index' ),
    path('sem', semester),
    path('ques', questions),
    path('search-results', search_results, name='search_results')
]