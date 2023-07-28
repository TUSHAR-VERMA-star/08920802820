from django.shortcuts import render
from django.http import HttpResponse
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

def showList(request):
    return HttpResponse("OKAY")

class NumbersView(APIView):
    def get(self, request, *args, **kwargs):
        urls = request.query_params.getlist('url')
        results = {'numbers': []}
        for url in urls:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    for i in response.json()['numbers']:
                        # print(i)
                        results['numbers'].append(i)
                else:
                    pass
            except Exception as e:
                pass
        sorted_numbers = sorted(results['numbers'])
        numbers_set = set(sorted_numbers)
        unique_sorted_numbers = list(numbers_set)
        results['numbers'] = unique_sorted_numbers
        return Response(results, status=status.HTTP_200_OK)
