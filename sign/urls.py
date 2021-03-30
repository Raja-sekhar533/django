from django.urls import path
from sign import views



app_name = 'sign'
urlpatterns = [
    path('register/',views.register, name="register"),
    path('user_login/', views.user_login, name="login")
]
