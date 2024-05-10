import unittest
from app import app

class APIValidationTest(unittest.TestCase):
    
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

    # Test the response of the home page
    def test_home_page_response(self):
        response = self.app.get('/')
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the response data contains expected content
        self.assertIn(b'Home Page', response.data)

    # Test the response of the add student page
    def test_add_student_page_response(self):
        response = self.app.get('/addstudent')
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the response data contains expected content
        self.assertIn(b'Add New Student', response.data)

    # Test the response of the list students page
    def test_list_students_page_response(self):
        response = self.app.get('/list')
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the response data contains expected content
        self.assertIn(b'List of Students', response.data)

    # Test adding a new student
    def test_add_student_response(self):
        response = self.app.post('/addrec', data=dict(name='Ziad Mohamed', address='123 Main St', city='Cairo', pin='12345'))
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the response data contains expected content
        self.assertIn(b'Record successfully added!', response.data)

    # Test listing all students after adding a new student
    def test_list_students_after_adding_student(self):
        # Add a new student
        self.app.post('/addrec', data=dict(name='Ziad Mohamed', address='123 Main St', city='Cairo', pin='12345'))
        # Get the list of all students
        response = self.app.get('/list')
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the response data contains the newly added student's name
        self.assertIn(b'John Doe', response.data)

if __name__ == '__main__':
    unittest.main()
