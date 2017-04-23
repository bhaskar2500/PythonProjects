from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url='http://ppm.prolifics.com'
userName="bhaskar.kaushal@prolifics.com"
password="Prolifics2017"
driver = webdriver.Chrome(r'C:\Users\Da Silva\Desktop\DigitRecognition\chromedriver.exe')
driver.get(url)
userNameCon = driver.find_element_by_id("userName")
userNameCon.send_keys(userName)
passwordCon=driver.find_element_by_id("password")
passwordCon.send_keys(password)
submit=driver.find_element_by_id("send")
submit.click()
click_icon = WebDriverWait(driver, 5, 0.25).until(EC.visibility_of_element_located([By.ID, 'SaveMyTS']))
driver.execute_script(""" 
$timeDiv=$('div.layoutWid-2')

$allTextTypes=$($timeDiv[5]).find("input[type=text]")

$($allTextTypes).each(function()
    {
    if($(this).prop('disabled', false) || $(this).val()==0)
        { 
            $(this).val(8); 
        }          
    })
""")

# saveTs=driver.find_element_by_id("SaveMyTS")
# saveTs.click()

