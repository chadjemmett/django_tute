from django.db import models

class Price(models.Model):
    item_price = models.CharField(max_length=256)
    transaction = models.CharField(max_length=16)

    def __str__(self):
        return self.item_price

class Item(models.Model):
    item_name = models.CharField(max_length=256)
    item_type = models.CharField(max_length=256)
    price_id = models.ForeignKey(Price, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item_name}, {self.item_type}"

