from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('register/', views.signup, name='signup'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'),name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'),name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
     auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'),name='password_reset_complete'),

]