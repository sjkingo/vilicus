# Django local site-specific settings for vilicus project.

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',     # leave blank
        'PORT': '',     # leave blank
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# If DEBUG is True, localhost will automatically be added to this list.
ALLOWED_HOSTS = []

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6x78*0ze892of8f+=mo8ce8cg9!e#r5_v45oz2=6$j_v)=0i0d'
