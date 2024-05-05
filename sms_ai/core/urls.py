from django.urls import path
from . import views



urlpatterns = [
    path('sitters/', views.sitter_list, name='sitter_list'),
    path('sitters/<int:pk>/', views.sitter_detail, name='sitter_detail'),
    path('sitters/create/', views.sitter_create, name='sitter_create'),
    path('sitters/<int:pk>/update/', views.sitter_update, name='sitter_update'),
    path('sitters/<int:pk>/delete/', views.sitter_delete, name='sitter_delete'),
    
    
    path('dolls/', views.doll_list, name='doll_list'),
    path('dolls/<int:pk>/', views.doll_detail, name='doll_detail'),
    path('dolls/create/', views.doll_create, name='doll_create'),
    path('dolls/<int:pk>/update/', views.doll_update, name='doll_update'),
    path('dolls/<int:pk>/delete/', views.doll_delete, name='doll_delete'),
]
