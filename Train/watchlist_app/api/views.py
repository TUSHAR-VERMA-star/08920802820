from django.shortcuts import render
from django.http import HttpResponse
import uuid
import secrets
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CompanySerializer

class CompanyView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            response_from_server = self.send_data_to_external_server(data)
            response_data = {
                "companyName": serializer.validated_data["companyName"],
                "clientId": response_from_server.get("clientId"),
                "clientServer": response_from_server.get("clientServer"),
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_data_to_external_server(self, data):
        return {
            "clientId": uuid.uuid4(),
            "clientServer": secrets.token_hex(10),
        }

class TrainListView(APIView):
    def get(self, request, *args, **kwargs):
        api_url = "http://20.244.56.144/train/trains"

        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Failed to fetch data from the API"}, status=response.status_code)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TrainListItemView(APIView):
    def get(self, request,id, *args, **kwargs):
        api_url = f"http://20.244.56.144/train/trains/{id}"

        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Failed to fetch data from the API"}, status=response.status_code)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def showList(request):
    return HttpResponse("OKAY")