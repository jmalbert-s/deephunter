"""
WSGI config for deephunter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Inject OS trust store into Python's ssl before any HTTPS connections
try:
    import truststore
    truststore.inject_into_ssl()
except Exception:
    # Optionally log; don’t fail startup just for this
    pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deephunter.settings')

application = get_wsgi_application()
