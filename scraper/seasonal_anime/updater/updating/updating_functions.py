from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def collect_scores(anime_box: WebElement, idx):
    try:
        score = (
            anime_box.find_element(
                By.XPATH,
                f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//span[@class='js-score']",
            )
            .get_attribute("innerHTML")
            .strip()
        )
        if score == "0":
            score = "NULL"
    except Exception as e:
        # "'Unknown'"
        score = "Unknown"
    # return f"'score'"
    return score


def collect_members(anime_box: WebElement, idx):
    try:
        member = (
            anime_box.find_element(
                By.XPATH,
                f"//div[contains(@class, 'seasonal-anime-list')][1]//div[contains(@class, 'js-seasonal-anime') and not(contains(@class, 'js-kids'))][{idx+1}]//span[@class='js-members']",
            )
            .get_attribute("innerHTML")
            .strip()
        )
    except Exception as e:
        # "'Unknown'"
        member = "Unknown"
    # return f"'member'"
    return member


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
