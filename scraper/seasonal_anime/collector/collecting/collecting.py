from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from .constants import BASE_URL
from time import sleep
from .collecting_report import CollectingReport

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class Collecting(webdriver.Chrome):
    def __init__(self, teardown=False):
        super().__init__(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options,
        )
        self.teardown = teardown
        self.implicitly_wait(5)
        self.maximize_window()

    def open_page(self):
        self.get(BASE_URL)

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            sleep(3)
            print("브라우저를 닫습니다.")
            self.quit()

    # collecting
    # seasonal_anime 중 new 박스만 가져옴
    # collecting_report로 전달
    def report_results(self):
        new_anime_boxes = self.find_element(
            By.XPATH,
            "//div[contains(@class, 'seasonal-anime-list')][1]",
        )
        report = CollectingReport(new_anime_boxes)
        queries = report.get_all_attributes(driver=self)  # collect_images <- driver
        return queries
