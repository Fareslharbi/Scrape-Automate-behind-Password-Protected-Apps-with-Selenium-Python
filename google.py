from selenium import webdriver
import time
browser = webdriver.Safari()
from selenium.webdriver.common.by import By
url = 'https://google.com'
browser.get(url)


"""
<input type='text' class='' id='' name='??' />
<input name="q" type="text">
"""
time.sleep(2)
name = 'q'
#print(dir(browser)) # all the functions inside browser
search_el = browser.find_element("name", "q")
#print(search_el)
search_el.send_keys("selenium python") # we need delay incase it open so fast and can't type fast enough

"""
<input type='submit' />
<button type='submit' />
<form></form>

<input type="submit" > We only need <type> because <name> might change
"""

submit_btn_el = browser.find_element(By.CSS_SELECTOR, "input[type='submit']" )
print(submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()