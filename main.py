import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException as NSEE
from Test_Data.testData import data
from pageObjetcts.PageObjects import pageObjects

user_name = data().username
pass_word = data().password
Firstname = data().firstname
Middlename = data().middlename
Lastname = data().lastname
main_username = data().Main_username
User_password = data().user_password

Username = pageObjects().UserName
Password = pageObjects().PassWord
LoginButton = pageObjects().Login_button
addButton = pageObjects().add_button
first_name = pageObjects().firstname
middle_name = pageObjects().middlename
last_name = pageObjects().lastname
save_button = pageObjects().save_button
admin_tab = pageObjects().Admin_tab
admin_add_button = pageObjects().Admin_Add_button
userrole_select = pageObjects().Userrole_Select
userrole_admin = pageObjects().Userrole_admin
Main_username = pageObjects().Main_username
employee_name = pageObjects().Employee_name
main_status = pageObjects().Main_status
admin_password = pageObjects().Admin_Password
admin_confirm_password = pageObjects().Admin_Confirm_Password
# admin_save_button = pageObjects().Admin_save_button
Username_dropdown = pageObjects().username_dropdown
Status_enabled = pageObjects().status_enabled
Add_user_save_button = pageObjects().add_user_save_button
Admin_search_username = pageObjects().admin_search_username
Admin_search_button = pageObjects().admin_search_button
Username_from_table = pageObjects().username_from_table
Main_user_dropdown = pageObjects().main_user_dropdown
Logout = pageObjects().logout

# service = Service(executable_path=GeckoDriverManager().install())
# driver = webdriver.Firefox(service=service)
driver = webdriver.Chrome()

# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

url = pageObjects.url1


def launch(url):
    # getting input from the Login data file
    # launch url
    try:
        driver.get(url)
        time.sleep(6)
        driver.maximize_window()
        print("URL is launched Successfully")

    except NSEE:
        print("Error in launching URL")
        driver.quit()


def invalid_login():
    driver.find_element(by=By.XPATH, value=Username).send_keys(user_name)
    driver.find_element(by=By.XPATH, value=Password).send_keys("pass_word")
    # click on Login
    driver.find_element(by=By.XPATH, value=LoginButton).click()
    print("Invalid Login Scenario")
    invalid_text = driver.find_element(by=By.XPATH, value="//p[text()='Invalid credentials']").text
    print(invalid_text)
    text = "Invalid credentials"
    if invalid_text == text:
        print("Validation is thrown")
        driver.quit()
    else:
        print("Issue in displaying validation")
        driver.save_screenshot()
        driver.quit()


def login():
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value=Username).send_keys(user_name)
    driver.find_element(by=By.XPATH, value=Password).send_keys(pass_word)
    # click on Login
    driver.find_element(by=By.XPATH, value=LoginButton).click()
    print("Login Successful")


def PIM_click_add_button():
    # navigate to PIM page
    driver.implicitly_wait(10)
    try:
        driver.find_element(by=By.XPATH, value="//a[@href='/web/index.php/pim/viewPimModule']").click()
        # clicking the Add button
        driver.find_element(by=By.XPATH, value=addButton).click()
        print("Add Employee page opened")
    except NSEE:
        print("Error in Clicking Add button")


def PIM_Add_Employee():
    # Provide inputs to create employee
    # input details
    driver.find_element(by=By.XPATH, value=first_name).send_keys(Firstname)
    driver.find_element(by=By.XPATH, value=middle_name).send_keys(Middlename)
    driver.find_element(by=By.XPATH, value=last_name).send_keys(Lastname)
    driver.implicitly_wait(5)
    # image upload
    driver.find_element(by=By.XPATH, value="//input[@class='oxd-file-input'][@type='file']").send_keys(
        "C:\\Users\\Surya\\Downloads\\7.jpg")
    # click on save button
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=save_button).click()
    driver.implicitly_wait(2)
    time.sleep(1)
    save_tag = driver.find_element(by=By.XPATH,
                                   value="//div[@class='oxd-toast-content oxd-toast-content--success']").text
    print("Toast message is displayed", save_tag)
    # self.driver.save_screenshot("add employee success")
    print("Add Employee Successful")
    time.sleep(6)
    # add further details
    # license number
    driver.find_element(by=By.XPATH,
                        value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys(
        "license")
    # license expiry date
    driver.find_element(by=By.XPATH, value="//form/div[2]/div[2]/div[2]/div/div[2]/div/div/input").send_keys(
        "2023/09/11")
    # Nationality
    driver.find_element(by=By.XPATH, value="//form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]").click()
    driver.find_element(by=By.XPATH, value="//form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[83]/span").click()
    # marital Status
    driver.find_element(by=By.XPATH,
                        value="// form / div[3] / div[1] / div[2] / div / div[2] / div / div / div[1]").click()
    driver.find_element(by=By.XPATH, value="//form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]").click()
    # DOB
    driver.find_element(by=By.XPATH, value="//form/div[3]/div[2]/div[1]/div/div[2]/div/div/input").send_keys(
        "1997/11/16")
    # Gender=male
    driver.find_element(by=By.XPATH, value="//input[@type='radio'][@value='1']").click()
    # save button
    driver.find_element(by=By.XPATH, value="//form/div[5]/button").click()


def search_user_PIM():
    driver.find_element(by=By.XPATH, value="//form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys(Firstname)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="//form/div[1]/div/div[1]/div/div[2]/div/div[2]/div").click()
    driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()


def edit_user_PIM():
    driver.find_element(by=By.XPATH, value="//i[@class='oxd-icon bi-pencil-fill']").click()
    # edit page opens
    # as of now, just editing one field, Nick name
    driver.find_element(by=By.XPATH, value="//form/div[1]/div[2]/div/div/div[2]/input").send_keys("dattebayo")
    # save button
    driver.find_element(by=By.XPATH, value="//form/div[5]/button").click()
    time.sleep(1)
    # capturing toast message
    save_tag = driver.find_element(by=By.XPATH, value='//*[@id="oxd-toaster_1"]/div/div[1]/div[2]').text
    print("Toast message is displayed as below:", save_tag)


def delete_user_PIM():
    # deleting User by clicking delete icon
    driver.find_element(by=By.XPATH, value="//i[@class='oxd-icon bi-trash']").click()
    # clicking the Yes button in the Pop up delete window
    driver.find_element(by=By.XPATH, value="//button[text()=' Yes, Delete ']").click()
    # toast message
    save_tag = driver.find_element(by=By.XPATH, value='//*[@id="oxd-toaster_1"]/div/div[1]/div[2]').text
    print("Toast message displayed is", save_tag)


launch(url)
# invalid_login()
login()
#PIM_click_add_button()
#PIM_Add_Employee()
search_user_PIM()
edit_user_PIM()
#delete_user_PIM()
