"""
WSGI config for dsm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application
from dsm import settings

path = settings.BASE_DIR


os.environ.setdefault('DJANGO_SETTINGS_MODULE', "dsm.settings")

application = get_wsgi_application()
