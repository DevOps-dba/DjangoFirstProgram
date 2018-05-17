# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.


def hello(request):
    return render(request, "myapp/hello.html", {"var": 2})


def article(request, id):
    cursor = connection.cursor()
    select_test_sql = "SELECT fname,lname FROM person WHERE age > 30 limit 3;"
    cursor.execute(select_test_sql)
    result = cursor.fetchall()
    text = "Displaying article Number: %s" % id
    return HttpResponse(result)
