from django.db import models


class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=60)
    state_province=models.CharField(max_length=30)
    country=models.CharField(max_length=50)
    website=models.URLField()
    latitude=models.DecimalField(null=True,blank=True,decimal_places=15,max_length=19,default=0,max_digits=19)
    longitude=models.DecimalField(null=True,blank=True,decimal_places=15,max_length=19,default=0,max_digits=19)

    class Meta:
        "Meta Options"
        ordering=["id"]

    def __str__(self):
        return self.name

    @property
    def location_field_indexing(self):
        """Location for indexing
        Used In Elastic indexing/tests of geo_distance native filter """
        return {
            'lat':self.latitude,
            'lon':self.longitude
        }

    