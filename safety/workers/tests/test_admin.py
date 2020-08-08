from django.test import TestCase
from django.contrib import admin

from ..models import Worker
from ..admin import WorkerAdmin


class WorkerAdminTest(TestCase):
    def test_admin_should_be_refistered(self):
        self.assertTrue(isinstance(admin.site._registry[Worker], WorkerAdmin))

    def test_admin_should_set_list_display(self):
        expected = (
            'first_name',
            'last_name',
            'is_availble',
            'primary_phone',
            'secondary_phone'
        )
        self.assertEqual(WorkerAdmin.list_display, expected)

    def test_admin_should_set_list_filter(self):
        expected = (
            'is_availble'
        )
        self.assertTrue(WorkerAdmin.list_filter, expected)