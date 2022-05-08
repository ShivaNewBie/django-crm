from django.urls import path, include 


from rest_framework.routers import DefaultRouter
from .views import ClientViewSet,ClientView, NoteViewSet,convert_lead_to_client,delete_client

router = DefaultRouter()
router.register('clients', ClientViewSet,basename='clients')
router.register('notes',NoteViewSet,basename='notes')
urlpatterns = [
    path('clients/list/',ClientView.as_view()), #when using class based views always add .as_view()
    path('convert_lead_to_client/', convert_lead_to_client),
    path('client/delete_client/<int:id>', delete_client),
    path('', include(router.urls)),
]
