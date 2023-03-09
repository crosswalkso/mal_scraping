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
    except Exception as e:
        # "'Unknown'"
        title = "Unknown"
    # return f"'title'"
    return title


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
    except Exception as e:
        synopsis = "Unknown"
    return synopsis


### genre table list

### studio table

### source table

### theme table

### demographic table

### broadcast table
