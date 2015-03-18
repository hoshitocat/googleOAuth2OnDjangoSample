# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse, render

def index(request):  # index.html的な役回り
    # return HttpResponse("Hello, World")
    return render(request, 'index.html')

def detail(request, sample_app_id):  # url:/polls/1/で表示
    return HttpResponse("You're looking at sample_app %s." % sample_app_id)
def results(request, sample_app_id):  # url:/polls/1/results/で表示
    return HttpResponse("You're looking at the results of sample_app %s." % sample_app_id)
def vote(request, sample_app_id):  # url:/polls/1/vote/で表示
    return HttpResponse("You're voting on sample_app %s." % sample_app_id)
