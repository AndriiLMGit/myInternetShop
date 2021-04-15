from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def main_finance(request):

    url = "https://finance.i.ua/"
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    
    table = soup.find("table", attrs = {"class" : "table-data"})

    rows = soup.findAll("td")

    valuta = soup.find("td", attrs = {"class" : "col-cy"})
    buy = soup.find("td", attrs = {"class" : "col-buy"})
    sale = soup.find("td", attrs = {"class" : "col-sale"})
    nbu = soup.find("td", attrs = {"class" : "col-nbu"})

    data = {
        'title' : soup.title.string,
        'table' : table,
        'table_contents' : table.contents,
        'rows' : rows,
        'valuta' : valuta.string,
        'buy' : buy.string,
        'sale' : sale.string,
        'nbu' : nbu.string,
        'value' : 'My name is Andrii',

    }

    return render(request, 'finance/main_finance.html', data)