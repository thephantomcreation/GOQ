from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='index' ),

    path('see', SeeList.as_view()),
    path('plus2', PlusTwoList.as_view()),


    #urls for csit 1 to 8 semester 
    path('csit1', Csit1List.as_view()),
    path('csit2', Csit2List.as_view()),
    path('csit3', Csit3List.as_view()),
    path('csit4', Csit4List.as_view()),
    path('csit5', Csit5List.as_view()),
    path('csit6', Csit6List.as_view()),
    path('csit7', Csit7List.as_view()),
    path('csit8', Csit8List.as_view()),

    
    #urls for BIM 1 to 8 semester
    path('bim1', BIM1List.as_view()),
    path('bim2', BIM2List.as_view()),
    path('bim3', BIM3List.as_view()),
    path('bim4', BIM4List.as_view()),
    path('bim5', BIM5List.as_view()),
    path('bim6', BIM6List.as_view()),
    path('bim7', BIM7List.as_view()),
    path('bim8', BIM8List.as_view()),

    #urls for BHM 1 to 8 semester
    path('bhm1', BHM1List.as_view()),
    path('bhm2', BHM2List.as_view()),
    path('bhm3', BHM3List.as_view()),
    path('bhm4', BHM4List.as_view()),
    path('bhm5', BHM5List.as_view()),
    path('bhm6', BHM6List.as_view()),
    path('bhm7', BHM7List.as_view()),
    path('bhm8', BHM8List.as_view()),

    #urls for BCA 1 to 8 semester
    path('bca1', BCA1List.as_view()),
    path('bca2', BCA2List.as_view()),
    path('bca3', BCA3List.as_view()),
    path('bca4', BCA4List.as_view()),
    path('bca5', BCA5List.as_view()),
    path('bca6', BCA6List.as_view()),
    path('bca7', BCA7List.as_view()),
    path('bca8', BCA8List.as_view()),


]