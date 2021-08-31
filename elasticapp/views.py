from django.db.models.lookups import Lookup
from django.shortcuts import render

# Create your views here.
from django_elasticsearch_dsl_drf.constants import ( LOOKUP_FILTER_GEO_DISTANCE,)

from django_elasticsearch_dsl_drf.filter_backends import (FilteringFilterBackend, OrderingFilterBackend,CompoundSearchFilterBackend,)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

# Example app models
from elasticapp.documents import PublisherDocument
from elasticapp.serializers import PublisherDocumentSerializer

class PublisherDocumentView(DocumentViewSet):
    document=PublisherDocument
    serializer_class=PublisherDocumentSerializer
    lookup_field='id'
    filter_backends=[
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend

    ]

    search_fields=(
        'name',
        'address',
        'city',
        'state_province'
        'country'
    )

    filter_fields={
        'id': None,
        'name': 'name.raw',
        'city': 'city.raw',
        'state_province': 'state_province.raw',
        'country': 'country.raw',
    }

    ordering_fields = {
        'id': None,
        'name': None,
        'city': None,
        'country': None,
    }

    # Specify default ordering
    ordering = ('id', 'name',)
    # Define geo-spatial filtering fields
    geo_spatial_filter_fields = {
        'location': {
            'lookups': [
                LOOKUP_FILTER_GEO_DISTANCE,
            ],
        },
    }