from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.contrib.auth import get_user_model


	


class Book(models.Model):
	BookName = models.CharField(max_length=50, default='New book')

	def __str__(self):
		return f'{self.BookName}'


class BookUser(models.Model):
	BookId = models.IntegerField(default=1)
	UserId = models.IntegerField(default=1)

	def __str__(self):
		return f'{self.BookId} : {self.UserId}'



class Trade(models.Model):
	BookId = models.IntegerField(default=1)
	CounterpartyId = models.IntegerField(default=1)
	SecurityId = models.IntegerField(default=1)
	
	quantity = models.IntegerField(default=1)
	status = models.CharField(max_length=10 ,choices = (('s' , 'Success'),('f' , 'Failed'),
                          ('p' , 'Pending'),('na','Not Available')),
                default = 'na' )
	Price = models.IntegerField(default=00)
	Buy_Sell = models.CharField(max_length=10 ,choices = (('b' , 'Buy'),('s' , 'Sell')),
                default = 'b' )
	TradeDate= models.DateTimeField(auto_now_add=True)
	SettlementDate= models.DateTimeField(auto_now_add=False)
	
	

	def __str__(self):
		return f'{self.TradeDate} : {self.status}'


class Security(models.Model):
	ISIN = models.IntegerField(default= 0)
	CUSIP = models.IntegerField(default= 0)
	Issuer = models.CharField(max_length=200 , default='NA')
	MaturityDate= models.DateTimeField(auto_now_add=False)

	Coupon = models.IntegerField(default= 0)
	Type = models.CharField(max_length=10 ,choices = (('1' , 'Type 1'),('2' , 'Type 2'),
                          ('3' , 'Type 3'),('4','Type 4')),
                default = '1' )

	FaceValue = models.IntegerField(default= 0)

	status = models.CharField(max_length=10 ,choices = (('s' , 'Success'),('f' , 'Failed'),
                          ('p' , 'Pending'),('na','Not Available')),
                default = 'na' )

	def __str__(self):
		return f'{self.MaturityDate} : {self.status}'


class Counterparty(models.Model):
	Name = models.CharField(max_length=50, default='New Counterparty')



	def __str__(self):
		return f'{self.id} : {self.Name}'


