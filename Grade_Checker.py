from selenium import webdriver
from selenium.webdriver import Keys
import time
from playsound import playsound
from selenium.webdriver.common.by import By
import Credentials


WEB_PATH = r"https://gezer1.bgu.ac.il/meser/login.php"
CELL_PATH = "/html/body/form[2]/table/tbody/tr[2]/td[6]/input"
USERNAME_ID = "username"
PASS_ID = "pass"
ID = "id"
AGREE = "agree"

driver = webdriver.Edge(Credentials.PATH) # Accessing the webdriver of Edge browser
driver.get(WEB_PATH) # Entering the web page

username = driver.find_element(By.ID, USERNAME_ID) # Finding the username element in the web page
username.send_keys(Credentials.USERNAME) # Entering the username credentials to the text field
time.sleep(1) # Waiting one second no to be suspicious

password = driver.find_element(By.ID, PASS_ID) # Finding the password element in the web page
password.send_keys(Credentials.PASSWORD) # Entering the password credentials to the text field
time.sleep(1) # Waiting one second no to be suspicious

mId = driver.find_element(By.ID, ID) # Finding the id element in the web page
mId.send_keys(Credentials.MY_ID) # Entering the id credentials to the text field
time.sleep(1) # Waiting one second no to be suspicious

mId.send_keys(Keys.RETURN) # Pressing enter after filling the form
time.sleep(3) # Waiting 3 seconds for the page to load and not to be suspicious

agree_button = driver.find_element(By.NAME, AGREE) # Finding the agree element in the web page
agree_button.send_keys(Keys.RETURN) # Pressing enter on the element
time.sleep(5) # Waiting 5 seconds for the page to load. And no to be suspicious.

TABLE_PATH = "/html/body/form[1]/table/tbody"
#/html/body/form[1]/table/tbody/tr[2]/td[4]
#/html/body/form[1]/table/tbody/tr[4]/td[4]
## if /html/body/form[1]/table/tbody/tr[2]/ has "מועד א" check /html/body/form[1]/table/tbody/tr[2]/td[4] 
# if isn't "אין" add to json file (if not exist - check name of course). if json file is bigger ring the bell. 
table = driver.find_elements(By.XPATH, TABLE_PATH)
rows = table[0].find_elements(By.TAG_NAME, "tr")
for row in rows:
    col = row.find_elements(By.TAG_NAME, "td")
    print (col.text)
time.sleep(4)
driver.quit()
# for i in (range(len(table))):
#     path = ("/html/body/form[1]/table/tbody/tr[2]/td[%d]" %(i+1))
#     print(driver.find_element(By.XPATH, path).text)

# try:
#     output = driver.find_element(By.XPATH, CELL_PATH) # Trying to find the input element in the table.
#     playsound(Credentials.PATH_TO_SOUND) # If the input element is there, there is a grade update and a sound will play.
#     playsound(Credentials.PATH_TO_SOUND)
# except:
#     driver.quit() # If there isn't an input element, there will be an error and the software will quit.



