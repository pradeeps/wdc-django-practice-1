from django.test import TestCase
import datetime

class TasksTestCase(TestCase):

    def test_hello_world(self):
        """Should return Hello World while GETing to /hello-world URL"""
        response = self.client.get('/hello-world/')
        assert response.status_code == 200
        assert 'Hello World' in str(response.content)

    def test_date(self):
        """Should return Hello World while GETing to /hello-world URL"""
        response = self.client.get('/date/')
        assert response.status_code == 200
        cur_date = datetime.date.today().strftime("%d, %B %Y")
        assert cur_date in str(response.content)