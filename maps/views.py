from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
import geocoder

# Create your views here.


def index(request,local):
    location = geocoder.osm(local)
    print("sumit")
    print(location)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        # address.delete()
        
        return render(request,'notmap.html',{'local':local})

    # Create Map Object
    m = folium.Map(location=[lat, lng], zoom_start=16)

    folium.Marker([lat, lng], tooltip='Click for more',
                  popup=local).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'indexx.html', context)

