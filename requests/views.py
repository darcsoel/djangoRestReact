"""BAsic example rest api view"""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView

from requests.models import Request
from requests.serializers import RequestSerializer


class IndexView(ListAPIView, CreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('text',)


class RequestIndexView(ListAPIView, CreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('text',)
