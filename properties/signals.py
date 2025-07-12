from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property

@receiver(post_delete, sender=Property)
@receiver(post_save, sender=Property)
def clear_property_cache(sender, instance, **kwargs):
    """
    Clear the cache for all properties when a property is saved or deleted.
    """
    cache.delete('all_properties')
