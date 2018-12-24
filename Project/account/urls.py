from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='registration'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('get/<str:username>/', views.get_profile, name='get'),
    path('edit/', views.update_profile, name='edit')
]
