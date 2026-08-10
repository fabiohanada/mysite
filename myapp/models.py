from django.db import models

# Create your models here.
class Item(models.Model):
    
        def __str__(self):
                return self.item_name
            
        item_name = models.CharField(max_length=200)
        item_desc = models.CharField()
        item_price = models.IntegerField()
        item_image = models.CharField(max_length=500, default='https://img.favpng.com/6/11/15/food-logo-cutlery-and-plate-icon-for-dining-kgzBem0K_t.jpg')