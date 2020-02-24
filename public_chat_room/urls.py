from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .viewsets import MessagesViewSet


messages_list = MessagesViewSet.as_view({
    'get': 'list'
})

message = MessagesViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('messages/list/<int:page>', messages_list, name='messages-list'),
    path('messages/single/<int:pk>', message, name='message-single'),
])
