from django.shortcuts import render, redirect
from django.urls import reverse
import os

from pagination.functions import get_list_of_dicts, abs_path_to_file


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = 1
    next_page_url = 'write your url'
    bus_stations_list = get_list_of_dicts(abs_path_to_file(r'pagination\data-398-2018-08-30.csv'), list_of_dicts=None)
    return render(request, 'index.html', context={
        'bus_stations': bus_stations_list,
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })

