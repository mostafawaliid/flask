import unittest
from app import app

class FlaskIntegrationTest(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test adding a new student and then listing all students to check if the new student is added
    def test_add_student_and_list_students(self):
        self.app.post('/addrec', data=dict(name='Mostafa Walid', address='123 Main St', city='Cairo', pin='12345'))
        response = self.app.get('/list')
        self.assertIn(b'Mostafa Walid', response.data)

    # Test accessing the home page
    def test_home_page_access(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home Page', response.data)

    # Test accessing the add student page
    def test_add_student_page_access(self):
        response = self.app.get('/addstudent')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add New Student', response.data)

    # Test accessing the list students page
    def test_list_students_page_access(self):
        response = self.app.get('/list')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'List of Students', response.data)

if __name__ == '__main__':
    unittest.main()


