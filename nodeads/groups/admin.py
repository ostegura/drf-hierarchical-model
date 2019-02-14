from django.contrib import admin
import mptt.admin


from .models import Vehicle, VehicleType

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(VehicleType, mptt.admin.MPTTModelAdmin)
