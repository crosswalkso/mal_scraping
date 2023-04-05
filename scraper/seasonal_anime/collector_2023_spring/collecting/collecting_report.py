# text 수집 후 list 를 쿼리로 변환 후 쿼리문의 배열 반환

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from .collecting_functions import *
from .queries import *


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

    # anime + detail 수집
    def get_all_attributes(self, driver):
        # anime table
        anime_table_lists = []
        # detail set
        # detail_set.add('detail_name')
        genre_set = set()
        studio_set = set()
        source_set = set()
        theme_set = set()
        demographic_set = set()
        # detail dict
        # detail_dict['main_img'] = 'detail_name'
        genre_dict = {}
        studio_dict = {}
        theme_dict = {}
        source_dict = {}  # 1 to 1
        demographic_dict = {}  # 1 to 1
        # detail_dicts
        # {
        # 'genre' : {'id1':['Comedy', 'Fantasy'], 'id2': [...]}
        # 'source' : { ... }
        # }
        detail_dicts_by_anime = {}

        # 모든 attribute 수집
        length = len(self.anime_boxes)
        for idx, anime_box in enumerate(self.anime_boxes):  # len(idx) - anime 개수
            if int(idx + 1 / length) == 1:
                print(f"100% ...")
            else:
                print(f"{round((idx+1)/length, 4)*100}% 진행중...")
            anime_table_temp = []
            # anime_tables
            anime_table_temp.append(collect_titles(anime_box, idx))
            anime_table_temp.append(collect_start_dates(anime_box, idx))
            anime_table_temp.append(collect_episodes(anime_box, idx))
            anime_table_temp.append(collect_durations(anime_box, idx))
            main_img = collect_images(anime_box, idx, driver)
            anime_table_temp.append(main_img)
            anime_table_temp.append(collect_synopses(anime_box, idx))
            anime_table_lists.append(anime_table_temp)
            # genre, studio, theme, source, demo
            genres = collect_genres(anime_box, idx)
            if genres:
                for genre in genres:
                    g = genre.get_attribute("innerText")
                    genre_set.add(g)
                    if not genre_dict.get(main_img):
                        genre_dict[main_img] = [g]
                    else:
                        genre_dict[main_img].append(g)
            # studio - x
            studios = collect_studios(anime_box, idx)
            if studios:
                for studio in studios:
                    temp = studio.get_attribute("innerText")
                    temp_s = temp.split("'")
                    result = ""
                    for s in temp_s:
                        result += s + "''"
                    studio_set.add(result[:-2])
                    if not studio_dict.get(main_img):
                        studio_dict[main_img] = [result[:-2]]
                    else:
                        studio_dict[main_img].append(result[:-2])

            # theme
            themes = collect_themes(anime_box, idx)
            if themes:
                for theme in themes:
                    t = theme.get_attribute("innerText")
                    theme_set.add(t)
                    if not theme_dict.get(main_img):
                        theme_dict[main_img] = [t]
                    else:
                        theme_dict[main_img].append(t)

            # source - x
            source = collect_source(anime_box, idx)
            if source:
                source_set.add(source)
                if not source_dict.get(main_img):
                    source_dict[main_img] = [source]
                else:
                    source_dict[main_img].append(source)

            # demographic
            demographics = collect_demographics(anime_box, idx)
            for demographic in demographics:
                d = demographic.get_attribute("innerText")
                demographic_set.add(d)
                if not demographic_dict.get(main_img):
                    demographic_dict[main_img] = [d]
                else:
                    demographic_dict[main_img].append(d)

        # create queries
        anime_table_queries = create_anime_query(anime_table_lists)
        spring_detail_info_sets = [
            genre_set,
            studio_set,
            theme_set,
            source_set,
            demographic_set,
        ]
        detail_dicts_by_anime["genre_dict"] = genre_dict
        detail_dicts_by_anime["studio_dict"] = studio_dict
        detail_dicts_by_anime["theme_dict"] = theme_dict
        detail_dicts_by_anime["source_dict"] = source_dict
        detail_dicts_by_anime["demographic_dict"] = demographic_dict
        return (
            anime_table_queries,
            spring_detail_info_sets,
            detail_dicts_by_anime,
        )
