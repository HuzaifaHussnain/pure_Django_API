"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from updates.views import update_model_detail_view, json_data_update, SerializedListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', update_model_detail_view, name = None),
    path('json_data_update', json_data_update, name = None),
    path('serialized_list_view', SerializedListView.as_view(), name=None)

]
