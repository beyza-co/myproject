from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('harita', map,name='harita'),
    path('neyenir', restaurant),
    path('PLAJLAR',beach),
    path('konaklama',hotel),
    
]
