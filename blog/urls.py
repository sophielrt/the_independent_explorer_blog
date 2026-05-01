from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('admin-dashboard/', views.dashboard, name='admin_dashboard'),
    path('admin-dashboard/add/', views.post_add , name='post_add'),
    path('admin-dashboard/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('admin-dashboard/delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]