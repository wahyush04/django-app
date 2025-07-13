from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Component
import json

@csrf_exempt
def component_list(request):
    if request.method == 'GET':
        components = list(Component.objects.values())
        return JsonResponse(components, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        component = Component.objects.create(**data)
        return JsonResponse({'id': component.id}, status=201)

@csrf_exempt
def component_detail(request, id):
    try:
        component = Component.objects.get(id=id)
    except Component.DoesNotExist:
        return JsonResponse({'error': 'gak ada pak'}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            'id': component.id,
            'name': component.name,
            'brand': component.brand,
            'category': component.category,
            'price': float(component.price),
            'stock': component.stock,
            'description': component.description,
        })

    elif request.method == 'PUT':
        data = json.loads(request.body)
        for key, value in data.items():
            setattr(component, key, value)
        component.save()
        return JsonResponse({'message': 'Component updated'})

    elif request.method == 'DELETE':
        component.delete()
        return JsonResponse({'message': 'Component deleted'})
