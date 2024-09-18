from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views

from .views import SignUpView

app_name = 'accounts'
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('password-change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('accounts:password_change_done')),
         name='password_change'),
]
