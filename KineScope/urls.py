"""KineScope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('films/', views.films, name='films'),

    path('film/<int:id>/', views.film, name='film'),
    path('user/', views.user, name='user'),
    path('actor/', views.actor, name='actor'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('film/add/', views.add_film, name='add_film'),
    path('actor/add/', views.add_actor, name='add_actor'),
    path('director/add/', views.add_director, name='add_director'),
    path('studio/add/', views.add_studio, name='add_studio'),
    path('award/add/', views.add_award, name='add_award'),

    path('films/<int:id>/edit/', views.edit_film, name='edit_film'),
    path('actors/<int:id>/edit/', views.edit_actor, name='edit_actor'),
    path('directors/<int:id>/edit/', views.edit_director, name='edit_director'),
    path('studios/<int:id>/edit/', views.edit_studio, name='edit_studio'),
    path('awards/<int:id>/edit/', views.edit_award, name='edit_award'),

    path('films/<int:id>/delete/', views.delete_film, name='delete_film'),
    path('actors/<int:id>/delete/', views.delete_actor, name='delete_actor'),
    path('directors/<int:id>/delete/', views.delete_director, name='delete_director'),
    path('studios/<int:id>/delete/', views.delete_studio, name='delete_studio'),
    path('awards/<int:id>/delete/', views.delete_award, name='delete_award'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)