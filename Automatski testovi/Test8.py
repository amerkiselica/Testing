#unos samo obaveznih polja u kreiranja admin profila
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')



driver.get("https://www.puppies-closet.com/evidencija/login.php")


driver.implicitly_wait(4)
username=driver.find_element_by_name("username")
password=driver.find_element_by_name("password")
username.send_keys("amerkiselica")
password.send_keys("amerkiselica123")

prijava=driver.find_element_by_class_name("loginbutton")
prijava.click()

name=driver.find_element_by_name("firstname")
name.send_keys("Amerika")

prezime=driver.find_element_by_name("lastname")
prezime.send_keys("Kis")


office_ddmenu= Select(driver.find_element_by_name("office_id"))
office_ddmenu.select_by_index(1)

org_unit_ddmenu= Select(driver.find_element_by_name("organization_id"))
org_unit_ddmenu.select_by_index(2)

save=driver.find_element_by_name("save")
save.click()