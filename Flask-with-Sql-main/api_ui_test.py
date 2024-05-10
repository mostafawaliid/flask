import unittest
from selenium import webdriver  # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore

class APIUITest(unittest.TestCase):

    def setUp(self):
        # Initialize Selenium WebDriver
        self.driver = webdriver.Chrome()  # Use appropriate WebDriver (e.g., Chrome, Firefox)
        self.driver.get("http://localhost:5000")  # Replace with the URL of your Flask app

    def test_home_page(self):
        # Test the home page
        assert "Home Page" in self.driver.title

    def test_add_student_page(self):
        # Test the add student page
        self.driver.get("http://localhost:5000/addstudent")
        assert "Add New Student" in self.driver.title

    def test_add_student(self):
        # Test adding a new student
        self.driver.get("http://localhost:5000/addstudent")
        name_input = self.driver.find_element_by_name("name")
        name_input.send_keys("Mostafa Walid")  # Updated name
        address_input = self.driver.find_element_by_name("address")
        address_input.send_keys("123 Main St")
        city_input = self.driver.find_element_by_name("city")
        city_input.send_keys("Cairo")
        pin_input = self.driver.find_element_by_name("pin")
        pin_input.send_keys("12345")
        submit_button = self.driver.find_element_by_name("submit")
        submit_button.click()
        assert "Record successfully added!" in self.driver.page_source

    def tearDown(self):
        # Clean up after tests
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
