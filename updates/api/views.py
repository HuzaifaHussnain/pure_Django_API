import json
from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel
from django.views.decorators.csrf import csrf_exempt
from updates.forms import UpdateModelForm
from updates.utils import is_json

class UpdateModelDetailApiView(View):
	def get_object(self, id=None):
		try:
			obj = UpdateModel.objects.get(id=id)
		except UpdateModel.DoesNotExist:
			obj = None
		return obj

	def get(self, request, id, *args, **kwargs):	# GET api/updates/1
		obj = self.get_object(id)
		if obj is None:
			json_data = json.dumps({'message': 'Object not found'})
		else:
			json_data = obj.serialize()
		return HttpResponse(json_data, content_type='application/json')	

	def post(self, request, *args, **kwargs):	# POST api/updates/
		print('post')
		json_data = json.loads(request.body)
		form = UpdateModelForm(json_data)
		status_code = 200
		data = {}
		if form.is_valid():
			form.save()
		else:
			data = json.dumps(form.errors)
			status_code = 400
		return HttpResponse(data, content_type='application/json', status = status_code)	 

	def put(self, request, id, *args, **kwargs):	# PUT api/updates/1
		if not is_json(request.body):
			error_data = json.dumps({"message": "Invalid data sent, please send data in json format"})
			return HttpResponse(error_data, content_type='application/json', status=400)

		obj = self.get_object( id)
		if obj is None:
			error_data = json.dumps({"message": "Update Not found"})
			return HttpResponse(error_data, content_type='application/json', status=404)
		
		data = json.loads(obj.serialize())
		new_data = json.loads(request.body)
		for key, value in new_data.items():
			data[key] = value

		form = UpdateModelForm(data, instance=obj)
		if form.is_valid():
			obj = form.save(commit=True)
			obj_data = json.dumps(data)
			return HttpResponse(obj_data, content_type='application/json', status=200)

		if form.errors:
			data = json.dumps(form.errors)
			return HttpResponse(data, content_type='application/json', status=400)

	def delete(self, request, id, *args, **kwargs):		# DELETE api/updates/1
		obj = self.get_object(id=id)
		if obj is None:
			error_data = json.dumps({"message": "Update Not found"})
			return HttpResponse(error_data, content_type='application/json', status=404)
		deleted = obj.delete()
		if deleted:
			message = json.dumps({"message": "Successfully deleted the update"})
			return HttpResponse(message, content_type='application/json', status=200)
		else:
			message = json.dumps({"message": "Could not delete the update"})
			return HttpResponse(message, content_type='application/json', status=400)