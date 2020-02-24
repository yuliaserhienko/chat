import logging

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError

from .models import Message

log = logging.getLogger(__name__)


class MessagesSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = ("email", "text")

    def validate_text(self, value):
        STOP_WORDS = ['omg', ]

        if any([word in value.split() for word in STOP_WORDS]):
            raise ValidationError('Text have wrong words')
        return value
