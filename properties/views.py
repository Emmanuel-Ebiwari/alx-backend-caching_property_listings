from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .utils import get_all_properties
from django.views.decorators.http import require_GET

@cache_page(60 * 15)
@require_GET
def property_list(request):
    properties = list(get_all_properties().values())
    return JsonResponse({'data': properties}, safe=False)