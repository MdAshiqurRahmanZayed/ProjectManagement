
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register,logout_view,login_page

app_name='accounts'

urlpatterns = [
    path('login/',login_page, name='login'),
    path('logout/', logout_view, name='logout_page'),
    path('register/', register, name='register'),
]
