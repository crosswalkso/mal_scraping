from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


### anime table list
def collect_titles(anime_box: WebElement, idx):
    try:
        title = (
            anime_box.find_element(
                By.XPATH,
                f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//a[@class='link-title']",
            )
            .get_attribute("innerHTML")
            .strip()
        )
        title_s = title.split("'")
        result = ""
        for t in title_s:
            result += t + "''"
    except Exception as e:
        # "'Unknown'"
        title = "Unknown"
    # return f"'title'"
    return result[:-2]


def collect_start_dates(anime_box: WebElement, idx):
    try:
        start_date = (
            anime_box.find_element(
                By.XPATH,
                f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//div[@class='prodsrc']//span[@class='item'][1]",
            )
            .get_attribute("innerHTML")
            .strip()
        )
    except Exception as e:
        start_date = "Unknown"
    return start_date


def collect_episodes(anime_box, idx):
    try:
        episode = (
            anime_box.find_element(
                By.XPATH,
                f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//div[@class='info']//span[@class='item'][2]//span[1]",
            )
            .get_attribute("innerHTML")
            .strip()
        )
    except Exception as e:
        episode = "Unknown"
    return episode


def collect_durations(anime_box, idx):
    try:
        duration = (
            anime_box.find_element(
                By.XPATH,
                f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//div[@class='info']//span[@class='item'][2]//span[2]",
            )
            .get_attribute("innerHTML")
            .strip()
        )
    except Exception as e:
        duration = "Unknown"
    return duration


# scroll down
def collect_images(anime_box, idx, driver):
    try:
        image = (
            anime_box.find_element(
                By.XPATH,
                f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//img[@src]",
            )
            .get_attribute("src")
            .strip()
        )
        # image loading error
        driver.execute_script(f"window.scrollTo({idx*500}, {(idx+1)*500})")
    except Exception as e:
        image = "Unknown"
    return image


def collect_synopses(anime_box, idx):
    try:
        synopsis = (
            anime_box.find_element(
                By.XPATH,
                f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//p[@class='preline']",
            )
            .get_attribute("innerHTML")
            .strip()
        )
        synopsis_s = synopsis.split("'")
        result = ""
        for synopsis in synopsis_s:
            result += synopsis + "''"
    except Exception as e:
        result = "Unknown  "
    return result[:-2]


### genre table list
def collect_genres(anime_box, idx):
    try:
        genres = anime_box.find_elements(
            By.XPATH,
            f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//span[@class='genre']",
        )
    except Exception as e:
        return None
    # for genre in genres:
    #     genre_set.add(genre.get_attribute("innerText"))
    return genres


### studio table
def collect_studios(anime_box, idx):
    try:
        studios = anime_box.find_elements(
            By.XPATH,
            f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//div[@class='property'][1]//a",
        )
    except Exception as e:
        return None
    return studios


### source table
def collect_source(anime_box, idx):
    try:
        source = (
            anime_box.find_element(
                By.XPATH,
                f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//div[@class='property'][2]//span[@class='item']",
            )
            .get_attribute("innerText")
            .strip()
        )
    except Exception as e:
        return None
    return source


### theme table
def collect_themes(anime_box, idx):
    try:
        themes = anime_box.find_elements(
            By.XPATH,
            f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//div[@class='property'][3]//span[@class='item']",
        )
    except Exception as e:
        return None
    return themes


### demographic table
def collect_demographics(anime_box, idx):
    try:
        demographics = anime_box.find_elements(
            By.XPATH,
            f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//div[@class='property'][4]//span[@class='item']",
        )
    except Exception as e:
        return ["Unknown"]
    return demographics


### broadcast table
def collect_broadcasts(anime_box, idx, broadcast_set):
    try:
        broadcasts = anime_box.find_elements(
            By.XPATH,
            f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//div[@class='broadcast']//i",
        )
    except Exception as e:
        return broadcast_set
    return broadcasts
