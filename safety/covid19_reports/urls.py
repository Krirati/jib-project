# from django.contrib import admin
from django.urls import path

from .views import Covid19ReportViews

urlpatterns = [
    path('', Covid19ReportViews.as_view()),
]
