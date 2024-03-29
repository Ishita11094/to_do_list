from django.db import models
from django.contrib.auth.models import User

class TodoModel(models.Model):
	task = models.CharField(max_length=50, primary_key=True)
	deadline = models.CharField(max_length=50)
	note = models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.task