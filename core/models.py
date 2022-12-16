from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Application(models.Model):
	VISA = 'Visa'
	PASSPORT = 'Passport'
	TYPE_CHOICES = [
		(VISA, 'Visa'),
		(PASSPORT, 'Passport'),
	]
	type = models.CharField(max_length=100, choices=TYPE_CHOICES, default=VISA, blank=False)
	submit_date = models.DateField(editable=True, blank=False)
	comments = models.TextField(max_length=300, blank=True)
	approved = models.BooleanField(blank=False, editable=True, default=False)
	created_at = models.DateTimeField(editable=False, default=timezone.now)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, editable=False)
	def __str__(self):
		return self.type
