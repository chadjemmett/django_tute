from django.db import models

class Item(models.Model):
    TYPE = [
            (10, 'Herb'),
            (20, 'Scroll'),
            (30, 'Bracelet'),
            (40, 'Jar'),
            (50, 'Staff'),
            ]
    item_name = models.CharField(max_length=256)
    item_type = models.IntegerField(choices=TYPE)
    buy_price = models.CharField(max_length=256)
    sell_price = models.CharField(max_length=256)
    found = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f"{self.item_name}, {self.item_type}, {self.buy_price}, {self.sell_price}"

