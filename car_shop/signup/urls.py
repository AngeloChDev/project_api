from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name="signup"

urlpatterns=[
    path("signup/", views.signup,name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), 
    path('logout/', views.CustomLogoutView.as_view(), name='logout'), 
    path('thankyou/', views.thankyou, name="thankyou" )
]

