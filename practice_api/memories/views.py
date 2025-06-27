from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *
from .permissions import *
from rest_framework.throttling import ScopedRateThrottle
from .throttling import *
from .pagination import *
from django_filters.rest_framework import DjangoFilterBackend

class MemoriesViewSet(viewsets.ModelViewSet):
    queryset = Memories.objects.all()
    serializer_class = MemoriesSerializer
    permission_classes = (OwnerPermissions,)
    throttle_classes = (LowRequestRateThrottle, ScopedRateThrottle)
    throttle_scope = 'low_request'
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('text',)
    
    def perform_create(self, serializers):
        return serializers.save(owner=self.request.user)