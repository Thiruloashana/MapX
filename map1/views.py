from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
import geocoder

def index(request):
	if request.method=='POST':
		form=SearchForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/map')
	else:
		form=SearchForm()
	address=Search.objects.all().last()
	location=geocoder.osm(address)
	lat=location.lat
	lng=location.lng
	country=location.country
	if lat==None or lng==None:
		address.delete()
		return HttpResponse("Your address input is invalid")
	#create map object
	m=folium.Map(location=[19,-12],zoom_start=2)
	folium.Marker([lat,lng],tooltip='Click for more',popup=country).add_to(m)
	m=m._repr_html_()
	context={
		'm':m,
		'form':form,
	}
	return render(request,'index.html',context)
