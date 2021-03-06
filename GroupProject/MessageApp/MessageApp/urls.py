"""MessageApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from pages import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url

urlpatterns = [
    path('', views.Views.home_view, name='home'),
    url(r'^$', views.HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
     url(r'^signup/$', views.Views.signup_view, name="signup"),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name="login"),
    url(r'^logout/$', LogoutView.as_view(template_name='pages/login.html'), name='logout'),
    url(r'^accounts/profile/', views.Views.profile_view, name='profile'),
    url(r'^create_thread/$', views.Views.create_thread, name='create_thread'),
    url(r'^create_message/$', views.Views.create_message, name='create_message'),
     url(r'^get_messages/$', views.Views.get_messages, name='get_messages'),

]