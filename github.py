import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Github:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        login_url = "https://github.com/login"

        self.driver.get(login_url)

        element = self.driver.find_element(By.ID, "login_field")
        element.clear()
        element.send_keys(self.username)

        element = self.driver.find_element(By.ID, 'password')
        element.clear()
        element.send_keys(self.password)
        element.send_keys(Keys.ENTER)

    def create_repo(self, repo_name):
        self.login()

        new_repo_url = 'https://github.com/new'

        self.driver.get(new_repo_url)

        element = self.driver.find_element(By.ID, 'repository_name')
        element.clear()
        element.send_keys(repo_name)
        element.submit()
