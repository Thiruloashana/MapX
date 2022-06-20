
from django import forms
from .models import Route_search

class Route_SearchForm(forms.ModelForm):
	address1= forms.CharField(label='START')
	address2= forms.CharField(label='END')
	class Meta:
		model = Route_search
		fields =['address1','address2',]
