from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest


def bad_response(request: HttpRequest):
    return HttpResponseBadRequest("Lomde lag gaye ")


def test_page(request: HttpRequest):
    list_people = [
        {"name": "harshit", "age": 21},
        {"name": "Tiwari", "age": 2},
        {"name": "Samosa", "age": 22},
        {"name": "billa", "age": 21},
    ]

    veges = ["cucumber", "potato", "tomato", "broccoli"]
    return render(
        request,
        template_name="test.html",
        context={"list_people": list_people, "vegetable": veges, "name": "harshit"},
    )


def home_page(request):

    return render(request=request, template_name="home.html")


# Create your views here.
