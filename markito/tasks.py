import requests
from celery.utils.log import get_task_logger
from django.http import HttpResponse
from celery import shared_task
from celery.result import AsyncResult

from test_project.celery import app



@shared_task
def get_records(token):
    url = "https://seller.digikala.com/api/v1/variants/"
    r = requests.get(url,headers={'Authorization': token})
    record = r.json()
    print(record)
    # print(AsyncResult(record))
    return record

