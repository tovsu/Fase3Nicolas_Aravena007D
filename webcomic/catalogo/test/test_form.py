from django.test import TestCase
from comic.forms import GenreForm, MovieForm
from comic.models import nombre_comic, codigo_comic, precio, editorial, autor, cantidad, ingreso_fechas
from django.core.files.uploadedfile import SimpleUploadedFile

class ComicFormsTest(TestCase):
    def test_valid_form(self):
        g = comic.objects.create(name='Prueba1', summary='Prueba')
        data = {'name': g.name, 'summary': g.summary,}
        form = GenreForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = comic.objects.create(name='', summary='Prueba')
        data = {'name': g.name, 'summary': g.summary,}
        form = GenreForm(data=data)
        self.assertFalse(form.is_valid())
