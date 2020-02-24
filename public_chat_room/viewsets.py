import logging

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.validators import ValidationError

from .models import Message
from .pagination import PublicChatPagination
from .serializers import MessagesSerializer

log = logging.getLogger(__name__)


class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializer
    pagination_class = PublicChatPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = kwargs.get('page')
        page = self.paginator.paginate_queryset(queryset, request, page_number=page)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            message = Message.objects.get(pk=pk)
        except Message.DoesNotExist:
            raise ValidationError('No message with such id')
        serializer = self.get_serializer(message)
        return Response(serializer.data)
