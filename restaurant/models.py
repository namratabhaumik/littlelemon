from django.db import models

# Create your models here.


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    def __str__(self):  # gets invoked while printing Menu obj, appears in the specified string format in django admin table
        return f'{self.title} : {str(self.price)}'
