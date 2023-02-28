import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def test_sample_test():
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    chrome_driver.get('randomwebsite')
    chrome_driver.maximize_window()
 
    chrome_driver.find_element_by_XXX
 
    title = "Any title really, assertion test"
    assert title == chrome_driver.title
 
    
    chrome_driver.close()