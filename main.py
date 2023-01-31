from tkinter import *
import json
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


root = Tk()

def btn_click():
    URL_TEMPLATE = urlInput.get()

    my_service = Service('C:\webdriver\chromedriver.exe')
    my_options = Options()
    my_options.add_extension("C:\webdriver\i1.18.13_0.crx")
    my_options.add_argument("--disable-infobars")
    my_options.add_argument("start-maximized")
    browser = webdriver.Chrome(service=my_service, options=my_options)

    browser.get(URL_TEMPLATE)

    label = browser.find_element(By.XPATH, "//label[text()='Get skin data, by default']")
    checkbox = label.find_element(By.CSS_SELECTOR, 'span.ui-checkboxradio-icon.ui-corner-all.ui-icon.ui-icon-background.ui-icon-blank').click()

    items = browser.find_elements(By.CLASS_NAME, 'market_listing_item_name_block')
    floats = browser.find_elements(By.CLASS_NAME, 'itemfloat')
    time.sleep(1)
    name = [x.text for x in items]
    floats_item = [x.text for x in floats]

    result_json = []
    for floats_item, name in zip(floats_item, name):
        result_json.append({
            'name': name,
            'float': floats_item
        })

    with open('res.json', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)

root.title('SteamParser')
root['bg'] = '#000000'
root.geometry('300x250')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=600, width=600)
canvas.pack()

frame = Frame(root, bg = '#696969')
frame.place(relwidth=1,relheight=1)

urlInput = Entry(frame, bg = 'white')
urlInput.pack()

btn = Button(frame, text = 'parse', bg = 'white', command=btn_click)
btn.pack()

root.mainloop()



