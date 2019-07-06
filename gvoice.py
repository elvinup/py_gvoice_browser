from time import sleep
from selenium import webdriver
import os
from libs.selenium_config import seleniumOptions

def login(driver, gmail, password):
    driver.get("https://voice.google.com/signup")
    sleep(1)
    driver.find_element_by_xpath("//input[@type='email']").send_keys(gmail)
    driver.find_element_by_xpath("//span[contains(text(), 'Next')]").click()
    sleep(5)
    driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
    driver.find_element_by_xpath("//span[contains(text(), 'Next')]").click()

def send_text(driver, number, msg):
    driver.get("https://voice.google.com/u/0/messages")
    sleep(3)
    driver.find_element_by_xpath("//div[@ng-if='ctrl.showThreadListHeader()']").click()
    driver.find_element_by_xpath("//input[@type='search']").send_keys(number)

    #Select number
    driver.find_element_by_xpath("//gv-contact-list").click()
    sleep(3)

    #Write text
    driver.find_element_by_xpath("//textarea").send_keys(msg)
    
    #Push send
    driver.find_element_by_xpath("//button[@aria-label='Send message']").click()

def logout(driver):

    driver.find_element_by_xpath("//a[contains(@aria-label, 'Google Account')]").click()
    driver.find_element_by_xpath("//a[contains(text(), 'Sign out')]").click()

def send_text_cycle(gmail, password, number, msg, chromedriver_path):
    # Setup
    options = seleniumOptions()
    driver = webdriver.Chrome(options = options, executable_path=chromedriver_path)

    login(driver, gmail, password)
    sleep(5)

    send_text(driver, number, msg)
    sleep(5)    

    logout(driver)
    driver.close()

def main():
    send_text_cycle('your gmail username', 'your password', '# to text', 'message to send', 'chromedriver path')

if __name__ == "__main__":
    main()
