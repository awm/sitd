"""
WSGI config for sitd project.

SPDX-License-Identifier: MPL-2.0
Copyright (c) 2021 Andrew MacIsaac

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitd.settings')

application = get_wsgi_application()
