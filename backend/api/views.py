from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from product.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from product.serializers import ProductSerializer
import json


# Create your views here.
@api_view(["POST"])
def api_home(request,*args, **kwargs):
    """
    DRF api View
    """
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save() 
        print(serializer.data)
        # data = serializer.data
        return Response(serializer.data)
    return Response({"Invalid" : "not good data"}, status=400)
    
    """
    This is  Django Rest Framework Model Serializers
    Ingest Data with Django Rest Framework Views
    
    """
# @api_view(["GET"])
# def api_home(request,*args, **kwargs):
#     """
#     DRF api View
#     """
#     instance = Product.objects.all().order_by("?").first()
#     data ={}
#     if instance:
#         data = ProductSerializer(instance).data
#         # data = model_to_dict(instance)
        
#         return Response(data)
        
        
    #     # data['id'] = model_data.id
    #     # data['title'] = model_data.title
    #     # data['content'] = model_data.content
    #     # data['price'] = model_data.price
    #     json_data_str = json.dumps(data)
        # return JsonResponse(data)
        
    
    # return HttpResponse(json_data_str, headers={"content-type":"application/json"})

# body = request.body
#     print(request.GET)
#     print(request.POST)
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data)
    
#     # data['headers'] = request.headers
#     print(request.headers)
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type