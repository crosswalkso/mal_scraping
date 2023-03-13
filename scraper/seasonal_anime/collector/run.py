# method 동작
# title, genres ..
from collecting.collecting import Collecting
from collecting.execute_queries import insert_queries

with Collecting(teardown=True) as bot:
    bot.open_page()
    queries = bot.report_results()
    insert_queries(queries[0])  # anime_table
    insert_queries(queries[1])  # genre_table
    insert_queries(queries[2])  # anime_genres_table
    insert_queries(queries[3])  # studio_table
    insert_queries(queries[4])  # anime_studios_table
    insert_queries(queries[5])  # source_table
    insert_queries(queries[6])  # source_list_table
    insert_queries(queries[7])  # theme_table
    insert_queries(queries[8])  # theme_list_table
    insert_queries(queries[9])  # queries_demographic
    insert_queries(queries[10])  # queries_anime_demographics
    insert_queries(queries[11])  # queries_broadcast
    insert_queries(queries[12])  # queries_anime_broadcasts
