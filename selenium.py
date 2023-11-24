from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
from webdriver_manager.chrome import ChromeDriverManager
url = "https://www.ohmydollz.com/"
browser  = webdriver.Firefox()
browser.implicitly_wait(4)
browser.get(url)
browser.maximize_window()
pseudo = browser.find_element(by=By.NAME, value="pseudo")
psw = browser.find_element(by=By.NAME, value="pass")
login = browser.find_element(by=By.XPATH, value="//input[@type='image']")
pseudo.send_keys("")
psw.send_keys("")
login.click()

try:
  work = browser.find_element(by=By.XPATH, value="//a[@class='actif']")
  work.click()
except:

