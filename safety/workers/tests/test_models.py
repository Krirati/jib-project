import os
from unittest.mock import MagicMock

from django.core.files import File
from django.test import TestCase

from ..models import Worker

class TestWorker(TestCase):
    def test_worker_should_have_definded_field(self):
        # Given (ว่าเรามีอะไร)
        first_name = 'Keng'
        last_name = 'Mak'
        is_availble = True
        primary_phone = '081-689-777x'
        secondary_phone = '081-687-778x'
        address = 'Geeky Base All Start'
        image_mock = MagicMock(spec=File)
        image_mock.name = 'nine.png'

        # When (เมื่อดึงขึ้นมาควรจะมีตามที่ set ค่าไว้)
        worker = Worker.objects.create(
            first_name = first_name,
            last_name = last_name,
            image_profile = image_mock,
            is_availble = is_availble,
            primary_phone = primary_phone,
            secondary_phone = secondary_phone,
            address = address,
        )
        
        # Then 

        assert worker.first_name == first_name
        assert worker.is_availble is True

        self.assertEqual(worker.first_name, first_name)
        self.assertEqual(worker.last_name, last_name)
        self.assertEqual(worker.image_profile.name, image_mock.name)
        self.assertTrue(worker.is_availble, is_availble)
        self.assertEqual(worker.primary_phone, primary_phone)
        self.assertEqual(worker.secondary_phone, secondary_phone)
        self.assertEqual(worker.address, address)

        os.remove('media/nine.png')
