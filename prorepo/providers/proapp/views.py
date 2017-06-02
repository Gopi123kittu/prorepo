# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.views import View

from .models import *
import json

from providers.settings import BASE_DIR
from django.http import Http404



import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)
import json

class Providesrs_view(View):
    """
        Using Django Class based views which automatically
        passess the request methods to their respected 
        functions
    """
    def get(self, request):
        data = providers_data.objects.values("name", "email", "phone", "language", "currency")
        result = []
        for i in data:
             result.append(i)    
        return HttpResponse(result)

    def post(self, request):
        try:
            print "came into post try"
            request_data = json.loads(request.body)
            obj = providers_data(name = request_data["name"], email = request_data['email'],
                                phone = int(request_data['phone']), language = request_data['language'],
                                currency = request_data['currency'])
            obj.save()
            return HttpResponse("Priovider: {} saved ".format(request_data["name"]))
        except Exception as e:
            logger.error('Exceptin raised {}'.format(e))
            return HttpResponse("Encountere errror while saving")

    def put(self, request):
        try:
            d = {}
            request_data = json.loads(request.body)
            print "request body", request_data
            if request_data.has_key('name'):
                d["name"] = request_data['name']                    # taking name to search for data
            if request_data.has_key('email'):
                d["email"] = request_data['email']
            if request_data.has_key('phone'):
                d["phone"] = request_data['phone'] 
            if request_data.has_key('language'):
                d["language"] = request_data['language']
            if request_data.has_key('currency'):
                d["currency"] = request_data['currency']
            name = d["name"]
            d.pop("name")
            # fetching the value based upong the provider name 
            providers_data.objects.filter(name=name).update(**d)
            return HttpResponse("Updated succesfully")
        except Exception as e:
            logger.error('Exceptin raised {}'.format(e))
            return HttpResponse("Encountere errror while updating")

    def delete(self, request):
        """
            deleting the data with the name as a constraint
        """
        try:
            request_data = json.loads(request.body)
            name = request_data["name"]
            providers_data.objects.get(name=request_data["name"]).delete()
            return HttpResponse("Provider '{}' deleted".format(name))
        except Exception as e:
            logger.error('Exceptin raised {}'.format(e))
            return HttpResponse("Encountere errror while deleting")

class polygons_view(View):

    def get(self, request):
        data = polygons.objects.values("name", "price", "prov", "poly")
        result = []
        for i in data:
             print i
             result.append(i)    
        return HttpResponse(result)

    def post(self, request):
        try:
            print "came into try", request
            # = GEOSGeometry('{ "type": "Point", "coordinates": [ 5.000000, 23.000000 ] }')  # GeoJSON
            request_data = json.loads(request.body)
            try:
                print request_data["prov"]
                my_object = providers_data.objects.get(name=request_data["prov"])
                request_data = json.loads(request.body)
                obj = polygons(name = request_data["name"], price = request_data['price'],
                                prov = request_data["prov"], poly = request_data['point'])
                obj.save()
                return HttpResponse("polygon: {} saved ".format(request_data["name"]))
            except providers_data.DoesNotExist:
                raise Http404("Provider Name does not exists")
        except Exception as e:
            logger.error('Exceptin raised {}'.format(e))
            return HttpResponse("Encountere errror while saving")


    def put(self, request):
        try:
            d = {}
            request_data = json.loads(request.body)
            print "request body", request_data
            if request_data.has_key('name'):
                d["name"] = request_data['name']                    # taking name to search for data
            if request_data.has_key('price'):
                d["price"] = request_data['price']
            if request_data.has_key('prov'):
                d["prov"] = request_data['prov'] 
            if request_data.has_key('language'):
                d["point"] = request_data['point']
            if request_data.has_key('currency'):
                d["point"] = request_data['point']
            name = d["name"]
            d.pop("name")
            # fetching the value based upong the provider name 
            polygons.objects.filter(name=name).update(**d)
            return HttpResponse("Updated succesfully")
        except Exception as e:
            logger.error('Exceptin raised {}'.format(e))
            return HttpResponse("Encountere errror while updating")

    def delete(self, request):
        """
            deleting the data with the name as a constraint
        """
        try:
            request_data = json.loads(request.body)
            name = request_data["name"]
            polygons.objects.get(name=request_data["name"]).delete()
            return HttpResponse("Polygon '{}' data deleted".format(name))
        except Exception as e:
            logger.error('Exceptin raised {}'.format(e))
            return HttpResponse("Encountere errror while deleting")


# def get_poly(self, data):
    # print "priting data", data
    # request_data = json.loads(request.body)
    # print request_data
    # d = "{'cordinates': [{}, {}]}".format(request_data["lat"], request_data["long"])
    # obj = polygons.objects.filter(headline__contains=d)
    # print obj
def get_poly(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('long')
    d= [float(lat), float(lon)]
    #print str(d)
    obj = polygons.objects.filter(poly__contains=d)
    print "obj", obj
    return HttpResponse(obj)