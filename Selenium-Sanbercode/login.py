import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_success_login(self):
    # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(1)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

    # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)

    def test_b_success_login(self):
    # steps
        driver = self.browser #buka web browser
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(1)
        driver.find_element(By.ID,"email").send_keys("nadirarama98@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("dira039801") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signin_login").click()
        time.sleep(1)

    # validasi
        response_data = driver.find_element(By.CLASS_NAME,"swal2-title").text
        self.assertIn('Welcome nadira', response_data)

    def test_c_success_signup(self):
    # steps
        driver = self.browser #buka web browser
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(1)
        driver.find_element(By.ID, "signUp").click()
        driver.find_element(By.ID,"name_register").send_keys("rama") # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("nadira_ramadani@yahoo.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("rama1998") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(1)

    # validasi
        response_data = driver.find_element(By.CLASS_NAME,"swal2-title").text
        self.assertIn('berhasil', response_data)

    def tearDown(self):
     self.browser.close()

if __name__ == "__main__":
    unittest.main()

    