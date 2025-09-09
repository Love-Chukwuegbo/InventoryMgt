from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, ProductInventory

@receiver(post_save, sender=Product)
def update_or_create_inventory(sender, instance, created, **kwargs):

    product_quantity = getattr(instance, 'quantity', 1)

    if created:
        
        ProductInventory.objects.create(product=instance, quantity=product_quantity)
    else:
        inventory, inv_created = ProductInventory.objects.get_or_create(product=instance)
        if not inv_created:
           
            inventory.quantity += product_quantity
            inventory.save()
