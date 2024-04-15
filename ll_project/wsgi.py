"""
WSGI config for ll_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# ll_project/wsgi.py

from django.core.wsgi import get_wsgi_application
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug('Starting up...')
logger.debug(f'Current WORKDIR: {os.getcwd()}')
logger.debug(f'PYTHONPATH: {os.getenv("PYTHONPATH")}')
logger.debug(f'WSGI file location: {__file__}')
logger.debug(f'DJANGO_SETTINGS_MODULE: {os.getenv("DJANGO_SETTINGS_MODULE")}')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'll_project.settings')
application = get_wsgi_application()
print("Directory contents:", os.listdir('/opt/render/project/src'))
