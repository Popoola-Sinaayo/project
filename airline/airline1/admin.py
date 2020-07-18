from django.contrib import admin
from .models import Airport, Flight, Passenger
# Register your models here.
class PassengerInLine(admin.StackedInline):
    model = Passenger.airline1.through
    extra = 1

class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInLine]

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("airline1",)
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
