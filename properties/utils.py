from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Fetch all properties from Redis cache.
    Cache it for 1 hour if not found.
    """
    properties = cache.get('all_properties')
    if properties is None:
        properties = Property.objects.all()
        cache.set('all_properties', properties, timeout=3600)

    return properties
