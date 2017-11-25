from django.shortcuts import render
from .models import Measurement
from rest_framework import serializers, viewsets

# Create your views here.
class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    # answered by bovenson:
    #   https://stackoverflow.com/questions/20550598/django-rest-framework-could-not-resolve-url-for-hyperlinked-relationship-using
    # wtf just happened here? idk what HyperlinkedIdentityField does
    url = serializers.HyperlinkedIdentityField(view_name="measurements:measurements-detail")
    class Meta:
        model = Measurement
        fields = '__all__'


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
