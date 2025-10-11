from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def api_home(reques, *args, **kwargs):
    return JsonResponse({"message": "hola, esta es la api"})