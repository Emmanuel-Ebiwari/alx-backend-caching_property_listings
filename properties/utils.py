from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
import logging

logger = logging.getLogger(__name__)

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

def get_redis_cache_metrics():
    """
    Retrieve and analyze Redis cache
    hit or miss metrics.
    """
    conn = get_redis_connection("default")
    info = conn.info()

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)

    total = hits + misses
    hit_ratio = (hits / total) if total > 0 else None

    metrics = {
        "keyspace_hits": hits,
        "keyspace_misses": misses,
        "hit_ratio": hit_ratio,
    }

    logger.info(f"Redis Cache Metrics: {metrics}")
    return metrics

