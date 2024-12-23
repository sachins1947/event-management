from django.contrib import admin
from event_manager.models import Event,Attendee,Task
# Register your models here.
admin.site.register(Event) 
admin.site.register(Attendee)
admin.site.register(Task)

