from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from config.decorators import require_api_key
from .models import Connector

def serialize_connector(connector):
    return {
        'id': connector.id,
        'name': connector.name,
        'description': connector.description,
        'installed': connector.installed,
        'enabled': connector.enabled,
        'domain': connector.domain,
    }

@require_api_key('READ')
@require_http_methods(["GET"])
def get_connectors(request):
    """Return a list of connectors."""
    connectors = Connector.objects.all()
    data = [serialize_connector(connector) for connector in connectors]
    return JsonResponse({'data': data})

@require_api_key('READ')
@require_http_methods(["GET"])
def get_connector(request, pk):
    """Return details of a specific connector."""
    connector = get_object_or_404(Connector, pk=pk)
    return JsonResponse({'data': serialize_connector(connector)})
