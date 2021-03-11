"""
URL endpoint handlers for SITD document app.

SPDX-License-Identifier: MPL-2.0
Copyright (c) 2021 Andrew MacIsaac
"""
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """
    Trivial endpoint for initial testing.

    :param request: HTTP request instance.
    :type request: HttpRequest
    :return: Response to the HTTP request.
    :rtype: HttpResponse
    """
    return HttpResponse("Hello, world!")
