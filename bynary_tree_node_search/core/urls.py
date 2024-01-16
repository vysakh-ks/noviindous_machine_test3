from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add_node',views.add_node,name='add_node'),
    path('search_node',views.search_node,name='search_node'),
    
    
]
