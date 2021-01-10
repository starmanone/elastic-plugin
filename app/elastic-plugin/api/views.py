from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import *
from .models import *

from python_backend.elastic_api import get_search

class ElasticData(APIView):
    """
    Get data from elastic with a json request
    """
    def get(self, request, format=None):
        url = "http://192.168.121.189/_search"
        params = self.request.query_params.get('query')

        resp = get_search(url, params)

        return Response(resp)

class MailActionsView(APIView):
    """
    List a mail action selected with primary key.
    """
    def get_object(self, pk):
        try:
            return MailActions.objects.get(pk=pk)
        except MailActions.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = MailActionsSerialezer(queryset)
        return Response(serializer.data)

class MailActionsList(APIView):
    """
    List all mail actions.
    """
    def get(self, request, format=None):
        queryset = MailActions.objects.all()
        serializer = MailActionsSerialezer(queryset, many=True)
        return Response(serializer.data)

class MailMetadataView(APIView):

    def get_object(self, pk):
        try:
            return MailMetadata.objects.get(pk=pk)
        except MailMetadata.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = MailMetadataSerialezer(queryset)
        return Response(serializer.data)