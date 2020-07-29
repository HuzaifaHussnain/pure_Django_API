from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from status.models import Status
from .serializers import StatusSerializer

class StatusListAPIView(APIView):

	def get(self, request, format=None):
		qs = Status.objects.all()
		serialized_data = StatusSerializer(qs, many=True)
		return Response(serialized_data.data)


class StatusCreateAPIView(generics.CreateAPIView):
		queryset = Status.objects.all()
		serializer_class = StatusSerializer


class StatusDetailAPIView(generics.RetrieveAPIView):
		queryset = Status.objects.all()
		serializer_class = StatusSerializer
		lookup_field = 'id'

class StatusUpdateAPIView(generics.UpdateAPIView):
		queryset = Status.objects.all()
		serializer_class = StatusSerializer
		lookup_field = 'id'

class StatusDeleteAPIView(generics.DestroyAPIView):
		queryset = Status.objects.all()
		serializer_class = StatusSerializer
		lookup_field = 'id'