from django.db import models
from django.urls import reverse
import uuid 

class comic(models.Model):
	nombre_comic = models.CharField  (max_length=120)
	codigo_comic = models.CharField  (max_length=12)
	precio = models.CharField        (max_length=7)
	editorial = models.CharField     (max_length=21)
	autor = models.CharField         (max_length=120)
	cantidad = models.IntegerField   (default=0)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	
	class meta:
        ordering = ['nombre_comic']

	def get_absolute_url(self):
        return reverse('comic_especificacion', args=[str(self.id)])
	
	def _str_(self):
		return self.nombre_comic


