from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>', views.user_wishes, name='user'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('add/<int:user_id>', views.add_item, name='add'),
    path('<int:user_id>/delete', views.delete_item, name='delete'),
    path('<int:user_id>/edit', views.edit_item, name='edit'),
    path('<int:user_id>/<int:item_id>/save', views.save_item, name='save'),
]
