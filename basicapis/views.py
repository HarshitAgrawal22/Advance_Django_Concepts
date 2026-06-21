from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest


def bad_response(request: HttpRequest):
    return HttpResponseBadRequest("Lomde lag gaye ")


def page(request: HttpRequest):
    return render(request, "test.html")


# Create your views here.
