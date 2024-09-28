"""
URL configuration for Suppleez project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.shortcuts import redirect
from SuppleezApp.views import SignUpView,CustomLoginView,HomeView,LogoutView,HomeProfView,FormProfPageView,ListDemandesView,CoursView,ListDemandesArchiveView,erreur_404,erreur_500
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.views.static import serve



handler404 = erreur_404
handler500 = erreur_500

#django admin modification
admin.site.site_header = "Suppléance adminstration"
admin.site.site_title = "Page d'administrations des demandes de suppléance"
admin.site.index_title = "Bienvenue dans la page d'administration des demandes de suppléance de cours"
urlpatterns = [
    re_path(r'^static/(?P<path>.*)$',serve,{'document_root': settings.STATIC_ROOT}),
    path('signUp/', SignUpView.as_view(), name='signup-page'),
    path('login/', CustomLoginView.as_view(), name='login-prof'),
    path('home-prof/', HomeProfView.as_view(), name='home-prof'),
    path('formprof/', FormProfPageView.as_view(), name='form-prof'),
    path('list-demande/', ListDemandesView.as_view(), name='list-demande'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/logout/', lambda request: redirect('/logout/', permanent=False)),
    path('accounts/login/', lambda request: redirect('/login/', permanent=False)),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls,name='login-admin'),
    path('cours-prof/', CoursView.as_view(), name='cours-prof'),
    path('archive-prof/', ListDemandesArchiveView.as_view(), name='archive-prof'),
    

    path('', HomeView.as_view(), name='home-page'),
   

]
