from django.urls import include, re_path as url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path
#from django.urls.conf import include
from pages.views import  about_view, redirect_to_login_view
from users.views import  forgot_pwd_view, email_sent_view, user_changed_pwd_successfully_view, verify_code_view

from users.views import login_request,user_create_view, user_change_pwd_view,logout_request, reset_pwd_view

from clients.views import client_create_view

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', redirect_to_login_view),
    path('login/', login_request),
    path('register/', user_create_view),
    path('clients/', client_create_view),
    path('change-pwd/', user_change_pwd_view),
    path('change-pwd/done', user_changed_pwd_successfully_view),
    path('forgot-pwd/', forgot_pwd_view),
    path('forgot-pwd/sent/', email_sent_view),
    path('verify-code/', verify_code_view, name='verify-code'),
    path('reset-pwd/', reset_pwd_view),
    path('about/', about_view),
    path('logout/', logout_request)
    

]
