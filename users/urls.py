from django.urls import path
from .views import UserList


urlpatterns = [
    path('', UserList.as_view() ),
    path('cadastro', UserList.as_view())
]