from django.contrib import admin
from .models import Room, Reservation, BeverageOrder, Notification, Report, User

admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(BeverageOrder)
admin.site.register(Notification)
admin.site.register(Report)
admin.site.register(User)
