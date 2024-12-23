from rest_framework.viewsets import ModelViewSet
from .models import Event, Attendee, Task
from .serializers import EventSerializer, AttendeeSerializer, TaskSerializer
from django.shortcuts import render
from .models import Event
from django.shortcuts import get_object_or_404,redirect
from event_manager.froms import EventForm,TaskForm,AttendeeForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import calendar
from datetime import datetime
from django.shortcuts import render
from .models import Event

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("event_list")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login_page.html", {})

def log_out(request):
    logout(request)
    return redirect("login")

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get', 'post', 'put', 'delete'] 

class AttendeeViewSet(ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

def event_list(request):
    events = Event.objects.all()  # Fetch all events
    return render(request, 'homepage.html', {'events': events})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Get the event by ID or 404 if not found
    event.delete()  # Delete the event
    return redirect('event_list')  # Redirect to event list after deletion

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)  # Bind data to form
        if form.is_valid():
            form.save()  # Save the event to the database
            return redirect('event_list')  # Redirect to event list
    else:
        form = EventForm()  # Create an empty form for GET request
    
    return render(request, 'add_event.html', {'form': form})

@login_required
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Get the event by ID or 404 if not found

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)  # Bind data to form and populate with event data
        if form.is_valid():
            form.save()  # Save the updated event to the database
            return redirect('event_list')  # Redirect to event list
    else:
        form = EventForm(instance=event)  # Create a form populated with the event data for GET request
    
    return render(request, 'update_event.html', {'form': form})

@login_required
def add_task(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.event = event
            task.save()
            return redirect('event_task_list',event_id=event.id)  # Redirect to the event detail page
    else:
        form = TaskForm()
    
    return render(request, 'add_task.html', {'form': form, 'event': event})

def event_task_list(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    tasks = Task.objects.filter(event=event)
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status="Completed").count()
    
    # Calculate progress as a percentage (avoid division by zero)
    progress = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    
    context = {
        "event": event,
        "tasks": tasks,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "progress": progress,  # Pass the calculated progress to the template
    }
    return render(request, "task_list.html", context)

@login_required
def update_task(request, event_id, task_id):
    event = get_object_or_404(Event, id=event_id)
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Bind data to form and populate with task data
        if form.is_valid():
            form.save()  # Save the updated task to the database
            return redirect('event_task_list', event_id=event.id)  # Redirect to the event's task list page
    else:
        form = TaskForm(instance=task)  # Create a form populated with the task data for GET request
    
    return render(request, 'update_task.html', {'form': form, 'event': event, 'task': task})

@login_required
def delete_task(request, event_id, task_id):
    event = get_object_or_404(Event, id=event_id)
    task = get_object_or_404(Task, id=task_id)  # Get the task by ID or 404 if not found
    task.delete()  # Delete the task
    return redirect('event_task_list', event_id=event.id)  # Redirect to the event's task list page after deletion


@login_required
def event_attendee_list(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Get the event by ID
    attendees = event.attendees.all()  # Fetch all attendees related to the event
    return render(request, 'attendee_list.html', {'event': event, 'attendees': attendees})

@login_required
def add_attendee(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.event = event  # Assign the event
            attendee.save()
            return redirect('attendee_list', event_id=event.id)  # Redirect to event list after adding attendee
    else:
        form = AttendeeForm()

    return render(request, 'add_attendee.html', {'form': form, 'event': event})


@login_required
def update_attendee(request, event_id, attendee_id):
    event = get_object_or_404(Event, id=event_id)  # Retrieve the event by its ID
    attendee = get_object_or_404(Attendee, id=attendee_id, event=event)  # Retrieve the attendee within the event

    if request.method == 'POST':
        form = AttendeeForm(request.POST, instance=attendee)  # Pre-populate form with the existing attendee data
        if form.is_valid():
            form.save()  # Save the updated attendee details
            return redirect('attendee_list', event_id=event.id)  # Redirect to attendee list after update
    else:
        form = AttendeeForm(instance=attendee)  # Show the existing data in the form

    return render(request, 'update_attendee.html', {'form': form, 'event': event, 'attendee': attendee})

@login_required
def delete_attendee(request, event_id, attendee_id):
    event = get_object_or_404(Event, id=event_id)  # Retrieve the event by its ID
    attendee = get_object_or_404(Attendee, id=attendee_id, event=event)  # Retrieve the attendee within the event

    # Delete the attendee directly when this view is called
    attendee.delete()

    # Redirect to attendee list after deletion
    return redirect('attendee_list', event_id=event.id)
