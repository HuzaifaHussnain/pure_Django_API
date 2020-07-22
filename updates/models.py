from django.conf import settings
from django.db import models

def upload_update_image(instance, filename):
	return "updates/images/{filename}".format(filename=filename)

# Create your models here.
class Update(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField()
	image = models.ImageField(upload_to=upload_update_image, blank=True, null= True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True) 
 