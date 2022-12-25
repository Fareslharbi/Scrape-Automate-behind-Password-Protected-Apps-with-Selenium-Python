from urllib.parse import urlparse
import getpass
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
import os
my_username = '***'

#my_password = getpass.getpass("Enter Your Password :")
my_password = '****'
# print(my_password)
browser = webdriver.Chrome()
url = "https://www.instagram.com"

browser.get(url)

# Username
"""
<input name="username" type="text" >
"""
time.sleep(2)
search_el = browser.find_element("name", "username")
search_el.send_keys(my_username)

# Password
"""
<input name="password" type="text">
"""
time.sleep(2)
search_el = browser.find_element("name", "password")
search_el.send_keys(my_password)

# Click
"""
<button type="submit" />
"""
time.sleep(2)
submit_btn_el = browser.find_element(By.CSS_SELECTOR, "button[type='submit']" )
submit_btn_el.click()

# # Download the entire HTML page 
# body_el = browser.find_element(By.CSS_SELECTOR, "body")
# html_text = body_el.get_attribute("innerHTML")
# # print(html_text)
 

# Follow new person in instagram
"""
<button type="button">

<buttontype="button">Follow</button>
"""

# Using XPATH instead of By.CSS_SELECTOR or name
# my_btn_xpath = "//button"
# body_el = browser.find_element(By.XPATH, my_btn_xpath)
def click_to_follow(browser):
    # my_follow_btn_xpath = "//a[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    # my_follow_btn_xpath = "//button[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    my_follow_btn_xpath = "//*[contains(text(), 'Follow')][not(contains(text(), 'Following'))]" # Give me All the button that contain the word follow // The star means give me all the element that contain the follow
    follow_btn_elments = browser.find_elements(By.XPATH, my_follow_btn_xpath)
    for btn in follow_btn_elments: # Go through all the follow buttons
        time.sleep(2) # Self throttle so that Instagram don't detect us
        try:
            btn.click() # This will click all the follow button
        except:
            pass
time.sleep(20)
new_user_url = 'https://www.instagram.com/ted/'
browser.get(new_user_url)
# click_to_follow(browser)



# time.sleep(10)
# the_rock_url = "https://www.instagram.com/therock/"
# browser.get(the_rock_url)

# post_url_pattern = "https://www.instagram.com/p/<post-slug-id>"

# post_xpath_str = "//a[contains(@href, '/p/')]"
# post_links = browser.find_elements(By.XPATH, post_xpath_str)

# post_link_el = None
# if len(post_links) > 0:
#     post_link_el = post_links[0]

# if post_link_el != None:
#     post_href = post_link_el.get_attribute("href")
#     browser.get(post_href)



video_els = browser.find_elements(By.XPATH, "//video")
images_els = browser.find_elements(By.XPATH, "//img")


base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

# PIL to verify the size of any given image.

def scrape_and_save(elements):
    for el in elements:
        # print(img.get_attribute('src'))
        url = el.get_attribute('src')
        base_url = urlparse(url).path
        filename = os.path.basename(base_url)
        filepath = os.path.join(data_dir, filename)
        if os.path.exists(filepath):
            continue
        with requests.get(url, stream=True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
#scrape_and_save(images_els)


"""
LONG TERM Goal:
Use machine learning to classify the post's
image or video
and then comment in a relevant fashion
"""

"""
<textarea aria-label="Add a comment…" placeholder="Add a comment…" class="Ypffh" autocomplete="off" autocorrect="off" style="height: 18px;"></textarea>
"""

def automate_comment(browser, content="That is cool!"):
    time.sleep(3)
    comment_xpath_str = "//textarea[contains(@placeholder, 'Add a comment')]"
    comment_el = browser.find_element(By.XPATH, comment_xpath_str)
    comment_el.send_keys(content)
    submit_btns_CSS_SELECTOR = "button[type='submit']"
    submit_btns_els = browser.find_elements(By.CSS_SELECTOR, submit_btns_CSS_SELECTOR)
    time.sleep(2)
    for btn in submit_btns_els:
        try:
            btn.click()
        except:
            pass

def automate_likes(browser):
    like_heart_svg_xpath = "//*[contains(@aria-label, 'Like')]"
    all_like_hearts_elements = browser.find_elements(By.XPATH, like_heart_svg_xpath)
    max_heart_h = -1
    for heart_el in all_like_hearts_elements:
        h = heart_el.get_attribute("height")
        current_h = int(h)
        if current_h > max_heart_h:
            max_heart_h = current_h
    all_like_hearts_elements = browser.find_elements(By.XPATH, like_heart_svg_xpath)
    for heart_el in all_like_hearts_elements:
        h = heart_el.get_attribute("height")
        if h == max_heart_h or h == f"{max_heart_h}":
            parent_button = heart_el.find_element(By.XPATH, '..')
            time.sleep(2)
            try:
                parent_button.click()
            except:
                pass
#automate_likes(browser)
#puhvuq-7keTxi-savqow