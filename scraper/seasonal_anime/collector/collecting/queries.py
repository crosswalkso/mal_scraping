table_name = ""


def read_all_query():
    return f"SELECT * FROM {table_name}"


# [
# ["'name1'", "'address1'", "'score1'"],
# ["'name2'", "'address2'", "'score2'"]
# ]
'''
def create_row_query(data_list):
    queries = []
    for data in data_list:
        values_strings = ", ".join(map(str, data))
        # ["'name1'", "'address1'", "'score1'"]
        # "" 지워짐
        # values_strings = "
        #                    'name1', 'address1', 'score1'
        #                  "
        query = f"""
            INSERT INTO {table_name}
            VALUES ({values_strings});
            """
        queries.append(query)
    return queries
'''


# 아래 create_... method에서 생성된 모든 query를 모아서 최종 반환
def collect_queries(table_lists):
    pass


###


def create_season_name(date_list):
    pass


def create_anime_query(data_lists):
    queries = []
    for data_list in data_lists:
        query = f"""
        insert into anime(season_id, title, start_date, episodes, duration, main_img, synopsis)
        values ({1}, '{data_list[0]}', '{data_list[1]}', '{data_list[2]}', '{data_list[3]}',
            '{data_list[4]}'
            , '{data_list[5]}');
        """
        queries.append(query)
    return queries


def create_genre_query(data_list):
    queries = []
    genre_dict = {}
    for idx, data in enumerate(data_list):
        genre_dict[data] = idx + 1
        query = f"""
        insert into genre(genre_name)
        values ('{data}');
        """
        queries.append(query)
    return [queries, genre_dict]


# 이름 바꾸기 _query
def create_anime_genres(anime_id, genre_id):
    query = f"""
    insert into anime_genres(anime_id, genre_id)
    values ({anime_id}, {genre_id});
    """
    return query


def create_studio_query(data_list):
    queries = []
    studio_dict = {}
    for idx, data in enumerate(data_list):
        studio_dict[data] = idx + 1
        query = f"""
        insert into studio(studio_name)
        values ('{data}');
        """
        queries.append(query)
    return [queries, studio_dict]


def create_anime_studios(anime_id, studio_id):
    query = f"""
    insert into anime_studios(anime_id, studio_id)
    values ({anime_id}, {studio_id});
    """
    return query


def create_source_query(data_list):
    queries = []
    source_dict = {}
    for idx, data in enumerate(data_list):
        source_dict[data] = idx + 1
        query = f"""
        insert into source(source_name)
        values ('{data}');
        """
        queries.append(query)
    return [queries, source_dict]


def create_anime_sources(anime_id, source_id):
    query = f"""
    insert into source_list(anime_id, source_id)
    values ({anime_id}, {source_id});
    """
    return query


def create_theme_query(data_list):
    queries = []
    theme_dict = {}
    for idx, data in enumerate(data_list):
        theme_dict[data] = idx + 1
        query = f"""
        insert into theme(theme_name)
        values ('{data}');
        """
        queries.append(query)
    return [queries, theme_dict]


def create_anime_themes(anime_id, theme_id):
    query = f"""
    insert into theme_list(anime_id, theme_id)
    values ({anime_id}, {theme_id});
    """
    return query


def create_demographic_query(data_list):
    queries = []
    demographic_dict = {}
    for idx, data in enumerate(data_list):
        demographic_dict[data] = idx + 1
        query = f"""
        insert into demo(demo_name)
        values ('{data}');
        """
        queries.append(query)
    return [queries, demographic_dict]


def create_anime_demographics(anime_id, demo_id):
    query = f"""
    insert into demo_list(anime_id, demo_id)
    values ({anime_id}, {demo_id});
    """
    return query


def create_broadcast_query(data_list):
    queries = []
    broadcast_dict = {}
    for idx, data in enumerate(data_list):
        broadcast_dict[data] = idx + 1
        query = f"""
        insert into broadcast(broadcast_name)
        values ('{data}');
        """
        queries.append(query)
    return [queries, broadcast_dict]


def create_anime_broadcasts(anime_id, broadcast_id):
    query = f"""
    insert into broadcast_list(anime_id, broadcast_id)
    values ({anime_id}, {broadcast_id});
    """
    return query
