from django.test import TestCase,Client
from contact.models import Contact

# Create your tests here.
class ContactTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(first_name="shyam", last_name="kc", email="test@tst.com", subject="hello", message="hi")
        Contact.objects.create(first_name="hari", last_name="kc", email="test@tst.com", subject="hello", message="hi")

    def test_contact_name(self):
        shyam = Contact.objects.get(first_name="shyam")
        hari = Contact.objects.get(first_name="hari")
        self.assertEqual(shyam.get_first_name(), 'shyam')
        self.assertEqual(hari.get_first_name(), 'hari')

class ContactTestCase2(TestCase):

    def test_contacts_get_request(self):
        c = Client()
        response = c.post('/api/v1/contacts/',
                          {'first_name': 'test', 'last_name': 'test', 'email': 'princenirajan12@gmail.com',
                           'subject': 'test', 'message': 'test'})
        print('post', response)
        status_code = response.status_code
        self.assertEquals(status_code, 200)

        response = c.get('/api/v1/contacts/')
        status_code = response.status_code
        print(response.json())
        self.assertEquals(status_code, 200)



