#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
                   Code By BeRLiN
                 twitter @iAhmedika
'''
from selenium import webdriver
import pyautogui
import time
import keyboard
from config import *


def jdara():
    url = r"C:\Users\BeRLiN\Desktop\Automation Project\geckodriver.exe" # geckodriver Path

    driver = webdriver.Firefox(executable_path=url)

    driver.get('https://eservices.mcs.gov.sa/Jadara3/(S(jjfr5iqojfxemi1q2tjshjdq))/users/index.aspx') # url get
    clickibshr = driver.find_element_by_xpath(
         "/html/body/form/div[3]/div[4]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/input"
    ) # address button by xPath
    clickibshr.click() # click button to go ibsher website

    userName = driver.find_elements_by_class_name("c-input") # address to user name by class name
    time.sleep(5) # white 5 sec for full loading page

    keyboard.write(user, delay=0.25, restore_state_after=True) # write ibsher user name
    time.sleep(3) # white 3 sec for full user name write

    keyboard.press_and_release('tab') # jump to password box by tab button
    time.sleep(5)
    pyautogui.write(password, interval=0.25) # write password

def taqt():
    url = r"C:\Users\BeRLiN\Desktop\Automation Project\geckodriver.exe"  # geckodriver Path

    driver = webdriver.Firefox(executable_path=url)

    driver.get('https://www.taqat.sa/')  # url get
    clickTaqat = driver.find_element_by_xpath(
        "/html/body/header/div/div/div[2]/div[3]/div/div[3]/ul/li[4]/div/a/span[2]"
    )  # address button by xPath
    clickTaqat.click()  # click button

    userName = driver.find_elements_by_class_name("c-input")  # address to user name by class name
    time.sleep(5)  # white 5 sec for full loading page

    keyboard.write(user, delay=0.25, restore_state_after=True)  # write taqat user name
    time.sleep(3)  # white 3 sec for full user name write

    keyboard.press_and_release('tab')  # jump to password box by tab button
    pyautogui.write(password, interval=0.25)  # write password




while(1):
    try:
        print("hello\nfor Jadara Enter number 1:\nfor Taqat Enter number 2:")
        method = int(input())
        if method == 1:
            jdara()
        elif method == 2:
            taqt()
        else:
            print("try aging")
    except:
        print('Enter Number')