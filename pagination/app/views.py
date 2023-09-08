from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.functions import get_list_of_dicts


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = 1
    next_page_url = 'write your url'
    bus_stations_list = get_list_of_dicts(r'D:\projects\django_netology\2_netology_django_hw_requests_and_templates\pagination\data-398-2018-08-30.csv', list_of_dicts=None)
    return render(request, 'index.html', context={
        'bus_stations': bus_stations_list,

        # 'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'},
        #                  {'Name': 'другое название', 'Street': 'другая улица', 'District': 'другой район'}],
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })

