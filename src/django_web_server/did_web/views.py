from django.http import HttpResponseNotFound, JsonResponse
import json


def index(request):
    try:
        with open('data/did.json') as f:
            did_web_json = json.load(f)
    except Exception as e:
        print('Error: Unable to open did.json file')
        return HttpResponseNotFound()

    return JsonResponse(did_web_json)
