import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Keys class provide keys in the keyboard like RETURN, F1, ALT, etc
# By class is used to locate elements within a document
# Currently supported drivers: Firefox, Chrome, IE and Remote

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox() # Creates an instance of the Firefox webdriver

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org") # naivages to the provided url
        self.assertIn("Python", driver.title)
        element = driver.find_element(By.NAME, "q")
        element.clear()
        element.send_keys("pycon")
        element.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()