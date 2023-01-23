from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
URL_TEMPLATE = "https://steamcommunity.com/market/listings/730/StatTrak™%20AWP%20%7C%20Asiimov%20%28Battle-Scarred%29"
s = Service('D:\WebDriver_Chrome\chromedriver.exe')
o = Options()
o.add_extension("D:\WebDriver_Chrome\extension\extension_1_18_12_0.crx")
o.add_argument("--disable-infobars")
o.add_argument("start-maximized");
browser = webdriver.Chrome(service=s, options=o)
browser.get(URL_TEMPLATE)

label = browser.find_element(By.XPATH, "//label[text()='Get skin data, by default']")
select = label.find_element(By.CSS_SELECTOR, 'span.ui-checkboxradio-icon.ui-corner-all.ui-icon.ui-icon-background.ui-icon-blank').click()

time.sleep(100)