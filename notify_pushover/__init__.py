from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

_token_key = 'NOTIFY_PUSHOVER_API_TOKEN' 
if not hasattr(settings, _token_key):
    raise ImproperlyConfigured(_token_key + ' is missing but is required for the notify_pushover app')
TOKEN_KEY = getattr(settings, _token_key)

import signals
