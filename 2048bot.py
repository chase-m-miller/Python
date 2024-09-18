#! python3
# 2048bot.py - This program opens a web browser and automatically plays 2048.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element('tag name', 'html')
htmlElem.send_keys(Keys.END)
