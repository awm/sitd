"""
Declaration for SITD document handling application.

SPDX-License-Identifier: MPL-2.0
Copyright (c) 2021 Andrew MacIsaac
"""
from django.apps import AppConfig

class SitdDocumentsConfig(AppConfig):
    """
    Document handling application configuration.
    """
    name = 'sitd_documents'
    verbose_name = "SITD Documents"
