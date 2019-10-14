import os
from celery import Celery
from NewsSite import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsSite.settings')
app = Celery('NewsSite')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
