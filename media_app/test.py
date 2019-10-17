from django.test import TestCase
from media_app.models import Document
from datetime import datetime
from accounts.models import CustomUser
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
import os

class DocumentAssertion(TestCase):
    def assertDocmentModel(self, actual_docment, author, title, description, photo, uploaded_at):
        self.assertEqual(actual_docment.author, author)
        self.assertEqual(actual_docment.title, title)
        self.assertEqual(actual_docment.description, description)
        self.assertEqual(actual_docment.photo, photo)
        #self.assertEqual(actual_docment.uploaded_at, uploaded_at)

class TestDocumentModel(TestCase):
    def creating_a_docment_and_saving(self, author, title, description, photo,uploaded_at):
        document = Document()
        # if name is not None:
        #     document.author = author
        # if title is not None:
        #     document.title = title
        # if description is not None:
        #     document.description = description
        # if description is not None:
        #     document.description = description
        document.save()

    def test_is_empty(self):
        saved_docments = Document.objects.all()
        self.assertEqual(saved_docments.count(), 0)

    def test_is_not_empty(self):
        author = get_user_model().objects.create_user(username='admin', email='kazuma444756@gmail.com', password='kazuma123')
        title = "test"
        description = "test model"
        path = os.getcwd()
        photo = SimpleUploadedFile(name='test_img.jpg', content=open(path+"/media_test/test_img.jpg", 'rb').read(), content_type='image/jpeg')
        upload_at = None
        self.creating_a_docment_and_saving(author,title,description,photo,upload_at)
        saved_docments = Document.objects.all()
        self.assertEqual(saved_docments.count(), 1)
        actual_docment = saved_docments[0]
        self.assertDocmentModel(actual_docment,author,title,description,photo,upload_at)
