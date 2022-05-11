import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    # numele task-ului periodic
    'add-every-10-seconds': {
        # path-ul catre functia care sa se repete
        'task': 'webapp.tasks.insert_logs',
        # din cat in cat timp vrei sa se repete
        'schedule': 10.0
        # pasarea parametrilor la functia (task_print) din 'task'
        # 'args': (16, 16)
    }
}
