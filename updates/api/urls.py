from django.urls import path
from .views import UpdateModelDetailApiView

urlpatterns = [
	path('<int:id>', UpdateModelDetailApiView.as_view()), #api/updates/1
	path('', UpdateModelDetailApiView.as_view()) # for POST method
]
