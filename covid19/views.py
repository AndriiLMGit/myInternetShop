from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.

def covid19(request):
    """
    docstring
    """
    url = 'https://covid19.gov.ua/'
    get_page = requests.get(url)
    soup = BeautifulSoup(get_page.content, 'html.parser')

    all_soup = soup.findAll('div' , {'class' : 'one-field ' , 'class' : 'info-count'})
    add_date_soup = soup.findAll(style = "color: #999999;")
    add_date_soup = add_date_soup[0].string

    value_covid19 = []
    
    for item_soup in all_soup:
        value_item = item_soup.find('div', {'class' : 'field-value'})
        value = value_item.text
        value_covid19.append(value)
        
    
    number_of_patients = 'хворих на Covid-19'
    recovered = 'одужало'
    new_cases_per_day = 'нових випадків за добу'
    fatalities = 'летальних випадків'
    tested = 'протестовано'

    context = {
        'all_people' : value_covid19,
        'number_of_patients' : number_of_patients,
        'recovered' : recovered,
        'fatalities' : fatalities,
        'tested' : tested, 
        'add_date_soup' : add_date_soup,
    }

    return render(request, 'covid19/covid19.html', context)