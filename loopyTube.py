from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Welcome - Loopy Tube @danhpaiva #


def clear():
    try:
        import os
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 130
    print("\n" * lines)


def AcessGoogle(driver):
    driver.get('https://www.google.com')
    time.sleep(3)


def GoToSearch(driver):
    inputButon = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    inputButon.send_keys("Daniel Paiva Descomplica" + Keys.ENTER)

    time.sleep(3)

    inputClick = driver.find_element(
        By.XPATH, "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/video-voyager/div/div/a/div/div[2]/div[1]/div/span")
    inputClick.click()


# Let's Code #
pathSystem = '.\edgedriver_win64\msedgedriver.exe'
while (True):
    driver = webdriver.Edge(pathSystem)
    time.sleep(3)
    AcessGoogle(driver)
    GoToSearch(driver)
    time.sleep(31)
    driver.close()
    time.sleep(3)
    clear()
