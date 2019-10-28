from django.test import TestCase
from media_app.models import Document
from datetime import datetime
from accounts.models import CustomUser
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
import os

from django.http import HttpRequest
from django.template.loader import render_to_string
from media_app.views import ArticleListView
from django.urls import reverse
import media_app

class DocumentAssertion(TestCase):
    def test_is_empty(self):
        saved_docments = Document.objects.all()
        self.assertEqual(saved_docments.count(), 0)

    def test_is_create_docment(self):
        author = CustomUser.objects.create(username='test',email='test@gmail.com',password='test0123')
        print(author)
        title = "test"
        description = "test create model"
        path = os.getcwd()
        photo = SimpleUploadedFile(name='test_img.jpg', content=open(os.path.join(path, 'media_test/test_img.jpg'),'rb').read(), content_type='image/jpeg')
        uploaded_at = None
        Document.objects.create(author=author,title = title,description = description,photo = photo,uploaded_at = uploaded_at)
        self.assertEqual(1, len(Document.objects.all()))

class HtmlTests(TestCase):
    # URLを返す関数
    def _getTarget(self):
        return reverse('article_list_view')

    def test_list_returns_correct_html(self):
        # リクエストを擬似的に送ってくれるHTTPクライアント（self.cliant）でレスポンスオブジェクトを生成
        res = self.client.get(self._getTarget())
        #expected_html = render_to_string('media_app/article_list_view.html')
        self.assertTemplateUsed(res, 'media_app/article_list_view.html')
