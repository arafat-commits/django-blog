from django.contrib import admin # admin site visit korar jonno.
from django.views.generic import RedirectView
from django.urls import path, include

from users import views as user_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls), # admin site url route.
    path('blog/', include('blog.urls')),
    path('', RedirectView.as_view(url='blog/')), # bujhar kotha. See the comment at the end.

    # 'user_views' howate ei duto file e kebol 'users' app ti te thakbe. baki shob 'auth_views' ekshathe thakbe
    path('register/', user_views.register, name='register'), # function-based view(only 1 of 2 user_views)
    path('profile/', user_views.profile, name='profile'), # function-based view(only 2 of 2 user_views)

    # shob 'auth_views'. egulu thakbe "root project/templates/registration(folder)" er vetor.
    path('login/', 
    auth_views.LoginView.as_view(template_name='users/login.html'), 
    name='login'), # class-based views

    path('logout/', 
    auth_views.LogoutView.as_view(template_name='users/logout.html'), 
    name='logout'), # class-based view

    path('password-reset/', 
    auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
    name='password_reset'), # class-based view

    path('password-reset/done/', 
    auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
    name='password_reset_done'), # class-based view

    path('password-reset-confirm/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
    name='password_reset_confirm'), # class-based view

    path('password-reset-complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
    name='password_reset_complete'), # class-based view

    ]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
