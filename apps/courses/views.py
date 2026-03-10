from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def course_list(request):
    courses = [
        {
            'id':1,
            'level':'Principiante',
            'rating': 4.8,
            'course_title': 'Python: numero 1 rellenando las tarjetas de presentacion de forma dinamica',
            'instructor': 'Profesor 1',
            'course_image': 'images/curso_1.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/68.jpg',
        },
        {
            'id': 2,
            'level': 'Basic',
            'rating': 4,
            'course_title': 'Python: numero 2 rellenando las tarjetas de presentacion de forma dinamica',
            'instructor': 'Profesor 2',
            'course_image': 'images/curso_2.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/20.jpg',
        },
        {
            'id': 3,
            'level': 'Junior',
            'rating': 3.5,
            'course_title': 'Python: numero 3 rellenando las tarjetas de presentacion de forma dinamica',
            'instructor': 'Profesor 3',
            'course_image': 'images/curso_3.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/32.jpg',
        },
        {
            'id': 4,
            'level': 'Pro',
            'rating': 5,
            'course_title': 'Python: numero 4 rellenando las tarjetas de presentacion de forma dinamica',
            'instructor': 'Profesor 4',
            'course_image': 'images/curso_4.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/65.jpg',
        }
    ]
    return render(request, 'courses/courses.html', {
        'courses': courses
    })

def course_detail(request):
    return HttpResponse("<h1>Hola Mundo desde el detalle del curso</h1>")

def course_lessons(request):
    return HttpResponse("<h1>Hola Mundo desde las lecciones del curso</h1>")