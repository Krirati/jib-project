from django.test import TestCase

from ..models import Certificate
from ..serializers import CertificateModelSerializer

class TestCertificateModelSerializer(TestCase):
    def test_model_serializer_should_set_certificate(self):
        # print(dir(CertificateModelSerializer.Meta.model))
        assert CertificateModelSerializer.Meta.model == Certificate

    def test_model_serializer_use_all_fields(self):
        assert CertificateModelSerializer.Meta.fields == '__all__'
