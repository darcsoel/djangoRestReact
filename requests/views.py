"""BAsic example rest api view"""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from requests.models import Request
from requests.serializers import RequestSerializer


class IndexViewSet(ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('text',)
