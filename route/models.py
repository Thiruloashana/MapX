from django.db import models

# Create your models here.
class Route_search(models.Model):
	address1 = models.CharField(max_length=200,null =True)
	address2 = models.CharField(max_length=200,null =True)
	date = models.DateTimeField(auto_now_add=True)
	def __data__(self):
		return self.address1,self.address2
