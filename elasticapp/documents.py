
from django_elasticsearch_dsl import Document,Index,fields
from elasticsearch_dsl import analyzer

from .models import Publisher

"Name Of The Elastic Search index"

PUBLISHER_INDEX=Index('publisher')

"See Elasticsearch Indices API reference for availbale settings"
PUBLISHER_INDEX.settings(
    number_of_shards=5,
    number_of_replicas=1
)

@PUBLISHER_INDEX.doc_type
class PublisherDocument(Document):
    "Publisher Elasticsearch document"

    id=fields.IntegerField(attr='id')

    name=fields.TextField(
        fields={
            'raw':fields.TextField(analyzer='keyword')
        }
    )

    address=fields.TextField(
        fields={
            'raw':fields.TextField(analyzer='keyword')
        }
    )

    city=fields.TextField(
        fields={
            'raw':fields.TextField(analyzer='keyword')
        }
    )

    state_province=fields.TextField(
        fields={
            'raw':fields.TextField(analyzer='keyword')
        }
    )

    country=fields.TextField(
        fields={
            'raw':fields.TextField(analyzer='keyword')
        }
    )

    website=fields.TextField(
        fields={
            'raw':fields.TextField(analyzer='keyword')
        }
    )

    "location"
    location=fields.GeoPointField(attr='location_field_indexing')

    class Django(object):

        model=Publisher  


    



