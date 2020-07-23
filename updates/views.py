import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.views.generic import View

from .models import Update

# Create your views here.

def update_model_detail_view(request):
	data = {
		"count": 5,
		"update": "Some new content"
	}
	return JsonResponse(data)

def json_data_update(request):
	data = {
		"count": 7,
		"update": "This data is converted using python's JSON library."
	}
	json_data = json.dumps(data)
	return HttpResponse(json_data, content_type='application/json')

class SerializedListView(View):
	def get(self, request, *args, **kwargs):
		query_set = Update.objects.all()
		json_data = serialize("json", query_set, fields=('user', 'content'))
		return HttpResponse(json_data, content_type='application/json')