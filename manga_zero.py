#oding: utf-8
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

cnt = 0

def login():
    b.get(LOGIN_URL)
    b.find_element_by_class_name('register-facebook').click()
    sleep(2)
    
    try:
        b.find_element_by_id('email').send_keys(LOGIN_ID)
        b.find_element_by_id('pass').send_keys(LOGIN_PASSWORD)
        b.find_element_by_id('loginbutton').click()
    #in case of pass login without authentication
    except:
        print("Login directly!!")
    
    #for first login by 12 hours'
    try:
        b.find_element_by_class_name('button--white.button--radius-4.button--40').click()
    except:
        print('No more getable tickets')


def getFree():
    b.get(TARGET_URL)
    sleep(2) 
    b.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    numBlueTicket = len(b.find_elements_by_class_name('chip-icon.chip-icon--blue'))

    #save manga for FREE
    for a in range(numBlueTicket):
        #open episode
        b.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        b.find_elements_by_class_name('chip-icon.chip-icon--blue')[a].click()
        print('Now loading episode ---- '+ str(a+1))
        sleep(2)
        b.find_element_by_class_name('button-direction.button-direction__horizontal').click()
        sleep(3)
        
        #get length of images to save(for counting roop)
        images = b.find_elements_by_class_name('canvas-wrapper')
        
        #save images
        for c in range(len(images)):
            png = b.find_element_by_class_name('viewer-horizontal').screenshot_as_png
            file_name = str(a+1)+'_'+ str(c+1)+'.png'
            with open('./image/'+ file_name, 'wb') as f:
                f.write(png)
            b.find_element_by_class_name('arrow.arrow-left').click()
            sleep(3)

        #close episode
        b.find_element_by_class_name('button--white.button--radius-4.button--40').click()
        sleep(2)
        b.find_elements_by_class_name('button-close')[1].click()
        sleep(4)

    cnt = numBlueTicket
    return cnt


def getManga():    
    b.get(TARGET_URL)
    sleep(3)
    b.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    numGreenTicket = len(b.find_elements_by_class_name('chip-icon.chip-icon--green'))

    if numGreenTicket > 4:
        numGreenTicket = 4
    
    #save manga using green tickets
    for x in range(numGreenTicket):
        #open episode
        b.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        try:
            b.find_elements_by_class_name('chip-icon.chip-icon--green')
            try:
                #available green ticket exists at first page
                b.find_elements_by_class_name('chip-icon.chip-icon--green')[0].click()
            except:
                #in case of available green ticket left only one
                b.find_element_by_class_name('chip-icon.chip-icon--green').click()
        except:
            try:
                #available green ticket doesn't exist at first page but next
                b.find_element_by_class_name('next.item-pagination').click()
                sleep(3)
                b.find_elements_by_class_name('chip-icon.chip-icon--green')[0].click()
            except:
                #available green ticket doesn't exist at all
                print('manga completedly saved!')
        
        print('Now loading episode ---- '+ str(cnt+x+1))
        sleep(3) 
        b.find_element_by_class_name('button-content').click()
        sleep(3)
        b.find_element_by_class_name('button-direction.button-direction__horizontal').click()
        sleep(3)

        #get length of images to save(for counting roop)
        images = b.find_elements_by_class_name('canvas-wrapper')
        
        #save images
        for y in range(len(images)):
            png = b.find_element_by_class_name('viewer-horizontal').screenshot_as_png
            file_name = str(cnt+x+1) + '_' + str(y+1)+'.png'
            with open('./image/'+ file_name, 'wb') as f:
                f.write(png)
            b.find_element_by_class_name('arrow.arrow-left').click()
            sleep(3)

    #close episode
    sleep(3)
    b.find_element_by_class_name('button--white.button--radius-4.button--40').click()
    sleep(2)
    b.find_elements_by_class_name('button-close')[1].click()
    sleep(4)



def readLogFile():
    a = open('log.csv','r+')
    manga_list = []
    for row in a:
        LINE = row.rstrip().split(',')
        ID = LINE[0]
        title = LINE[1]
        manga_list.append(title)
    return manga_list
        

def hosii():
    z = open('hosii.txt','r')
    hosii_list=[]
    for row in z:
        manga = row.rstrip()
        hosii_list.append(manga)
    return hosii_list


#b = webdriver.Chrome('./chromedriver')
#login()
#sleep(2)
hosii_list = hosii()
log_list = readLogFile()
print(hosii_list)
print(log_list)
#getFree()
#getManga()
#b.close()

