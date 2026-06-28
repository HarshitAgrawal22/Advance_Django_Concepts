from django.shortcuts import render
import json
from basicapis.models import Student
from django.http import HttpRequest, JsonResponse, HttpResponse, HttpResponseBadRequest
from icecream import ic
from django.views.decorators.csrf import csrf_exempt


def bad_response(request: HttpRequest):
    return HttpResponseBadRequest("Lomde lag gaye ")


def test_page(request: HttpRequest):
    list_people = list(
        {"name": student.Name, "age": student.Age} for student in Student.objects.all()
    )
    ic(list_people)
    veges = ["cucumber", "potato", "tomato", "broccoli"]
    return render(
        request,
        template_name="test.html",
        context={"list_people": list_people, "vegetable": veges, "name": "harshit"},
    )


def home_page(request):

    return render(request=request, template_name="home.html")


# @csrf_exempt
def create_student(request: HttpRequest):
    if request.method == "POST":
        # Name = request.POST.get("name")
        # Age = request.POST.get("age")
        data: dict = json.loads(request.body)
        Name = data.get("Name")
        Age = data.get("Age")
        ic(Name)
        ic(Age)
        Student.objects.create(Name=Name, Age=Age)
        return JsonResponse({"status": 200, "response": "ok"})
    else:
        return JsonResponse({"status": 400, "response": "api failed"})
