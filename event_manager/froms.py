from django import forms
from event_manager.models import Event,Task,Attendee

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'location', 'date']  # Specify the fields

        widgets = {
            'name': forms.TextInput(attrs={
                "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Enter event name here..."
            }),
            'description': forms.Textarea(attrs={
                "class": "peer h-full min-h-[100px] w-full resize-none rounded-md border border-blue-gray-200 border-t-transparent bg-transparent px-3 py-3 font-sans text-sm font-normal text-blue-gray-700 outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-gray-900 focus:border-t-transparent focus:outline-0 disabled:resize-none disabled:border-0 disabled:bg-blue-gray-50",
                "placeholder": "Enter event description here..."
            }),
            'location': forms.TextInput(attrs={
                "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Enter event location here..."
            }),
            'date': forms.DateInput(attrs={
                "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "type": "date",
                "placeholder": "Select event date"
            }),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'deadline', 'status', 'assigned_to']  # Specify the fields to include

        widgets = {
            'name': forms.TextInput(attrs={
                "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Enter task name here..."
            }),
            'deadline': forms.DateInput(attrs={
                "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "type": "date",
                "placeholder": "Select task deadline"
            }),
            'status': forms.Select(attrs={
                "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            }),
            'assigned_to': forms.Select(attrs={
                "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            }),
        }
class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', 'email', 'event']  # Include 'event' as it's now part of the form

        widgets = {
            'name': forms.TextInput(attrs={
                "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Enter attendee name here..."
            }),
            'email': forms.EmailInput(attrs={
                "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Enter attendee email here..."
            }),
            'event': forms.Select(attrs={
                "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            }),
        }

