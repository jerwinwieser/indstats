from django.db import models
from django.utils import timezone

class Application(models.Model):
	name = models.CharField(max_length=100, blank=False)
	comments = models.TextField(max_length=300, blank=True)
	created_at = models.DateTimeField(editable=False, default=timezone.now)
	updated_at = models.DateTimeField(editable=False, default=timezone.now)
	def __str__(self):
		return self.name