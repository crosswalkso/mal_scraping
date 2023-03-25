from rest_framework.test import APITestCase
from users.models import User

"""
python manage.py test seasons --settings='config.settings_test'
"""


# Create your tests here.
# python manage.py test
# function : test_ ...
class TestPutSeason(APITestCase):
    def setUp(self):
        user = User.objects.get(
            username="crossp",
        )

        self.user = user

    def test_seasons(self):
        self.client.force_login(
            self.user,
        )
        URL = "/api/v1/seasons/2"
        DATA = {
            "season_name": "Summer 2023",
        }
        response = self.client.put(
            URL,
            data=DATA,
            format="json",
        )

        print(response.json())

        # PUT 정상동작하는지 확인
        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
