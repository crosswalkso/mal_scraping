# method 동작
# title, genres ..
from collecting.collecting import Collecting

with Collecting(teardown=True) as bot:
    bot.open_page()
    bot.report_results()
