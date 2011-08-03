from django.db import models
from django.contrib import admin


class MenuList(models.Model):
	menu_item = models.CharField('Menu Item', max_length = 30)
	price = models.FloatField()
	available = models.BooleanField(default=False)
	def __unicode__(self):
		return self.menu_item

class Order(models.Model):
	order_item = models.ForeignKey('MenuList', null=False)
	quantity = models.IntegerField(default=1)	
	paid_for = models.BooleanField('Paid for')
	delivery = models.BooleanField('Do you want your food delivered to you? (50p)', default=False)
	delivery_cost = models.FloatField(default=.50)
	block = models.CharField('Block', blank=True, max_length = 30)
	room_num = models.IntegerField('Room number', blank=True)
	other_location = models.CharField('Other location', blank=True, max_length = 30)
	tel_num = models.IntegerField('Telephone', blank=True, null=True)
	order_details = models.TextField('Order details')
	created = models.DateTimeField('Date and time', auto_now_add=True)
	total_amount = models.FloatField(blank=True, null=True)

	def __unicode__(self):
		return str(self.order_item)

admin.site.register(MenuList)
admin.site.register(Order)
