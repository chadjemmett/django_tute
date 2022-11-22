from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=256)
    item_type = models.CharField(max_length=256)
    buy_price = models.CharField(max_length=256)
    sell_price = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.item_name}, {self.item_type}, {self._buy_price}, {self.sell_price}"

