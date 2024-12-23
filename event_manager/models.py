from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="attendees")

    def __str__(self):
        return self.name

class Task(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tasks")
    name = models.CharField(max_length=200)
    deadline = models.DateField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    assigned_to = models.ForeignKey(Attendee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
