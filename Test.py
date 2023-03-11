from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import sys
import time
from datetime import datetime
import util
from util import Screenshot
from util import word_cov

print("Start Time:" +datetime.today().strftime("%I:%M:%S %p,%d/%m/%Y"))
#df=pd.read_excel('amazon.xlsx',dtype=str)
dict=util.input_data(util.Db_Connection())
driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
url="https://automationtesting.co.uk"
driver.get(url)
Screenshot(driver,"loaded")

#Xpaths
First_Name=(By.XPATH,"//form[@id='contact_form']/input[@name='first_name']")
Last_Name=(By.XPATH,"//form[@id='contact_form']/input[@name='last_name']")
Email=(By.XPATH,"//form[@id='contact_form']/input[@name='email']")
Comment=(By.XPATH,"//form[@id='contact_form']/textarea[@name='message']")
Submit_button=(By.XPATH,"//div[@id='form_buttons']/input[@value='SUBMIT']")

contact_form_test=driver.find_element(by=By.XPATH,value="//nav[@id='menu']/ul//a[@href='contactForm.html']").click()
time.sleep(1)
for i in range (len(dict['SCENARIO'])):
    try:
        url="https://automationtesting.co.uk/contactForm.html"
        driver.get(url)
        Screenshot(driver,"login form")

        for _ in range(1):
            try:  
                F_Name=wait.until(EC.presence_of_element_located(First_Name))
                time.sleep(1)
                F_Name.click
                F_Name.send_keys(dict['F_NAME'][i])
                break
            except Exception:
                Screenshot(driver,"First name is missing")
                continue
            
        for _ in range(1):
            try:
                
                L_Name=wait.until(EC.presence_of_element_located(Last_Name))
                time.sleep(1)
                L_Name.click
                L_Name.send_keys(dict['L_NAME'][i])
                break
            except Exception:
                continue

        for _ in range(1):
            try:
                E_Name=wait.until(EC.presence_of_element_located(Email))
                time.sleep(1)
                E_Name.click
                E_Name.send_keys(dict['EMAIL'][i])
                break
            except Exception:
                Screenshot(driver,"email id is missing")
                continue

        for _ in range(1):
            try:
                C_Name=wait.until(EC.presence_of_element_located(Comment))
                time.sleep(1)
                C_Name.click
                C_Name.send_keys(dict['COMMENT'][i])
                Screenshot(driver,"All details filled")
                break
            except Exception:
                continue

        submit_button=wait.until(EC.element_to_be_clickable(Submit_button)).click()
        time.sleep(2)
        Screenshot(driver,"success")
        word_cov(dict['SCENARIO'][i])
        result=driver.title

        if str.__contains__(result,'Automation Testing - Homepage'):
            test="PASS"
            util.DB_Update(test,dict['SCENARIO'][i])
        if str.__contains__(result,'Contact form handler'):
            test="FAIL"
            util.DB_Update(test,dict['SCENARIO'][i])

    except Exception:
                continue

time.sleep(1)
print("Executed successfully")
print("End Time:" +datetime.today().strftime("%I:%M:%S %p,%d/%m/%Y"))
driver.close()
driver.quit()



"""
        df.to_excel('amazon.xlsx',index=False)
        df['Status'][i]="Passed"
        df.to_excel('amazon.xlsx',index=False)
        word_cov()  
"""
#/body[@innertext=' Error: Invalid email address']
#driver.find_element(by=By.XPATH,value="//div[@id='sidebar']/a[@href='#sidebar']")


#hamberger=driver.find_element(by=By.XPATH,value="").click()

#this is for drop down

#select = Select(driver.find_element(by=By.XPATH,value="/html//select[@id='cars']"))
#select.select_by_visible_text('Honda')
#source for drag and drop
#source = driver.find_element_by_link_text("Tutorialspoint")
#target
#target = driver.find_element_by_link_text("Selenium")
#action chain object
#action = ActionChains(driver)
# drag and drop operation
#action.drag_and_drop(source, target).perform()

#https://pythonspot.com/read-excel-with-pandas/

#//div[@id='main']/div[@class='inner']/div/div


