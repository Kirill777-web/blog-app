"""
WSGI config for ll_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# ll_project/wsgi.py
import os
import sys
from django.core.wsgi import get_wsgi_application

# Print system path and current working directory
print('Current PYTHONPATH:', sys.path)
print('Current Working Directory:', os.getcwd())
print('Directory Listing:', os.listdir(os.getcwd()))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'll_project.settings')

application = get_wsgi_application()
