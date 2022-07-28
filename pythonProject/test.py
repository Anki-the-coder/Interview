from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
driver.execute_script("""window.open("http://bings.com","_blank");""")
driver.execute_script("window.open('');")
curent_handle = driver.current_window_handle
print(type(curent_handle))
print(curent_handle)
c = driver.window_handles
print(type(c))
for d in c :
    print(d)
    driver.switch_to.window(d)

print(driver.current_window_handle)

name =driver.find_element_by_id("name")
name.is