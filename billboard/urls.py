from django.urls import path
from . import views

urlpatterns = [
    path('', views.billboards_list, name='billboards_list'),
    path('billboard/<int:pk>/', views.billboards_detail, name='billboards_detail'),
    path('billboard/new', views.billboard_new, name='billboard_new'),
    path('billboard/<int:pk>/edit/', views.billboards_edit, name='billboards_edit'),
    path('custom-admin/', views.admin_panel, name='admin_panel'),
    path('billboards/manage/', views.billboards_manage, name='billboards_manage'),
    path('billboard/delete/', views.billboard_delete_ajax, name='billboard_delete_ajax'),  # Удаление через AJAX
]