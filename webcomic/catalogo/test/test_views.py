from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from comic.models import nombre_comic, codigo_comic, precio, editorial, autor, cantidad, ingreso_fechas

class ComicListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_comic = 13

        for comic_codigo in range(number_comic):
            comic.objects.create(
                name=f'Accion {comic_codigo}',
                summary=f'Prueba {comic_codigo}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogos/comic/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('comics'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('comics'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/catalogos/comic_lista.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('comics'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['comic_lista']) == 10)

    def test_lists_all_comic(self):

        response = self.client.get(reverse('comics')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['comics']) == 3)

