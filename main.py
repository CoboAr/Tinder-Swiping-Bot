import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

# Environment variables
FB_EMAIL = os.environ.get("FB_EMAIL")
FB_PASSWORD = os.environ.get("FB_PASSWORD")

# Optional - Automatically keep your chromedriver up to date.
# from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager
# chrome_driver_path = ChromeDriverManager().install()

# service = Service(executable_path=chrome_driver_path)
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=service, options=options)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Tinder website
driver.get("http://www.tinder.com")
time.sleep(2)

# Accept cookies
accept_cookies = driver.find_element(by=By.XPATH, value="//*[@id='u-1919424827']/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]")
accept_cookies.click()
time.sleep(2)

# Log in
login_button = driver.find_element(by=By.XPATH, value="//div[text()='Log in']")
login_button.click()
time.sleep(5)

# Log in via Facebook
facebook_login = driver.find_element(by=By.XPATH, value="//*[@id='u647161393']/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div")
facebook_login.click()

# Switch windows
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Enter Facebook credentials and type Enter
time.sleep(3)
Email = driver.find_element(by=By.ID, value="email")
Email.send_keys(FB_EMAIL)
time.sleep(2)
Password = driver.find_element(by=By.ID, value="pass")
Password.send_keys(FB_PASSWORD)
time.sleep(2)
login=driver.find_element(by=By.NAME, value="login")
login.send_keys(Keys.ENTER)
time.sleep(2)

#return to the previous window
driver.switch_to.window(base_window)

# Allow location
time.sleep(3)
allow_location=driver.find_element(by=By.XPATH, value="/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]")
allow_location.click()
time.sleep(1)

# Enable notifications
enable_notifications = driver.find_element(by=By.XPATH, value="//*[@id='u647161393']/main/div/div/div/div[3]/button[1]/div[2]/div[2]")
enable_notifications.click()
time.sleep(1)

# Swipe right for a like 10 times then exit
for n in range(10):
    time.sleep(1)
    try:
        print("right swipe")
        # like_button = driver.find_element_by_xpath(
        #     '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        # like_button.click()
        driver.find_element (By.TAG_NAME, 'body').send_keys (Keys.ARROW_RIGHT)
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)
driver.quit()