from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element('link text', 'Read Online for Free')
    print('Found <%s> element with that link text!' % (elem.tag_name))
    elem.click()
except Exception:
    print('Was not able to find an element with that name.')
