import requests
from common.get_excel import getexcel

def test163():

    response = requests.post(url=getexcel()[2])

    print(response.text)