from functools import wraps
from django.http import JsonResponse
from .models import ApiKey

def require_api_key(required_type='READ'):
    """
    Decorator to protect API endpoints.
    Accepts keys via the Authorization header (Bearer <key>) or X-API-Key header.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # 1. Extract the key from headers
            auth_header = request.headers.get('Authorization', '')
            api_key = request.headers.get('X-API-Key', '')
            
            if auth_header.startswith('Bearer '):
                api_key = auth_header.split(' ')[1]
                
            if not api_key:
                return JsonResponse({'error': 'Unauthorized', 'detail': 'API key is missing.'}, status=401)
                
            # 2. Verify the key exists and matches the required type
            try:
                key_obj = ApiKey.objects.get(key=api_key)
            except ApiKey.DoesNotExist:
                return JsonResponse({'error': 'Forbidden', 'detail': 'Invalid API key.'}, status=403)
                
            # A WRITE key can access READ endpoints, but not vice-versa
            if required_type == 'WRITE' and key_obj.key_type == 'READ':
                return JsonResponse({'error': 'Forbidden', 'detail': 'API key does not have write permissions.'}, status=403)
                
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
