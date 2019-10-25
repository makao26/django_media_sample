from django.test import TestCase
from media_app.models import Document
from datetime import datetime
from accounts.models import CustomUser
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
import os

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
