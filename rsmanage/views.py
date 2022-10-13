from django.shortcuts import render

# Create your views here.

from django.views.generic.edit import UpdateView
from rsmanage.models import Resource


class RsUpdateView(UpdateView):
    template_name = 'test.html'
    # success_url = ''
    model = Resource
    fields = ['resource_rsa']
    # pk_url_kwarg = 'resource_hostname'

