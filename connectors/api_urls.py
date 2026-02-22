from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.get_connectors, name='api_connectors'),
    path('<int:pk>/', api_views.get_connector, name='api_connector_detail'),
]
