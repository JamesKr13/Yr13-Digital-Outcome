"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from myapp.spa.views import SpaView
from myapp.user_access.views import UserAccessView
from django.contrib.auth import views as auth_views
from myapp.register import views
from myapp.LoginSystem.views import logout_user
from Club.views import load_clubs
from myapp.LoginSystem.models import UserLoginForm
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path("admin/", admin.site.urls),
    path("home", SpaView, name="spa"),
    # path("home",GetRandomClub, name="spa"),
    # path("login/", auth_views.LoginView.as_view(),name='login'),
    # path('login/', include(''))
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name="login.html",
            authentication_form=UserLoginForm
            ),
        name='login'
),
    path("register/", views.register_request, name="register"),
    path('club/<str:name>', load_clubs, name = "club"),
    path("logout/", logout_user,name="logout"),
    # path("Images/",index, name="Images")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
