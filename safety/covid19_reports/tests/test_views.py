from django.test import TestCase
from unittest.mock import patch
# Create your tests here.
class TestCovid19ReportsView(TestCase):
    @patch('covid19_reports.views.requests.get')
    def test_views_should_be_accessible(self, _):
        response = self.client.get('/covid19-reports/')
        self.assertEqual(response.status_code, 200)

    @patch('covid19_reports.views.requests.get')
    def test_views_call_covid19_api(self,mock):
        self.client.get('/covid19-reports/')
        mock.assert_called_once_with(
            'https://covid19.th-stat.com/api/open/today'
        )