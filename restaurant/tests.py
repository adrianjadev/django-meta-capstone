from django.test import TestCase
from .models import Menu, Booking

# Create your tests here.

class MenuTest(TestCase):
    
    def test_get_item(self):
        menu_item = Menu.objects.create(title="Cornsilog", price=25,inventory=100)
        self.assertEqual(str(menu_item), 'Cornsilog : 25')

