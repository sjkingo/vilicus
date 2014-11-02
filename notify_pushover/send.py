import pushover
from . import TOKEN_KEY
pushover.init(TOKEN_KEY)

from models import PushoverUserTokens

# from https://pushover.net/api#priority
PRIORITY = {
    'LOWEST': -2,
    'LOW': -1,
    'NORMAL': 0,
    'HIGH': 1,
    'EMERGENCY': 2,
}

def send_push_notification(title, msg, priority=PRIORITY['NORMAL']):
    for t in PushoverUserTokens.objects.all():
        client = pushover.Client(t.token)
        client.send_message(msg, title='Vilicus alert: ' + title, priority=priority)
