import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Firefox()
# options = ChromeOptions()
# options.add_experimental_option( 'excludeSwitches', ['disable-hang-monitor', 'disable-prompt-on-repost', 'disable-background-networking', 'disable-sync', 'disable-translate', 'disable-web-resources', 'disable-client-side-phishing-detection', 'disable-component-update', 'disable-default-apps', 'disable-zero-browsers-open-for-tests', '--enable-automation', '--use-mock-keychain', '--user-data-dir', '--enable-blink-features', '--disable-popup-blocking', '--enable-logging --force-fieldtrials=SiteIsolationExtensions/Control', '--enable-logging', '--force-fieldtrials', '--ignore-certificate-errors', '--load-extension', '--log-level', '--no-first-run','--password-store','--remote-debugging-port','--test-type'
# ])
# options.add_argument("--headless")
# options.addArguments("disable-blink-features=AutomationControlled");
# options.setExperimentalOption("excludeSwitches", Collections.singletonList("enable-automation"));
# options.setExperimentalOption("useAutomationExtension", false);
# baseurl = "https://www.cleartrip.com"
# driver.get(baseurl)
driver.get("https://www.cleartrip.com/")
time.sleep(5)
driver.maximize_window()
driver.implicitly_wait(3)

_from = "//div[@class='col flex flex-middle']/div[1]//div[@class='p-relative']/input[1]"
_to = "//div[@class='col flex flex-middle']/div[5]//div[@class='p-relative']/input[1]"
_mumbai = "//div[@class='bg-white br-4 elevation-5 p-1 p-absolute mt-1 z-50 l-0']//p"
_delhi = "//input[@value='DEL - New Delhi, IN']"
_departDate = "//button[@xpath='1']"
_date = "//div[@aria-label='Fri May 13 2022']"
_infants = "//select[@xpath='1']"
_search = "//button[@xpath='1']"

driver.find_element_by_xpath(_from).click()
driver.find_element_by_xpath(_from).send_keys("Mum")
time.sleep(5)
driver.find_element_by_xpath(_mumbai).click()
time.sleep(3)

driver.find_element_by_xpath(_to).click()
driver.find_element_by_xpath(_to).send_keys("Del")
time.sleep(5)
# driver.find_element_by_xpath(_delhi).click()
driver.find_element_by_xpath(_mumbai).click()
time.sleep(3)

driver.find_element_by_xpath(_departDate).click()
driver.find_element_by_xpath(_date).click()

driver.find_element_by_xpath(_infants).click()
driver.find_element_by_xpath(_search).click()

driver.close()
