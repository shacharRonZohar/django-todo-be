import uuid

from django.db import models


# Create your models here.
class Todo(models.Model):
    class PriorityOptions(models.IntegerChoices):
        low = 1
        medium = 2
        high = 3
        critical = 4

    class SeverityOptions(models.IntegerChoices):
        low = 1
        medium = 2
        high = 3
        critical = 4

    class StatusOptions(models.TextChoices):
        pending = 'PENDING'
        in_progress = 'IN_PROGRESS'
        blocked = 'BLOCKED'
        completed = 'COMPLETED'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, blank=False, default='Default Title')
    description = models.TextField(max_length=500, blank=True)
    priority = models.IntegerField(choices=PriorityOptions.choices, default=PriorityOptions.low)
    severity = models.IntegerField(choices=SeverityOptions.choices, default=SeverityOptions.low)
    status = models.TextField(choices=StatusOptions.choices, default=StatusOptions.pending)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
