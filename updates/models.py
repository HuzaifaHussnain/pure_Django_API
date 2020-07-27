from django.core.serializers import serialize
from django.conf import settings
from django.db import models
import json

def upload_update_image(instance, filename):
	return "updates/images/{filename}".format(filename=filename)

class UpdateQuerySet(models.QuerySet):
	def serialize(self):
		qs = list(self.values("user", "content"))
		return json.dumps(qs)

class UpdateManager(models.Manager):
	def get_queryset(self):
		return UpdateQuerySet(self.model, using=self._db)


# Create your models here.
class Update(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField()
	image = models.ImageField(upload_to=upload_update_image, blank=True, null= True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True) 

	objects = UpdateManager()

	def serialize(self):
		data = {
			'user': self.user.id,
			'content': self.content
		}
		return json.dumps(data)
 