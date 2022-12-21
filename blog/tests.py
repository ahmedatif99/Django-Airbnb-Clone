from django.test import TestCase
from .models import Post, Category
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

class BlogModelTest(TestCase):

    def post_create(self):
        author = User.objects.create(username='ahmed', password='ahmed123456')
        category = Category.objects.create(name='test category')

        return Post.objects.create(
            author = author,
            title = 'Django testing',
            tags = 'django',
            description = 'Django testing description',
            category = category
        )

    def test_model_str(self):
        post = self.post_create()
        self.assertEqual(post.__str__(), post.title)

class BlogViewTest(TestCase):

    def test_blog_url(self):
        respons = self.client.get('/blog/')
        self.assertEqual(respons.status_code, 200)
        self.assertTemplateUsed(respons, 'blog/post_list.html')


    def test_view_revers(self):
        respons = self.client.get(reverse('blog:post_list'))
        self.assertTemplateUsed(respons, 'blog/post_list.html')