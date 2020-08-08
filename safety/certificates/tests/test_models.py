from django.test import TestCase

from ..models import Certificate

class TestCerticates(TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass


    def certificate(self):
        # Given (ว่าเรามีอะไร)
        name = 'Certficates'
        issued_by = 'Proof'
    
        # When (เมื่อดึงขึ้นมาควรจะมีตามที่ set ค่าไว้)
        certificate = Certificate.objects.create(
            name = name,
            issued_by = issued_by,
            
        )
        
        # Then 

        assert certificate.name == name
        assert certificate.issued_by == issued_by
