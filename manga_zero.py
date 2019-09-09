#coding: utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'
UNDERLINE = '\033[4m'
from time import sleep
import sys
import random
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


LOGIN_ID = 'kozasamizuki@gmail.com'
LOGIN_PASSWORD = 'nekoneko55'
LOGIN_URL = 'https://manga-zero.com/login'
TARGET_URL = 'https://manga-zero.com/product/3769'

def login():
    b.get(LOGIN_URL)
    b.find_element_by_class_name('register-facebook').click()
    sleep(2)
    try:
        b.find_element_by_id('email').send_keys(LOGIN_ID)
        b.find_element_by_id('pass').send_keys(LOGIN_PASSWORD)
        b.find_element_by_id('loginbutton').click()
    except:
        print("Login directly!!")
    try:
        b.find_element_by_class_name('button--white.button--radius-4.button--40').click()
    except:
        print('No more getable tickets')

def getFree():
    b.get(TARGET_URL)
    sleep(1)
    b.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    numBlueTicket = len(b.find_elements_by_class_name('chip-icon.chip-icon--blue'))
    for a in range(numBlueTicket):
        b.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        b.find_elements_by_class_name('chip-icon.chip-icon--blue')[a].click()
        print('Now loading episode ---- '+ str(a+1))
        sleep(3)
        b.find_element_by_class_name('button-direction.button-direction__horizontal').click()
        sleep(3)

        images = b.find_elements_by_class_name('canvas-wrapper')
        for c in range(len(images)):
            png = b.find_element_by_class_name('viewer-horizontal').screenshot_as_png
            file_name = str(a+1)+'_'+ str(c+1)+'.png'
            with open('./image/'+ file_name, 'wb') as f:
                f.write(png)
            b.find_element_by_class_name('arrow.arrow-left').click()
            sleep(2)

        b.find_element_by_class_name('button--white.button--radius-4.button--40').click()
        sleep(1)
        b.find_elements_by_class_name('button-close')[1].click()
        sleep(3)

def getManga():
    b.get(TARGET_URL)
    sleep(1)
    b.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    b.find_elements_by_class_name('chip-icon.chip-icon--blue')[0].click()
    #sleep(2)
    #b.find_element_by_class_name('button-content').click()
    sleep(3)
    b.find_element_by_class_name('button-direction.button-direction__horizontal').click()
    #画像保存
    sleep(3)
    images = b.find_elements_by_class_name('canvas-wrapper')
    for a in range(len(images)):
        png = b.find_element_by_class_name('viewer-horizontal').screenshot_as_png
        file_name = str(a)+'.png'
        with open('./image/'+ file_name, 'wb') as f:
            f.write(png)
        b.find_element_by_class_name('arrow.arrow-left').click()
        sleep(2)

    b.find_element_by_class_name('button--white.button--radius-4.button--40').click()
    
    
b = webdriver.Chrome('./chromedriver')

login()
sleep(2)
getFree()
#getManga()
#b.close()

