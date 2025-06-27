from rest_framework import pagination
from .models import *
from rest_framework.response import Response

class CustomPagination(pagination.BasePagination):

    def paginate_queryset(self, queryset, request, view=None):
        memories = Memories.objects.all()
        return memories
    
    def get_paginated_response(self, data):
        return Response({
            'result': data
        })