
from django.urls import path

from users.views import RegisterUser, LogoutView

urlpatterns=[
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]