"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .methods import get_mq_version
from rest_framework.response import Response
from rest_framework.views import APIView

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def versions(request):
    list = get_mq_version("http://10.2.0.245/Queues/MqService.svc?wsdl","http://192.53.244.121/queues/MqService.svc?wsdl")
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/services_table.html',
        {
            'header':["MQService","Fer3"],
            'rows': list
        }
    )
