import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("passingDriver")
class Test_Blogs:

    def test_pageURL(self):
        baseURL = "https://baseedu.in/blogs.php"
        self.driver.maximize_window()
        self.driver.get(baseURL)
        pageURL = self.driver.current_url
        print(pageURL)


        ttttttttrr
