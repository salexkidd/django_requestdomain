#-*- coding:utf-8 -*-
"""
project name valiable to settings.py
"""
from django.contrib.sites.models import RequestSite


def request_domain(request, *args, **kwargs):
    """
    Set project_name to context
    """
    domain = RequestSite(request).domain
    return {"request_domain": domain}
