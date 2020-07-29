from django.conf import settings
from django.db import models

# Create your models here.

def upload_status_image_to(instance, filename):
	return "status/{filename}".format(filename=filename)

class Status(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to=upload_status_image_to, null=True, blank=True)
	update = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.content)[:50]

	class Meta:
		verbose_name = "Status Post"
		verbose_name_plural = "Status Posts"