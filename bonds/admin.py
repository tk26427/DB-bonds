from django.contrib import admin
from .models import Book ,BookUser  , Trade , Security,  Counterparty

admin.site.register(Book)
admin.site.register(BookUser)
admin.site.register(Trade)
admin.site.register(Security)
admin.site.register(Counterparty)
