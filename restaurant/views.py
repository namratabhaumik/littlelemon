import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from restaurant.models import Menu

# Create your views here.


def index(request):
    return render(request, 'restaurant/index.html', {})


@csrf_exempt
def get_menu(request):
    menu_list = Menu.objects.values()
    return JsonResponse({'data': list(menu_list)})


@csrf_exempt
def modify_menu(request):
    if request.method == 'POST':
        try:
            # If the request is in JSON format, load it
            data = json.loads(request.body)

            # Extract values from the data
            id = data.get('id')
            title = data.get('title')
            price = data.get('price')
            inventory = data.get('inventory')

            # Check if any data is missing
            if not all([id, title, price, inventory]):
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            # Check if item exists, and update if it does, otherwise create a new one
            menu_item, created = Menu.objects.update_or_create(
                id=id,
                defaults={'title': title, 'price': price,
                          'inventory': inventory}
            )

            if created:
                return JsonResponse({'status': 'Item Created', 'id': menu_item.id})
            else:
                return JsonResponse({'status': 'Item Updated', 'id': menu_item.id})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def delete_menu(request, id):
    if request.method == 'DELETE':
        try:
            # Try to find the item by its ID
            menu_item = Menu.objects.get(id=id)

            # Delete the item
            menu_item.delete()

            return JsonResponse({'status': 'Item Deleted'})
        except Menu.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
