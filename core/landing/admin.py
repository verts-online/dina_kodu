from django.contrib import admin
from .models import *

class CallRequestFilters(admin.ModelAdmin):
    list_filter = ("services", "day", "time", "way", "request_created", "status")
    list_display = ("day", "time", "way", "contact", "request_created",  "status")

    # @admin.display(empty_value="???")
    # def name(self, obj):
    #
    #     return f"Заявка от {obj}"

admin.site.register(CallRequest, CallRequestFilters)
admin.site.register(Service)
admin.site.register(CallDayRequest)
admin.site.register(CallTimeRequest)
admin.site.register(CallWayRequest)