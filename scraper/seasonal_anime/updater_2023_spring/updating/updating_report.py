# text 수집 후 list 를 쿼리로 변환 후 쿼리문의 배열 반환

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from .updating_functions import *
from .queries import *
from .execute_queries import get_title_ids


class UpdatingReport:
    def __init__(self, anime_boxes_element: WebElement):
        self.anime_boxes_element = anime_boxes_element  # 큰 박스
        self.anime_boxes = self.get_each_box()

    # 큰 박스에서 작은 박스 검색
    def get_each_box(self):
        return self.anime_boxes_element.find_elements(
            By.XPATH,
            "//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))]",
        )

    def get_all_attributes(self, driver):
        scores = []
        members = []
        anime_ids = []
        titles = []

        for idx, anime_box in enumerate(self.anime_boxes):  # len(idx) - anime 개수
            scores.append(collect_scores(anime_box, idx))
            members.append(collect_members(anime_box, idx))
            titles.append(collect_titles(anime_box, idx))
        # create queries
        db_title_dict = get_title_ids()
        for title in titles:
            anime_ids.append(db_title_dict[title])
        score_queries = create_score_hist_query(anime_ids, scores)
        member_queries = create_member_hist_query(anime_ids, members)
        return score_queries, member_queries
