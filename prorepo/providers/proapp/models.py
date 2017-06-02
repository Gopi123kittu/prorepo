# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class providers_data(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=250)
	phone = models.BigIntegerField()
	language = models.CharField(max_length=150)
	currency = models.CharField(max_length=100)     # can use currency module

	def __str__(self):
		return "%s,%s,%d,%s,%s" % (self.name, self.email, self.phone, self.language, self.currency)


class polygons(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    prov = models.CharField(max_length=50)
    price = models.IntegerField()
    poly = models.CharField(max_length=250)
    # GeoDjango-specific: a geometry field (MultiPolygonField)

    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.name