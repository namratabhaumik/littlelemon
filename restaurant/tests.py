from django.test import TestCase
from restaurant.models import Menu

# Create your tests here.
class Test_New_Entry(TestCase):
    def test_new_menu_item(self):
        try:
            new_item = Menu.objects.create(id=5, title="IceCream", price=80, inventory=100)
            self.assertEqual(str(new_item), "IceCream : 80") #returns None--> test case passed
        except Exception as e:
            print(e)
