"""
URLs published from SITD document app.

SPDX-License-Identifier: MPL-2.0
Copyright (c) 2021 Andrew MacIsaac
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
