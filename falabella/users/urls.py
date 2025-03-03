from django.urls import path
from .views import UserListCreateView

urlpatterns = [
    path('users/',UserListCreateView.as_view(),name='user-list'),
    path('users/<int:pk>/',UserListCreateView.as_view(),name='user-detail'),
]
