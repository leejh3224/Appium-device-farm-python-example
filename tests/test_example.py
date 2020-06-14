import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


DIV_SELECTOR = "i_am_an_id"
TEXT_INPUT_SELECTOR = "comments"


def wait_for_input_text(driver, id, text):
    """Wait for the text appears on input with given id

    Args:
        driver {webdriver}: appium driver
        id {string}: element id
        text {string}: text to wait for

    Returns:
        bool: whether the value of an element matches given text
    """
    element = driver.find_element_by_id(id)
    return element.get_attribute("value") == text


class ExampleTest(unittest.TestCase):
    def setUp(self):
        # This config can be used for iOS Simulator on your local machine
        capabilities = dict(
            platformName="iOS",
            platformVersion="13.5",  # check platform version of your local simulator
            automationName="XCUITest",
            browserName="Safari",
            deviceName="iPhone SE (2nd generation)",  # change this as well
        )

        # use empty dictionary for device farm
        # capabilities = {}

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)

    def test_hello_world(self):

        self.driver.get("http://saucelabs.com/test/guinea-pig")

        # make sure you wait for an element to be located
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, DIV_SELECTOR))
        )

        div = self.driver.find_element_by_id(DIV_SELECTOR)
        self.assertEqual("I am a div", div.text)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, TEXT_INPUT_SELECTOR))
        )

        text = "My Comments"

        # Simulate text input keypress
        comments = self.driver.find_element_by_id(TEXT_INPUT_SELECTOR)
        comments.send_keys(text)

        # You can use lambda for custom wait conditions
        WebDriverWait(self.driver, 5).until(
            lambda driver: wait_for_input_text(driver, TEXT_INPUT_SELECTOR, text)
        )

        self.assertEqual(text, comments.get_attribute("value"))

        # You can take screenshot
        filename = "iPhone SE2.png"
        self.driver.get_screenshot_as_file(filename)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
