from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Estas en la página principal de Premiere")

def detail(request, question_id):
    return HttpResponse(f'Estas viendo la pregunta {question_id}')


def results(request, question_identifier):
    return HttpResponse(f'Estas viendo los resultados de la pregunta {question_identifier}')

def vote(request, question_id):
    return HttpResponse(f'Estas votando la pregunta {question_id}')