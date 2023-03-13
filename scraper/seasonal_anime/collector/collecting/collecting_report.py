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

    # 홈페이지에서 수집한 값들을 str형태로 반환함
    # studio, genre, source, theme, demographic, broadcast
    def get_all_attributes(self, driver):
        # anime table
        anime_table_lists = []
        # genre, studio, source, theme, demo, broad set
        genre_set = set()
        anime_id_and_genres = []  # (1, ['Action', 'Adventure', 'Drama'])의 리스트
        studio_set = set()
        anime_id_and_studios = []
        source_set = set()
        anime_id_and_sources = []
        theme_set = set()
        anime_id_and_themes = []
        demographic_set = set()
        anime_id_and_demographics = []
        broadcast_set = set()
        anime_id_and_broadcasts = []
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
            anime_table_temp.append(collect_images(anime_box, idx, driver))
            anime_table_temp.append(collect_synopses(anime_box, idx))
            anime_table_lists.append(anime_table_temp)
            # genre, studio, source, theme, demo, broad
            # genre
            genres = collect_genres(anime_box, idx, genre_set)
            anime_genres = []  # anime_id의 장르들
            for genre in genres:
                g = genre.get_attribute("innerText")
                genre_set.add(g)  # x
                anime_genres.append(g)  #
            anime_id_and_genres.append((idx + 1, anime_genres))
            # studio
            studios = collect_studios(anime_box, idx, studio_set)
            anime_studios = []
            for studio in studios:
                temp = studio.get_attribute("innerText")
                temp_s = temp.split("'")
                result = ""
                for s in temp_s:
                    result += s + "''"
                # anime_id_and_studios.append((idx + 1, result[:-2]))
                studio_set.add(result[:-2])
                anime_studios.append(result[:-2])
            anime_id_and_studios.append((idx + 1, anime_studios))
            # source
            sources = collect_sources(anime_box, idx, source_set)
            anime_sources = []
            for source in sources:
                s = source.get_attribute("innerText")
                source_set.add(s)
                anime_sources.append(s)
            anime_id_and_sources.append((idx + 1, anime_sources))
            # theme
            themes = collect_themes(anime_box, idx, theme_set)
            anime_themes = []
            for theme in themes:
                t = theme.get_attribute("innerText")
                theme_set.add(t)
                anime_themes.append(t)
            anime_id_and_themes.append((idx + 1, anime_themes))
            # demographic
            demographics = collect_demographics(anime_box, idx)
            anime_demographics = []
            for demographic in demographics:
                if demographic == "Unknown":
                    anime_demographics = ["Unknown"]
                    break
                d = demographic.get_attribute("innerText")
                demographic_set.add(d)
                anime_demographics.append(d)
            anime_id_and_demographics.append((idx + 1, anime_demographics))
            # broadcast
            broadcasts = collect_broadcasts(anime_box, idx, broadcast_set)
            anime_broadcasts = []
            for broadcast in broadcasts:
                b = broadcast.get_attribute("class")
                bb = b.split()[1]
                if bb == "malicon-streaming":
                    broadcast_set.add("MAL")
                    anime_broadcasts.append("MAL")
                elif bb == "spicon-crunchyroll":
                    broadcast_set.add("crunchyroll")
                    anime_broadcasts.append("crunchyroll")
                elif bb == "spicon-disneyplus":
                    broadcast_set.add("disney+")
                    anime_broadcasts.append("disney+")
                else:
                    continue
            anime_id_and_broadcasts.append((idx + 1, anime_broadcasts))
        # create queries
        queries_anime = create_anime_query(anime_table_lists)
        queries_genre, genre_dict = create_genre_query(list(genre_set))
        queries_studio, studio_dict = create_studio_query(list(studio_set))
        queries_source, source_dict = create_source_query(list(source_set))
        queries_theme, theme_dict = create_theme_query(list(theme_set))
        queries_demographic, demographic_dict = create_demographic_query(
            list(demographic_set)
        )
        queries_broadcast, broadcast_dict = create_broadcast_query(list(broadcast_set))
        # anime_id and genre key 묶기
        queries_anime_genres = []
        for anime_id_and_genre in anime_id_and_genres:
            # anime_id_and_genre = [1, [g1, g2, g3..]]
            anime_id = anime_id_and_genre[0]
            genre_names = anime_id_and_genre[1]
            for genre_name in genre_names:
                queries_anime_genres.append(
                    create_anime_genres(anime_id, genre_dict[genre_name])
                )
        queries_anime_studios = []
        for anime_id_and_studio in anime_id_and_studios:
            anime_id = anime_id_and_studio[0]
            studio_names = anime_id_and_studio[1]
            for studio_name in studio_names:
                queries_anime_studios.append(
                    create_anime_studios(anime_id, studio_dict[studio_name])
                )
        queries_anime_sources = []
        for anime_id_and_source in anime_id_and_sources:
            anime_id = anime_id_and_source[0]
            source_names = anime_id_and_source[1]
            for source_name in source_names:
                queries_anime_sources.append(
                    create_anime_sources(anime_id, source_dict[source_name])
                )
        queries_anime_themes = []
        for anime_id_and_theme in anime_id_and_themes:
            anime_id = anime_id_and_theme[0]
            theme_names = anime_id_and_theme[1]
            for theme_name in theme_names:
                queries_anime_themes.append(
                    create_anime_themes(anime_id, theme_dict[theme_name])
                )
        queries_anime_demographics = []
        for anime_id_and_demographic in anime_id_and_demographics:
            anime_id = anime_id_and_demographic[0]
            demographic_names = anime_id_and_demographic[1]
            for demographic_name in demographic_names:
                queries_anime_demographics.append(
                    create_anime_demographics(
                        anime_id, demographic_dict[demographic_name]
                    )
                )
        queries_anime_broadcasts = []
        for anime_id_and_broadcast in anime_id_and_broadcasts:
            anime_id = anime_id_and_broadcast[0]
            broadcast_names = anime_id_and_broadcast[1]
            for broadcast_name in broadcast_names:
                queries_anime_broadcasts.append(
                    create_anime_broadcasts(anime_id, broadcast_dict[broadcast_name])
                )
        return (
            queries_anime,
            queries_genre,
            queries_anime_genres,
            queries_studio,
            queries_anime_studios,
            queries_source,
            queries_anime_sources,
            queries_theme,
            queries_anime_themes,
            queries_demographic,
            queries_anime_demographics,
            queries_broadcast,
            queries_anime_broadcasts,
        )  # genre 테이블, anime_genre 테이블
