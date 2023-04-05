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
        self.implicitly_wait(10)
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
        # data 수집: (1) anime_info:query (2) detail_info (3) new_season_detail_info_set
        # (4) [genre, studio, ...]detail_dict = {main_img:detail_name, ... , ...}
        (
            anime_table_queries,
            spring_detail_info_sets,
            detail_dicts_by_anime,
        ) = report.get_all_attributes(
            driver=self
        )  # collect_images <- driver
        # anime + detail table query
        # (1) update anime_table (2) update detail_dict and update detail_info

        # anime_id, detail_id query
        # (1) DB에서 {main_img:anime_id, ...} 뽑고
        # (2) main_img -> detail_name -> detail_id로 추적
        # (3) (anime_id, detail_id) query 생성
        return (
            anime_table_queries,
            spring_detail_info_sets,
            detail_dicts_by_anime,
        )
