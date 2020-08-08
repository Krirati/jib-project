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
        # When (เมื่อดึงขึ้นมาควรจะมีตามที่ set ค่าไว้)
        worker = Worker.objects.create(
            first_name = first_name,
            last_name = last_name,
            is_availble = is_availble,
            primary_phone = primary_phone,
            secondary_phone = secondary_phone,
            address = address,
        )
        # Then 
        self.assertEqual(worker.first_name, first_name)
        self.assertEqual(worker.last_name, last_name)
        self.assertTrue(worker.is_availble, is_availble)
        self.assertEqual(worker.primary_phone, primary_phone)
        self.assertEqual(worker.secondary_phone, secondary_phone)
        self.assertEqual(worker.address, address)
