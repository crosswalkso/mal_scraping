from rest_framework.test import APITestCase
from users.models import User

"""
python manage.py test animes --settings='config.settings_test'
"""


# Create your tests here.
# python manage.py test
# function : test_ ...
# [o] start_date, episodes, duration
# [o] season_id
# request.data -> 유저가 건들면 안되는 data는 read_only=True
class TestPutSeasonAnimes(APITestCase):
    def setUp(self):
        user = User.objects.get(
            username="crossp",
        )

        self.user = user

    def test_put_anime(self):
        self.client.force_login(
            self.user,
        )
        URL = "/api/v1/seasons/1/animes/23"
        DATA = {
            "season": {"id": 2},
            "title": "Onepiece",
            "duration": "255 min",
        }
        response = self.client.put(
            URL,
            data=DATA,
            format="json",
        )
        print(response.json())
        self.assertEqual(response.status_code, 200, "failed")
