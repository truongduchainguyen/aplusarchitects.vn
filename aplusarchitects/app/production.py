# DATABASE SETTINGS
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# EMAIL SETTINGS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = "Django Base <" + EMAIL_HOST_USER + ">"

# CELERY SETTINGS
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672/'
CELERY_TASK_ALWAYS_EAGER = False if CELERY_BROKER_URL else True
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'

DEBUG = False
ALLOWED_HOSTS = ["*"]
