import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("passingDriver")
class Test_Careers:

    def test_pageURL(self):
        baseURL = "https://baseedu.in/careers.php"
        self.driver.maximize_window()
        self.driver.get(baseURL)
        pageURL = self.driver.current_url
        print(pageURL)

    def test_currentOpenings(self):
        self.driver.find_element(By.ID, "crntopen").click()

    def test_clickBlogs(self):
        self.driver.find_element(By.LINK_TEXT, 'Blogs').click()

