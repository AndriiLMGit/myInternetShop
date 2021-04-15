from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def yobit(request):
    """
    docstring
    """

    template_name = 'yobit/yobit_main_view.html'


    url = "https://yobit.net/ru/"
    request_yobit = requests.get(url)

    content = request_yobit.text

    soup = BeautifulSoup(content, 'html.parser')

    ETH_BTC_LAST = soup.find("span", attrs = {"id" : "label_last"})
    ETH_BTC_24_HIGHT = soup.find(id="label_high24")
    ETH_BTC_24_LOW = soup.find(id="label_low24")
    ETH_BTC_24_VOL = soup.find(id="label_vol24")


    LIST_OF_ETH_BTCS = [ETH_BTC_LAST, ETH_BTC_24_HIGHT, ETH_BTC_24_LOW, ETH_BTC_24_VOL]

    data = {
        'LIST_OF_ETH_BTCS' : LIST_OF_ETH_BTCS,
    }


    return render(request, template_name, data)