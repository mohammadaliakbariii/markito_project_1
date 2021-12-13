import requests
from django.http import HttpResponse


def get_records(token):
    url = "https://seller.digikala.com/api/v1/variants/"
    r = requests.get(url,headers={'Authorization': token})
    record = r.json()
    print(record)
    return HttpResponse(record)

