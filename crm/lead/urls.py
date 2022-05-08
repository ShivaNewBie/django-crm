from django.urls import path, include 


from rest_framework.routers import DefaultRouter
from .views import LeadViewSet,LeadView

router = DefaultRouter()
router.register('leads', LeadViewSet,basename='leads')

urlpatterns = [
    path('leads/list/',LeadView.as_view()), #when using class based views always add .as_view()

    path('', include(router.urls)),
]
