from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

import requests

# Create your views here.
class Covid19ReportViews(View):
    def get(self, request):
        r = requests.get('https://covid19.th-stat.com/api/open/today')
        data = r.json()
        new_confirmed = data['NewConfirmed']
        return HttpResponse(f'NewConfirmed: {new_confirmed}')