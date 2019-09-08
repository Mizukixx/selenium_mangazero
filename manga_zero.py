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
        b.find_element_by_class_name('button--white button--radius-4 button--40').click()
    except:
        print('No more tickets you can get')

def getManga():
    b.get(TARGET_URL)
    

b = webdriver.Chrome('./chromedriver')

login()
sleep(2)
getManga()
#b.close()

#one-click注文オン
#b.find_element_by_class_name('a-size-mini').click()
#while True:
#	# 値段
#	p = b.find_element_by_id('priceblock_ourprice').text
#	print(str(p))
#	p = int(str(p).replace('￥','').replace(',',''))
#	#ショップ
#	shop = b.find_element_by_id('merchant-info').text
#	shop = shop.split('この商品は、')[1].split(' が販売、発送します。')[0]
#	shop = shop.replace('が販売し、Amazon.co.jp が発送します。','').replace('この出品商品にはコンビニ・ATM・ネットバンキング・電子マネー払いが利用できます。','').replace(' ギフトラッピングを利用できます。','')
#	#商品名
#	title = b.find_element_by_id('title').text
#	print('========================================')
#	print(PURPLE+'¥'+str(p)+ ENDC+' '+shop+ ' ' +UNDERLINE+OKBLUE+title+ENDC)
#	print('========================================')
	#値段が希望額以下であり，かつ，ショップがAmazonである時のみ購入
#	if p <=lim and shop == 'Amazon.co.jp':
#		break
#	else:
#		b.refresh()
#	time.sleep(random.uniform(4, 7))
#	time.sleep(0.3)
#	print('*****')
#	time.sleep(0.3)
#	print('****')
#	time.sleep(0.3)
#	print('***')
#	time.sleep(0.3)
#	print('**')
#	time.sleep(0.3)
#	print('*')
#
#b.find_element_by_id('one-click-button').click()
#b.find_element_by_id('buy-now-button').click()
#time.sleep(1)
#b.find_element_by_name('ppw-widgetEvent:SetPaymentPlanSelectContinueEvent').click()
#time.sleep(2)
#placeYourOrder1
#b.find_element_by_xpath("//input[@title='注文を確定する']").click();
#b.find_element_by_class_name('a-button-text.place-your-order-button').click()
#print('商品を購入しました')
#LINE_notify(ITEM_URL)
#print(OKGREEN+'LINEにお知らせしました'+ENDC)
