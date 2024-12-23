from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event_manager.views import EventViewSet, AttendeeViewSet, TaskViewSet,event_list,delete_event,add_event,update_event,add_task,event_task_list,update_task,delete_task,event_attendee_list,add_attendee,update_attendee,delete_attendee,login_user,log_out
from django.contrib import admin

router = DefaultRouter()
router.register('events', EventViewSet)
router.register('attendees', AttendeeViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path("",login_user,name="login"),
    path("logout/",log_out,name="logout"),
    path('api/', include(router.urls)),
    path("home/",event_list,name="event_list"),
    path('admin/', admin.site.urls),
    path("delete_event/<int:event_id>/",delete_event,name='delete_event'),
    path("add_event/",add_event,name="add_event"),
    path('events/<int:event_id>/update/',update_event, name='update_event'),
    path("events/<int:event_id>/add_task/", add_task, name="add_task"),
    path('events/<int:event_id>/tasks/', event_task_list, name='event_task_list'),
    path('events/<int:event_id>/task/<int:task_id>/update/', update_task, name='update_task'),
    path('events/<int:event_id>/task/<int:task_id>/delete/', delete_task, name='delete_task'),
    path('events/<int:event_id>/attendees/', event_attendee_list, name='attendee_list'),
    path('events/<int:event_id>/add_attendee/', add_attendee, name='add_attendee'),
    path('events/<int:event_id>/attendee/<int:attendee_id>/update/', update_attendee, name='update_attendee'), 
    path('events/<int:event_id>/attendee/<int:attendee_id>/delete/', delete_attendee, name='delete_attendee'), 
]
