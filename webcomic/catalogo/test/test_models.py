from django.test import TestCase
from comic.models import nombre_comic, codigo_comic, precio, editorial, autor, cantidad, ingreso_fechas
from usuarios.models import comic

class GenreModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        comic.objects.create(name='Accion', summary='Prueba')
    
    def test_name_label(self):
        comic = comic.objects.get(id=1)
        field_label = comic._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_summary_label(self):
        comic = comic.objects.get(id=1)
        field_label = comic._meta.get_field('summary').verbose_name
        self.assertEquals(field_label,'summary')
    
    def test_name_max_length(self):
        comic = comic.objects.get(id=1)
        max_length = comic._meta.get_field('name').max_length
        self.assertEquals(max_length,100)
    
    def test_summary_max_length(self):
        comic = comic.objects.get(id=1)
        max_length = comic._meta.get_field('summary').max_length
        self.assertEquals(max_length,1000)
        
    def test_get_absolute_url(self):
        comic = comic.objects.get(id=1)
        self.assertEquals(comic.get_absolute_url(), '/catalogos/comic/1')

