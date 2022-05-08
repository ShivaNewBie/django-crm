from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.pagination import PageNumberPagination


from rest_framework import viewsets,filters
from rest_framework.decorators import api_view 
from rest_framework.views import APIView
from rest_framework.response import Response 

from team.models import Team

from django.contrib.auth.models import User 
from .models import Lead

from .serializers import LeadSerializer 

class LeadPagination(PageNumberPagination):
    page_size = 2

class LeadViewSet(viewsets.ModelViewSet): #this is a way to write better code. We get all products and each detail
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    pagination_class = LeadPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('company', 'contact_person')

    def perform_create(self,serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team,created_by=self.request.user)

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first() #checking if self.request.user is in members
        return self.queryset.filter(team=team)


@api_view(['POST'])
def delete_lead(request,lead_id):
    team = Team.objects.filter(members__in=[request.user]).first() #checking if self.request.user is in members

    lead = team.leads.filter(pk=lead_id) #same as get_object
    lead.delete()

    return Response({'message':'The lead was deleted'})


class LeadView(APIView): 
    def get(self,request,format=None):
        leads = Lead.objects.all()
        serializers = LeadSerializer(leads,many=True)
        return Response(serializers.data)
