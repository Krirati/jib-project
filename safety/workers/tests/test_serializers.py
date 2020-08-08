from django.test import TestCase
from ..models import Worker
from ..serializers import WorkerSerializer

class TestWorkerSerializer(TestCase):
    def test_serializer_sholud_return_correct_serializer_data(self):
        worker = Worker.objects.create(
            first_name= 'Nine',
            last_name= 'K',
            is_availble= True,
            primary_phone= '1234567890',
            secondary_phone= '1234567890',
            address= 'Oddtria',
        )
        serializer = WorkerSerializer(worker)

        expected = {
            'first_name': 'Nine',
            'last_name': 'K',
            'is_availble': True,
            'primary_phone': '1234567890',
            'secondary_phone': '1234567890',
            'address': 'Oddtria',
        }

        assert serializer.data == expected