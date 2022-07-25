import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_experimental_option('prefs', {
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})

# Initialize the browser
browser = webdriver.Chrome(options=options)

# Import students
fileHandler = open('students.txt', 'r')
sStudents = fileHandler.read()
students = sStudents.split()

# Load this page
browser.get('http://sbteonline.in')
browser.implicitly_wait(100)

for student in students:
    try:
        rollTextField = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[5]/div/div/div/div/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/div/div/div[1]/input')
        rollTextField.clear()
        rollTextField.click()
        rollTextField.send_keys(student)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[5]/div/div/div/div/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/div/div/div[3]/div/span/span').click()
        browser.implicitly_wait(100)
        try:
            browser.switch_to.frame(browser.find_element(By.CSS_SELECTOR, 'div.v-window.v-widget.v-has-width.v-has-height>div>div>div.v-window-contents>div>div>div>div>iframe'))
            browser.find_element(By.XPATH, '/html/body/div/div/a/button').click()
            time.sleep(2)
            browser.switch_to.default_content()
            browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]').click()
        except:
            print('Result not found of ' + student)
    except:
        print('Error Occurred')

browser.quit()
