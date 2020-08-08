import json


from django.test import TestCase

from rest_framework.test import APIClient, APITestCase

from ..models import Worker

class TestWorkerListView(APITestCase):
    def test_view_should_be_accessible(self):
        response = self.client.get('/workers/')
        # print(dir(response))
        self.assertEqual(response.status_code, 200)

    def test_view_should_render_list_of_worker_names(self):
        # Given
        Worker.objects.create(
            first_name = 'Nine',
            last_name = '1',
            is_availble = True,
            primary_phone = '0000000000',
            secondary_phone = '0000000001',
            address = 'address',
        )
        Worker.objects.create(
            first_name = 'Kririati',
            last_name = '2',
            is_availble = False,
            primary_phone = '0000000003',
            secondary_phone = '0000000004',
            address = 'ODDS',
        )
        # When

        # client = APITestCase()
        response = self.client.get('/workers/')


        # Then

        # self.assertContains(response, '<li>Nine</li>')
        # self.assertContains(response, '<li>Kririati</li>')
        # self.maxDiff = None

        expected = [
            {
                "first_name": "Nine",
                "last_name": "1",
                "is_availble": True,
                "primary_phone": "0000000000",
                "secondary_phone": "0000000001",
                "address": "address"
            },
            {
                "first_name": "Kririati",
                "last_name": "2",
                "is_availble": False,
                "primary_phone": "0000000003",
                "secondary_phone": "0000000004",
                "address": "ODDS"
            }
        ]
        self.assertEqual(response.data,expected)