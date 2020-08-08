from django.test import TestCase
from django.contrib import admin

from ..models import Certificate
from ..admin import CertificateAdmin


class CertificateAdminTest(TestCase):
    def test_admin_should_be_refistered(self):
        self.assertTrue(isinstance(
            admin.site._registry[Certificate], 
            CertificateAdmin))

    def test_admin_should_set_list_display(self):
        expected = (
            'name',
            'issued_by',
        )
        self.assertEqual(CertificateAdmin.list_display, expected)
