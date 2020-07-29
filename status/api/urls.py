from django.urls import include
from django.contrib import admin
from django.urls import path
from .views import (
	StatusListSearchAPIView,
	StatusCreateAPIView,
	StatusDetailAPIView,
	StatusUpdateAPIView,
	StatusDeleteAPIView
	)


urlpatterns = [
	path('', StatusListSearchAPIView.as_view(), name=None),
    path('create/', StatusCreateAPIView.as_view(), name=None),
    path('detail/<int:id>', StatusDetailAPIView.as_view(), name=None),
    path('update/<int:id>', StatusUpdateAPIView.as_view(), name=None),
    path('delete/<int:id>', StatusDeleteAPIView.as_view(), name=None)
]
