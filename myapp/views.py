# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import query
import json

# Create your views here.


def hello(request):
    return render(request, "myapp/hello.html", {})


def article(request, id):
    text = "Displaying article Number: %s" % id
    return HttpResponse(text)


def mysql_test(request):
    select_test_sql = "SELECT fname,lname FROM person WHERE age > 30 limit 3;"
    result = query(select_test_sql, 'default')
    # return HttpResponse(result)
    return HttpResponse(json.dumps(result), content_type="application/json")


def index(request):
    return render(request, "myapp/index.html")
