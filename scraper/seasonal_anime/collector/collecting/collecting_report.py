# text 수집 후 list 를 쿼리로 변환 후 쿼리문의 배열 반환

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from .collecting_functions import *


class CollectingReport:
    def __init__(self, anime_boxes_element: WebElement):
        self.anime_boxes_element = anime_boxes_element  # 큰 박스
        self.anime_boxes = self.get_each_box()

    # 큰 박스에서 작은 박스 검색
    def get_each_box(self):
        return self.anime_boxes_element.find_elements(
            By.XPATH,
            "//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))]",
        )

    # 홈페이지에서 수집한 값들을 str형태로 반환함
    # studio, genre, source, theme, demographic, broadcast
    def get_all_attributes(self, driver):
        titles = []
        start_dates = []
        episodes = []
        durations = []
        images = []
        synopses = []
        # 모든 attribute 수집
        for idx, anime_box in enumerate(self.anime_boxes):
            # anime_tables
            titles.append(collect_titles(anime_box, idx))
            start_dates.append(collect_start_dates(anime_box, idx))
            episodes.append(collect_episodes(anime_box, idx))
            durations.append(collect_durations(anime_box, idx))
            images.append(collect_images(anime_box, idx, driver))
            synopses.append(collect_synopses(anime_box, idx))
            # genre, studio, source, theme, demo, broad
            # ... 추가예정
        anime_table_list = (
            titles + start_dates + episodes + durations + images + synopses
        )
        return anime_table_list
