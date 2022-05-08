from django.urls import path, include 


from rest_framework.routers import DefaultRouter
from .views import LeadViewSet,LeadView,delete_lead

router = DefaultRouter()
router.register('leads', LeadViewSet,basename='leads')

urlpatterns = [
    path('leads/list/',LeadView.as_view()), #when using class based views always add .as_view()
    path('leads/delete_lead/<int:lead_id>/',delete_lead),
    path('', include(router.urls)),
]
