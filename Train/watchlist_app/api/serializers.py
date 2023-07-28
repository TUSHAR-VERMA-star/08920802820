from rest_framework import serializers
from watchlist_app.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('companyName', 'ownerName', 'rollNo', 'ownerEmail', 'accessCode')
