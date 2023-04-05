# anime id는 자동
def create_anime_query(data_lists):
    queries = []
    for data_list in data_lists:
        query = f"""
        insert into anime(season_id, title, start_date, episodes, duration, main_img, synopsis)
        values ({2}, '{data_list[0]}', '{data_list[1]}', '{data_list[2]}', '{data_list[3]}',
            '{data_list[4]}'
            , '{data_list[5]}');
        """
        queries.append(query)
    return queries
