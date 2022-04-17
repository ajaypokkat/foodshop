from .models import *
from .views import *


def count(request):
    items_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct = cartlist.objects.filter(car_id=cart_id(request))
            cti = items.objects.all().filter(cart=ct[:1])
            for c in cti:
                items_count += c.qnty
        except cartlist.DoesNotExist:
            items_count = 0
        return dict(itc=items_count)
