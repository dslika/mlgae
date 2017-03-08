"""
WSGI config for mlgae project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

from mlgae.boot import fix_path

fix_path()

import os

from djangae.wsgi import DjangaeApplication
from django.core.wsgi import get_wsgi_application

# settings = "mlgae.settings_live" if on_production() else "mlgae.settings"
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mlgae.settings")

application = DjangaeApplication(get_wsgi_application())
