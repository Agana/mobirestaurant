from django.template import Context, loader
from django.http import HttpResponse
from models import *
from django import forms
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response



class OrderForm(ModelForm):
	class Meta:
		model = Order
		exclude=['paid_for', 'total_amount', 'order_details']

def welcome(request, limit=15):
	
	return render_to_response('mobilerestaurant/welcome.html')

@csrf_exempt
def place_order(request, limit=15):
	
	place_order= Order.objects.all()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			
			return render_to_response('mobilerestaurant/placed.html', {'request':request, 'place_order':place_order})  
	else:
		form = OrderForm()
	return render_to_response('mobilerestaurant/order.html', {'form': form.as_p(), 'request':request, 'place_order':place_order})

def calc_total(request):
	meal = MenuList.objects.filter(pk==id)
	order = Order.objects.objects.get(quantity__pk=id)
	total_cost = (meal.price*order.quantity) + order.delivery_cost
	return render_to_response('mobilerestaurant/bill.html', {'total_cost':total_cost, 'order':order, 'meal':meal, 'request':request})
