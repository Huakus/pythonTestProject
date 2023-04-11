import logging
from django.conf import settings

logger = logging.getLogger(__name__)

# Redact sensitive information from logs
class RedactingFormatter(logging.Formatter):
    def format(self, record):
        formatted_message = super().format(record)
        for word in settings.SECRETS:
            formatted_message = formatted_message.replace(word, '*' * 6)
        return formatted_message

