# define URL route for index() view
from django.urls import path
from restaurant.views import index, get_menu, modify_menu, delete_menu

urlpatterns = [
    path('', index, name='index'),
    path('modify_menu', modify_menu,
         name='modify_menu'),
    path('get_menu', get_menu, name='get_menu'),
    path('delete_menu/<int:id>', delete_menu, name='delete_menu'),
]
