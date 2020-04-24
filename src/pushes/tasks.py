from celery import task
from pushes.models import Pushes
from datetime import datetime
from celery.schedules import crontab
from celery.task import periodic_task


@task(name='send_pushes')
def send_pushes():
    now = datetime.now()
    pushes = Pushes.objects.filter(sent_date__lte=now)
    for push in pushes:
        push.sent_status = True
        push.save()



