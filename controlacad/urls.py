from django.contrib import admin
from django.urls import path
from Login import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from Login.views import SignupView, RolCreate, RolUpdate, RolModificar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('roles/<int:pk>/editar/',RolUpdate),
    path('roles/<int:pk>/modificar/',RolModificar),
    path('inicio/',views.HomePage,name='inicio'),
    path('roles/',views.RolPage,name='roles'),
    path('create-rol/',views.RolCreate,name='create_rol'),
    path('',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('reset-password/',PasswordResetView.as_view(),name='reset-password'),
    path('password-reset-done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
]

