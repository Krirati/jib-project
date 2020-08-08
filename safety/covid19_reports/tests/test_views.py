from django.test import TestCase
from unittest.mock import patch
# Create your tests here.
class TestCovid19ReportsView(TestCase):
    @patch('covid19_reports.views.requests.get')
    def test_views_should_be_accessible(self, _): #ใส่ _  เมื่อไม่ต้องการรับ parameter นั้น
        response = self.client.get('/covid19-reports/')
        self.assertEqual(response.status_code, 200)

    @patch('covid19_reports.views.requests.get')
    def test_views_call_covid19_api(self,mock):
        self.client.get('/covid19-reports/')
        mock.assert_called_once_with(
            'https://covid19.th-stat.com/api/open/today'
        )

    @patch('covid19_reports.views.requests.get')
    def test_view_should_render_number_of_confime(self,mock):
        r = mock.return_value
        r.json.return_value = { # ตรงไหนที่เคยเป็น วงเล็บ เอามาใช้จริงให้เอาออก
            "Confirmed": 3345,
            "Recovered": 3148,
            "Hospitalized": 139,
            "Deaths": 58,
            "NewConfirmed": 50,
            "NewRecovered": 0,
            "NewHospitalized": 15,
            "NewDeaths": 0,
            "UpdateDate": "07/08/2020 11:36",
            "Source": "https://covid19.th-stat.com/",
            "DevBy": "https://www.kidkarnmai.com/",
            "SeverBy": "https://smilehost.asia/"
        }
        response = self.client.get('/covid19-reports/')
        self.assertContains(response, 'NewConfirmed: 50')