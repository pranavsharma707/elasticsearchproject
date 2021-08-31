
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers
from elasticapp.models import Publisher
from elasticapp.documents import PublisherDocument

import json

class PublisherDocumentSerializer(DocumentSerializer):

    location=serializers.SerializerMethodField()

    class Meta:
        model=Publisher
        document=PublisherDocument

        fields=(
            'id',
            'name',
            'address',
            'city',
            'state_province',
            'country',
            'website',
            'latitude',
            'longitude',
        )

    def get_location(self,obj):
        try:
            return obj.location.to_dict()
        except:
            return {} 

