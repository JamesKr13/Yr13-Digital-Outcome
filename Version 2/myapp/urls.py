
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
    path("home/", SpaView, name="spa"),
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
