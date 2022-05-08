from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets,filters
from rest_framework.decorators import api_view 
from rest_framework.views import APIView
from rest_framework.response import Response 

from team.models import Team
from lead.models import Lead




from django.contrib.auth.models import User 

from .models import Client, Note
from .serializers import ClientSerializer, NoteSerializer 



class ClientPagination(PageNumberPagination):
    page_size = 2

class ClientViewSet(viewsets.ModelViewSet): #this is a way to write better code. We get all products and each detail
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = ClientPagination
    filter_backends = (filters.SearchFilter,) #comma is important here 
    search_fields = ('name','contact_person')    
    # def list(self, request): #this code affects the response.data.results
    #     queryset = Client.objects.all()
    #     serializer = ClientSerializer(queryset,many=True)
    #     return Response(serializer.data)
    # def retrieve(self,request,pk=None):   
    #     queryset = Client.objects.all()
    #     client = get_object_or_404(queryset,pk=pk)
    #     serializer = ClientSerializer(client)
    #     return Response(serializer.data)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        serializer.save(team=team, created_by=self.request.user)

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        return self.queryset.filter(team=team)
    
    

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.GET.get('client_id')

        return self.queryset.filter(team=team).filter(client_id=client_id)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.data['client_id']

        serializer.save(team=team, created_by=self.request.user, client_id=client_id)

        
class ClientView(APIView): 
    def get(self,request,format=None):
        leads = Client.objects.all()
        serializers = ClientSerializer(leads,many=True)
        return Response(serializers.data)
        
@api_view(['POST'])
def convert_lead_to_client(request):
    team = Team.objects.filter(members__in=[request.user]).first() 
    lead_id = request.data['lead_id']

    try:
        lead = Lead.objects.filter(team=team).get(pk=lead_id)
    except Lead.DoesNotExist:
        raise Http404
    #after the function from above runs the function below will run
    client = Client.objects.create(team=team, name=lead.company,
    contact_person = lead.contact_person, email = lead.email, phone=lead.phone, website = lead.website, created_by = lead.created_by)

    return Response()