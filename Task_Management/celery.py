import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Task_Management')

celery_app = Celery('Task_Management')
