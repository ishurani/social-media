from django.urls import path
from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from allauth.account import views as allauth_views
from allauth.account.views import confirm_email
# from django.views.decorators.csrf import csrf_exempt
app_name = 'accounts'


urlpatterns = [
    #url for login/signup
    path('signup/',allauth_views.SignupView.as_view(),name='account_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'),
    name='login'),

    #url for password change
    path('password/change/',allauth_views.PasswordChangeView.as_view(),name='account_change_password'),
    path('password/reset/',allauth_views.PasswordResetView.as_view(),name='account_reset_password'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('profile', views.profile, name='profile'),
    path('verification/', views.verification, name='verification'),
    #url for editing profile
    #path('profile/edit/',views.edit_profile, name='edit_profile'),
]
