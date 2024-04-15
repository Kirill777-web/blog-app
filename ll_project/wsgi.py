"""
WSGI config for ll_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# ll_project/wsgi.py
from django.core.wsgi import get_wsgi_application
import os
import sys
print("Current PYTHONPATH:", sys.path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'll_project.settings')

application = get_wsgi_application()
print("DJANGO_SETTINGS_MODULE:", os.getenv("DJANGO_SETTINGS_MODULE"))
print("Current PYTHONPATH:", os.sys.path)
