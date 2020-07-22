from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Update
# Create your views here.

def update_model_detail_view(request):
	data = {
		"count": 5,
		"update": "Some new content"
	}
	return JsonResponse(data)