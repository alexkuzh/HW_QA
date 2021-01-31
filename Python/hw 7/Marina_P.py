import unittest

from selenium import webdriver
# import requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # Methods in UnitTest should start from "test" keyword
    def test_search(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@type="submit"]')))
        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page has", driver.title + " as Page title")
        driver.implicitly_wait(3)
        popUp = driver.find_element_by_xpath('//*[@value="Close and accept"]')
        if popUp:
            popUp.click()
        driver.find_element_by_id("g2-name").clear()
        driver.find_element_by_id("g2-name").send_keys("Musya")
        driver.find_element_by_id("g2-email").clear()
        driver.find_element_by_id("g2-email").send_keys("abc@mail.com")
        driver.find_element_by_name("g2-message").clear()
        driver.find_element_by_name("g2-message").send_keys("My message is short.")
        driver.implicitly_wait(3)
        popUp2 = driver.find_element_by_xpath('//*[@class="bottom-sticky__ad-close-btn"]')
        if popUp2:
            popUp2.click()
        submit = driver.find_element_by_xpath('//*[@type="submit"]')
        body = driver.find_element_by_xpath('//div[@id="page"]')
        driver.implicitly_wait(5)
        if submit:
            submit.click()
        elif driver.body.send_keys(Keys.PAGE_DOWN):
            submit.click()
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
        except TimeoutException:
            print("Page can't Go Back!")
        driver.implicitly_wait(10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-55")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-34")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-56")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-30")))
        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page has", driver.title + " as Page title")

    def test_search_chrome_1120x550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        driver.get("https://qasvus.wordpress.com/")

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@type="submit"]')))
        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page has", driver.title + " as Page title")

        driver.find_element_by_id("g2-name").clear()
        driver.find_element_by_id("g2-name").send_keys("Musya")
        driver.find_element_by_id("g2-email").clear()
        driver.find_element_by_id("g2-email").send_keys("abc@mail.com")
        driver.find_element_by_name("g2-message").clear()
        driver.find_element_by_name("g2-message").send_keys("My message is short.")
        driver.find_element_by_xpath('//*[@type="submit"]').click()

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
        except TimeoutException:
            print("Page can't Go Back!")

        driver.implicitly_wait(10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-55")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-34")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-56")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-30")))
        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page has", driver.title + " as Page title")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
