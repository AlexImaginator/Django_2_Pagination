from django.shortcuts import render, redirect
from django.urls import reverse
from csv import DictReader
from django.core.paginator import Paginator

import pagination.settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    data = []
    
    with open(pagination.settings.BUS_STATION_CSV, 'r', encoding='utf-8') as csvdata:
        reader = DictReader(csvdata)
        for row in reader:
            station = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            data.append(station)
            
    paginator = Paginator(data, 10)
    current_page = int(request.GET.get('page', 1))
    bus_stations = paginator.get_page(current_page)

    context = {
        'bus_stations': bus_stations,
    }
    
    return render(request, 'stations/index.html', context)
