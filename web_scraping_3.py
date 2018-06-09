from selenium import webdriver

link_for_get = 'https://...'

browser = webdriver.Firefox()
browser.get(link_for_get)

part_for_css_selector = ''

elem = browser.find_element_by_css_selector(part_for_css_selector)
elem.click()
# for clicking on that element of the page
elems = browser.find_elements_by_css_selector('p')
len(elems)
# it returns a list of elements
# to write into an element
searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('hello')
browser.submit()

# for controlling the browser
browser.back()
browser.forward()
browser.refresh()
browser.quit()

# elem.text gives the text inside that element in the webpage
print(elem.text)