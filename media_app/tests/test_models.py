from django.test import TestCase
from media_app.models import Document
from datetime import datetime

class DocumentAssertion(TestCase):
    def assertDocmentModel(self, actual_docment, author, title, description, photo, uploaded_at):
        self.assertEqual(actual_docment.author, author)
        self.assertEqual(actual_docment.title, title)
        self.assertEqual(actual_docment.description, description)
        self.assertEqual(actual_docment.photo, photo)
        #self.assertEqual(actual_docment.uploaded_at, uploaded_at)

class TestDocumentModel(TestCase):
    def creating_a_docment_and_saving(self, author="kazuma444756@gmail.com", title="test", description="model test", photo=="./media/test.jpg", uploaded_at=datetime.now().strftime("%Y/%m/%d %H:%M:%S")):
        document = Document()
        # if name is not None:
        #     document.author = author
        # if title is not None:
        #     document.title = title
        # if description is not None:
        #     document.description = description
        # if description is not None:
        #     document.description = description
        book.save()

    def test_is_empty(self):
        saved_docments = Document.objects.all()
        self.assertEqual(saved_docments.count(), 0)

    def test_is_not_empty(self):
        self.creating_a_docment_and_saving()
        saved_docments = Document.objects.all()
        self.assertEqual(saved_docments.count(), 1)
        actual_docment = saved_docments[0]
        self.assertDocmentModel(actual_docment,"kazuma444756@gmail.com","test","model test","./media/test.jpg",datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
