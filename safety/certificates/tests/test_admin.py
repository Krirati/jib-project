from django.test import TestCase
from django.contrib import admin

from ..admin import CertificateAdmin
from ..models import Certificate


class CertificateAdminTest(TestCase):
    def test_admin_should_be_refistered(self):
        assert isinstance(
            admin.site._registry[Certificate], 
            CertificateAdmin)

    def test_admin_should_set_list_display(self):
        expected = (
            'name',
            'issued_by',
    
        )
        assert CertificateAdmin.list_display == expected
