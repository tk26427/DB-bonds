from django.urls import path
from . import views

urlpatterns=[
				path('',views.main ,  name='mainpage'),
				path('trademain',views.trademain ,  name='trademainpage'),
				path('sign/',views.sign ,  name='signpage'),
				path('about/',views.about ,  name='aboutpage'),
				path('security/',views.security ,  name='securitypage'),
				path('trade/',views.trade ,  name='tradepage'),
				path('logout/',views.logout_view ,  name='logout'),
]
