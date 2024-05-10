import unittest
from app import app

class FlaskTest(unittest.TestCase):

    # Setup a test client for the app
    def setUp(self):
        self.tester = app.test_client(self)

    # Ensure that the Flask app is set up correctly
    def test_index(self):
        response = self.tester.get('/')
        self.assertEqual(response.status_code, 200)

    # Ensure the home page returns the correct content
    def test_home_content(self):
        response = self.tester.get('/')
        self.assertIn(b'Home Page', response.data)

    # Ensure the 'Add New Student' page returns the correct content
    def test_add_student_page_content(self):
        response = self.tester.get('/addstudent')
        self.assertIn(b'Add New Student', response.data)

    # Ensure that adding a new student works correctly
    def test_add_student(self):
        response = self.tester.post('/addrec', data=dict(name='Mostafa Walid', address='123 Main St', city='Cairo', pin='12345'), follow_redirects=True)
        self.assertIn(b'Record successfully added!', response.data)

    # Ensure the 'List of Students' page returns the correct content
    def test_list_students_page_content(self):
        response = self.tester.get('/list')
        self.assertIn(b'List of Students', response.data)

if __name__ == '__main__':
    unittest.main()

