import random

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def greet_user(request: HttpRequest) -> HttpResponse:
    response_text = "Hellow, User!"
    response = HttpResponse(response_text)

    return response


def generate_3_random_number(request: HttpRequest) -> HttpResponse:
    num1 = random.randint(0, 3)
    num2 = random.randint(0, 3)
    num3 = random.randint(0, 3)

    if num1 == num2 == num3:
        response_text = f"Выпали числа: {num1}, {num2}, {num3}; Победа, все 3 числа равны!"
    else:
        response_text = f"Выпали числа: {num1}, {num2}, {num3}; Повезет в следующий раз!"

    response = HttpResponse(response_text)

    return response
