from collecting.collecting import Collecting
from collecting.execute_queries import insert_queries
from collecting.update_table import UpdateTables

anime_queries = []
detail_info_sets = []  # genre, studio, theme, source, demo
detail_names = [
    "genre",
    "studio",
    "theme",
    "source",
    "demo",
]
## (anime_id, detail_id)
updated_detail_table_info_dicts = []  # genre, studio, theme, source, demo
detail_dicts = {}  # {'genre_dict': {img1:['g1', 'g2', ...]}}

with Collecting(teardown=True) as bot:
    bot.open_page()
    results = bot.report_results()
    anime_queries = results[0]  # anime_table
    detail_info_sets = results[1]
    detail_dicts = results[2]


with UpdateTables() as tab:
    # anime table에 데이터 추가

    insert_queries(anime_queries)
    # detail 수집
    # Colletor에서 수집한 detail set 중복 제거
    for idx, detail_info_set in enumerate(detail_info_sets):
        new_detail_dict, updated_detail_dict = tab.get_new_detail(
            tab.detail_table_dicts[idx], detail_info_set
        )
        updated_detail_table_info_dicts.append(updated_detail_dict)
        tab.insert_detail_table(detail_names[idx], new_detail_dict)
    # new_detail_dict {'Mystery': 13, 'Gourmet': 14}

    # insert anime_id, detail_id
    # updated_detail_info_dicts = []
    tab.connect_anime_and_detail_id(detail_dicts, updated_detail_table_info_dicts)
