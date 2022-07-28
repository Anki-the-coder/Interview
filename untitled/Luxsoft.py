# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.amazon.in/ref=nav_logo")
# driver.maximize_window()
# links = driver.find_elements_by_xpath("//*[@href]")
# link = links[2]
# link.click()
#
# driver.switch_to.window(newWindow)
# ele = driver.find_element_by_xpath("elemennt on web page")
# assert ele.text == "text to be asseserted"
# driver.close()
# driver.switch_to.


class Car:

    def __init__(self, color):
        self.color = color

    def make_noise(self):
        print("brrrr'/'vrrr-u")
        print(self.color)


class DaciaCar(Car):

    def make_noise(self):
        print("DaciaCar' noise")
        print(self.color)


c = Car("Red")
c.make_noise()

d = DaciaCar("Blue")
d.make_noise()
