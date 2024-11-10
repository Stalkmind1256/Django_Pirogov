from django.urls import path
from . import views

urlpatterns = [
    path('', views.billboards_list, name='billboards_list'),
    path('billboard/<int:pk>/', views.billboards_detail, name='billboards_detail'),
    path('billboard/new', views.billboard_new, name='billboard_new'),
    path('billboard/<int:pk>/edit/', views.billboards_edit, name='billboards_edit'),
    path('custom-admin/',views.admin_panel, name='admin_panel')
]