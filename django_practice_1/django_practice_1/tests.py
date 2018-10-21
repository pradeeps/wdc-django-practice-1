from django.test import TestCase
import datetime

class TasksTestCase(TestCase):

    def test_hello_world(self):
        """Should return Hello World while GETing to /hello-world URL"""
        response = self.client.get('/hello-world/')
        assert response.status_code == 200
        assert 'Hello World' in response.content.decode('UTF-8')

    def test_date(self):
        """Should check if current date is same as /date while GETing to /date URL"""
        response = self.client.get('/date/')
        assert response.status_code == 200
        cur_date = datetime.date.today().strftime("%d, %B %Y")
        assert cur_date in str(response.content)

    def test_my_age(self):
        """Should return age while GETing to /my-age/year/month/day URL"""
        year, month, day = 1900, 8, 8
        url = '/my-age/'+str(year)+'/'+str(month)+'/'+str(day)
        response = self.client.get(url)
        assert response.status_code == 200
        assert 'Your age is 118 years old' in response.content.decode('UTF-8')

    def test_next_birthday(self):
        """Should return age while GETing to /my-age/year/month/day URL"""
        birthday = '2000-01-01'
        url = '/next-birthday/'+str(birthday)
        response = self.client.get(url)
        assert response.status_code == 200
        assert 'Days untill next birthday: 71 days' in response.content.decode('UTF-8')

    def test_profile(self):
        """Should return Hello World while GETing to /hello-world URL"""
        response = self.client.get('/profile/')
        assert response.status_code == 200
        assert 'My name is Pradeep and I\'m 67 years old.' in response.content.decode('UTF-8')

    def test_authors(self):
        """Should return lenght of authors while GETing to /authors URL"""
        response = self.client.get('/authors/')
        assert response.status_code == 200

    def test_author(self):
        """Should return lenght of authors while GETing to /authors URL"""
        import random
        authors_list = ['poe', 'borges']
        url = '/author/'+str(random.choice(authors_list))
        response = self.client.get(url)
        assert response.status_code == 200
