from django.http import JsonResponse
from django.core.files import File

from .models import Tree


def upload(request, id):
    t = Tree.objects.get(id=id)
    image = t.image_set.create(image=request.FILES.values()[0] if request.FILES else File(request))
    return JsonResponse({'status': 'lgtm', 'image_id': image.id})
