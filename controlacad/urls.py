from django.contrib import admin
from django.urls import path
from Login import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from Login.views import SignupView
from edificios.views import EdificioPage, EdificioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',views.HomePage,name='inicio'),
    path('',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('reset-password/',PasswordResetView.as_view(),name='reset-password'),
    path('password-reset-done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('edificio/', EdificioPage),
    path('edificio/crear/', EdificioView.as_view(),name='edificio_crear'),
]

