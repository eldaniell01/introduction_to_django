from django.shortcuts import render
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        #instance = serializer.save()
        #print(instance)
        return Response(serializer.data)
    return Response({'invalid': 'informacion no valida'}, status=400)