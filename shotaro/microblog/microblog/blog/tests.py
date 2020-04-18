from django.test import TestCase,Client

class BlogTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_index_access(self):
        #self.assert_(True) #失敗したら止まる
        res = self.c.get('/')
        self.assertEqual(200,res.status_code)
    
    def index_access_fail(self):
        res = self.c.get('/create')
        print(res.status_code)
        self.assertEqual(404,res.status_code)
