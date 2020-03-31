from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index' ),
    path('see', SeeList.as_view()),
    path('plus2', PlusTwoList.as_view()),

]