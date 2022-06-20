import folium
from django.shortcuts import render,redirect
from .import get_route
from .models import Route_search
from .forms import Route_SearchForm
from django.http import HttpResponse
import geocoder

def start_end(request):
    if request.method=='POST':
        form=Route_SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/route')
    else:
    	form=Route_SearchForm()

    add=Route_search.objects.all().last()

    address1=getattr(add,"address1")
    address2=getattr(add,"address2")
    location1=geocoder.osm(address1)
    location2=geocoder.osm(address2)
    lat1=location1.lat
    long1=location1.lng
    lat2=location2.lat
    long2=location2.lng
    country1=location1.country
    country2=location2.country
    '''if (lat1==None or long1==None or lat2==None or long2==None):
        address1.delete()
        address2.delete()
        return HttpResponse("Your address input is invalid")'''
    m=folium.Map(location=[19,-12],zoom_start=2)
    m=m._repr_html_()
    context={'m':m,'form':form}
    return render(request,'start_end.html',context)


def showroute(request):
    add=Route_search.objects.all().last()
    address1=getattr(add,"address1")
    address2=getattr(add,"address2")
    location1=geocoder.osm(address1)
    location2=geocoder.osm(address2)
    lat1=location1.lat
    long1=location1.lng
    lat2=location2.lat
    long2=location2.lng

    figure = folium.Figure()

    lat1,long1,lat2,long2=float(lat1),float(long1),float(lat2),float(long2)

    route=get_route.get_route(long1,lat1,long2,lat2)

    m = folium.Map(location=[(route['start_point'][0]),(route['start_point'][1])],zoom_start=10)
    m.add_to(figure)
    folium.PolyLine(route['route'],weight=10,color='blue',opacity=0.6).add_to(m)
    folium.Marker(location=route['start_point'],icon=folium.Icon(icon='play', color='green')).add_to(m)
    folium.Marker(location=route['end_point'],icon=folium.Icon(icon='stop', color='red')).add_to(m)
    figure.render()
    context={'map':figure}
    return render(request,'showroute.html',context)
