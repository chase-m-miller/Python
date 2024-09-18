#! python3
# 2048bot.py - This program opens a web browser and automatically plays 2048.

from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://google.com/')
