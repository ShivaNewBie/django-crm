from rest_framework import serializers 

from team.serializers import User, UserSerializer

from .models import Client, Note

class ClientSerializer(serializers.ModelSerializer):    
    class Meta: 
        ordering = ['-id']
        model = Client
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            'id',
            'name',
            'contact_person',
            'email',
            'phone',
            'website',
            'estimated_value',
            'created_at',
            'modified_at',        
        )

class NoteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Note 
        fields = (
            'id',
            'name',
            'body'
        )