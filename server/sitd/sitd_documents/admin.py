"""
Administrative configuration for SITD document app.

SPDX-License-Identifier: MPL-2.0
Copyright (c) 2021 Andrew MacIsaac
"""
from .models import Document, DocumentRevision

from django.contrib import admin

# Register models so that they appear in the admin interface.
admin.site.register(Document)
admin.site.register(DocumentRevision)
