import requests
from celery.utils.log import get_task_logger
from django.http import HttpResponse
from celery import shared_task
from celery.result import AsyncResult
from . import models
from test_project.celery import app



@shared_task
def get_records(token):
    url = "https://seller.digikala.com/api/v1/variants/"
    r = requests.get(url,headers={'Authorization': token})
    records = r.json()
    all_product = []
    for i in records['data']['items']:
        records_list = [i['title'], i['is_active'], i['fulfilment_and_delivery_cost'], i['stock']['selling_stock'],
                        i['price']['selling_price'], i['price']['rrp_price'], i['product']['category_name_fa'],
                        i['product']['image'],i['seller_id']]
        all_product.append(records_list)
    print(all_product)
    models.Products.objects.all().delete()
    for i in all_product:
        models.Products.objects.create(
            image=i[7],
            name=i[0],
            category=models.Categories.objects.create(name=i[6]),
            buy_price=i[5],
            sell_price=i[4],
            count=i[3],
            side_costs=i[2],
            is_active=i[1],


        )
    print(records)
    # print(AsyncResult(record))
    return records

