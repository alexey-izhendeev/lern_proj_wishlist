from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('<user>', views.user_wishes, name='user'),
    path('<int:user_id>', views.user_wishes, name='user'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('add/<int:user_id>', views.add_item, name='add'),
    path('<int:user_id>/delete', views.delete_item, name='delete')
]
