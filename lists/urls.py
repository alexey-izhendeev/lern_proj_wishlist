from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>', views.user_wishes, name='user'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
