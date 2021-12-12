from django.contrib import admin
from django.urls import path
from mini_app.views import home,news,weather,about_us,to_do,delete,createtask
from mini_auth.views import sign_up,user_login,user_logout,main,forgot_pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",main,name="main"),	
    path("home",home,name="home"),
    path("news",news,name="news"),
    path("weather",weather,name="weather"),
    path("to_do",to_do,name="to_do"),
    path("about_us",about_us,name="about_us"),
    path("sign_up",sign_up,name="sign_up"),
    path("user_login",user_login,name="user_login"),
    path("user_logout",user_logout,name="user_logout"),
    path("forgot_pass",forgot_pass,name="forgot_pass"),
    path(r'^delete/(?P<t>.*)$',delete,name="delete"),
    path("createtask",createtask,name="createtask"),
]

