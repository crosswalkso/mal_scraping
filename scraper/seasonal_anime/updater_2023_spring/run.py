# method 동작
# update scores, members ...

from updating.updating import Updating
from updating.execute_queries import insert_queries

with Updating(teardown=True) as bot:
    bot.open_page()
    queries = bot.report_results()
    insert_queries(queries[0])
    insert_queries(queries[1])
