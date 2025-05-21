from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class ViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Десерти")
        for i in range(15):
            Recipe.objects.create(name=f"Рецепт {i}", description="Опис", category=self.category)

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertTrue(len(response.context['recipes']) <= 10)

    def test_category_detail_view(self):
        response = self.client.get(reverse('category_detail', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')
        self.assertEqual(len(response.context['recipes']), 15)
