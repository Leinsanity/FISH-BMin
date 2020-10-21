from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets, mixins
from django.db.models import Q
from .models import Specimen, Preparation1, Preparation2, Collection_Date, Collector, Photographer, Locations, Status, Family, Tissue, Identifier
from. serializers import CollectionDateSerializer, Collectorserializer, FamilySerializer, IdentifierSerializer, LocationSerializer, PhotographerSerializer, Preparation1Serializer, Preparation2Serializer, SpecimenSerializer, StatusSerializer, TissueSerializer

class CollectionDateView(viewsets.ModelViewSet):
    queryset = Collection_Date.objects.all()
    serializer_class = CollectionDateSerializer

class CollectorView(viewsets.ModelViewSet):
    queryset = Collector.objects.all()
    serializer_class = Collectorserializer

class FamilyView(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class IdentifierView(viewsets.ModelViewSet):
    queryset = Identifier.objects.all()
    serializer_class = IdentifierSerializer   

class LocationView(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer

class PhotographerView(viewsets.ModelViewSet):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer

class Preparation1View(viewsets.ModelViewSet):
    queryset = Preparation1.objects.all()
    serializer_class = Preparation1Serializer

class Preparation2View(viewsets.ModelViewSet):
    queryset = Preparation2.objects.all()
    serializer_class = Preparation2Serializer         

class SpecimenView(viewsets.ModelViewSet):
    queryset = Specimen.objects.all()
    serializer_class = SpecimenSerializer

class StatusView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer  

class TissueView(viewsets.ModelViewSet):
    queryset = Tissue.objects.all()
    serializer_class = TissueSerializer  

# class SimilarViewSet(mixins.ListModelMixin):
#     def get_queryset(self):
#         Specimen = self.request.Specimen
#         return 

class SearchResultsView(ListView):
    model = Specimen
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('query')

        if query is not None: 
            lookups = Q(dna_barcode__icontains=query)

            results = Specimen.objects.filter(lookups).distinct()

            return results
        # else:
        #     return render (self, 'search.html')