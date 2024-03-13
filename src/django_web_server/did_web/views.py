from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
import json


def index(request):
    try:
        with open('../../did.json') as f:
            did_web_json = json.load(f)
            print(did_web_json)
    except Exception as e:
        print('Error: Unable to open did.json file')
        return HttpResponseNotFound()

    return JsonResponse(did_web_json)
