from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def course_list(request):
    return HttpResponse("<h1>Hola Mundo desde la lista de cursos</h1>")

def course_detail(request):
    return HttpResponse("<h1>Hola Mundo desde el detalle del curso</h1>")

def course_lessons(request):
    return HttpResponse("<h1>Hola Mundo desde las lecciones del curso</h1>")