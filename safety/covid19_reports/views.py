from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

import requests

# Create your views here.
class Covid19ReportViews(View):
    def get(self, request):
        requests.get('https://covid19.th-stat.com/api/open/today')
        return HttpResponse()