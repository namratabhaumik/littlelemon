import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from restaurant.models import Menu

# Create your views here.
def index(request):
    return render(request, 'restaurant/index.html', {})


def get_menu(request):
    #print(Menu.objects)
    menu_list = Menu.objects.values() #returns an itrable of dict
    #print(type(menu_list)) #<class 'django.db.models.query.QuerySet'>
    # for menu in menu_list:
    #     print(type(menu)) #<class 'dict'>, can't access any other funcs inside the model class
    
    # menu_obj = Menu.objects.all() #returns an iterable of model class obj
    # #print(type(menu_obj)) #<class 'django.db.models.query.QuerySet'>
    # for menu in menu_obj:
    #     print(type(menu)) #<class 'restaurant.models.Menu'>, can access every class attr
        #print(menu.get_item()) #normal func call w/ class obj
        #print(menu) #calls inbuilt func like __str__(self) if defined
    return JsonResponse({'data': list(menu_list)})


#For form-data input
@csrf_exempt
def modify_menu(request):
    id = json.loads(request.POST.get('id'))
    title = json.loads(request.POST.get('title'))
    price = json.loads(request.POST.get('price'))
    inventory = json.loads(request.POST.get('inventory'))

    #saving new items + modifying saved items in django admin (db)
    new_menu = Menu(id=id, title=title, price=price, inventory=inventory)
    new_menu.save()

    return JsonResponse({'status':'Success'})


#For JSON data input
class Modify_Menu(APIView):
    def post(self,request):
        id = request.data.get('id')
        title = request.data.get('title')
        price = request.data.get('price')
        inventory = request.data.get('inventory')

        new_menu = Menu(id=id, title=title, price=price, inventory=inventory)
        new_menu.save()

        return JsonResponse({'status':'Success'})
