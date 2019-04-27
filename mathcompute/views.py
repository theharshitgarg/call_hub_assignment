# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404, JsonResponse
from ratelimit.decorators import ratelimit


from .utils import timed_nth_fibonacci, timed_fast_nth_fibonacci, timed_nth_fibonacci_string


@ratelimit(key='get:q', method=ratelimit.ALL, rate='10/m', block=True)
def fibonacci_view(request):
    success = True
    value = None
    time = None
    errors = []
    try:
        query = int(request.GET.get("q"))
    except Exception as e:
        success = False
        errors.append({
            "description": str(e),
            "error": "incorrect input data",
        })
        print(e)

    ans = [0, 0]
    time, value, funcs = timed_nth_fibonacci_string(query)

    json = {
        "data": {
            "value": value,
            "sequence_number": request.GET.get("q"),
            "calculation_time": {
                "value": time,
                "unit": "seconds",
            }
        },
        "success": success,
    }

    return JsonResponse(json)


@ratelimit(key='get:q', method=ratelimit.ALL, rate='100/m', block=True)
def fibonacci_html_view(request):

    return render(request, 'fibonacci.html')
