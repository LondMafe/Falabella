from django.urls import path
from .views import UserListCreateView, UserDetailView, ChangePasswordView

urlpatterns = [
    path('users/',UserListCreateView.as_view(),name='user-list'),
    path('users/<int:pk>/',UserListCreateView.as_view(),name='user-detail'),
    path('users/change_password/', ChangePasswordView.as_view(), name='change_password'),
]
