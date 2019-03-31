from django.urls import path, include
from .views import RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='user/login.html'),
        name='login'
        ),
    path('login/', include('send_post.urls')),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='user/logout.html'),
        name='logout'
        ),
]
