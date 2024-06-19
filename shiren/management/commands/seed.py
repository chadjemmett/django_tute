from django.core.management.base import BaseCommand, CommandError
from shiren.models import Item, Price
from shiren_price_list import items as all_items

class Command(BaseCommand):

    def handle(self, *args,**options):
        for key, value in all_items.items():
            if len(Price.objects.filter(price=key)) == 0:
                p = Price.objects.create(price=key)
                for i in value:
                    itom = Item.objects.filter(item_name=i)
                    if itom.exists():
                        if len(itom[0].price.filter(id=p.id)) == 0:
                            itom[0].price.add(p)

                    else:
                        itom2 = Item.objects.create(item_name=i, item_type=20)
                        itom2.price.add(p)
                        
