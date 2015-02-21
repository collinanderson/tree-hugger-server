from django.http import JsonResponse
from django.core.files.base import ContentFile

from .models import Tree


def upload(request, id):
    t = Tree.objects.get(id=id)
    if request.FILES:
        image_file = request.FILES.values()[0]
    else:
        image_file = ContentFile(request.body)
        image_file.name = request.META['HTTP_FILENAME']
    image = t.image_set.create(image=image_file)
    return JsonResponse({
        'id': image.id,
        'image': image.image.url,
        'resource_uri': '/api/v1/image/%s/' % image.id,
        'type': image.type,
    })
