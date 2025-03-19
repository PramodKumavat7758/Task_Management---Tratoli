from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_task_notification(email,task_title):
    send_mail(
        subject="New Task Assigned",
        message=f"A new task'{task_title}' has been assigned you.",
        from_email="admin@gmail.com",
        recipient_list=[email]
    )