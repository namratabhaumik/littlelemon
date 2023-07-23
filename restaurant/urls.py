# define URL route for index() view
from django.urls import path
from restaurant.views import index, get_menu, modify_menu, Modify_Menu

urlpatterns = [
    path('', index, name='index'),
    path('modify_menu_class_based', Modify_Menu.as_view(),
         name='modify_menu_class_based'),
    path('get_menu', get_menu, name='get_menu'),
    path('modify_menu', modify_menu, name='modify_menu'),
]
