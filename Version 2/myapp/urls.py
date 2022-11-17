
from django.contrib import admin
from django.urls import path,include
from myapp.spa.views import SpaView
from myapp.user_access.views import UserAccessView
from django.contrib.auth import views as auth_views
from myapp.register import views
from myapp.LoginSystem.views import logout_user
from Club.views import load_clubs
from myapp.LoginSystem.models import LoginForm
from django.conf import settings
from django.conf.urls.static import static 
from Club.views import club_form
from emailsystem.views import emailing
urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", SpaView, name="spa"),
    # path("home",GetRandomClub, name="spa"),
    # path("login/", auth_views.LoginView.as_view(),name='login'),
    # path('login/', include(''))
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(
            template_name="login.html",
            authentication_form=LoginForm
            ),
        name='login'
),
    path("register/", views.register_request, name="register"),
    path('club/<str:name>', load_clubs, name = "club"),
    path('email/<str:email>-<str:name>-<str:from>',emailing),
    path("logout/", logout_user,name="logout"),
    path("Create-Club/", club_form, name='form'),
    path("accounts/", include("django.contrib.auth.urls")), 
    # path("Images/",index, name="Images")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
