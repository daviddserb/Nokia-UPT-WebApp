from celery import shared_task

@shared_task
def task_print():
    print(f'se intra in functia task_print()')
