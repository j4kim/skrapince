from bs4 import BeautifulSoup
import requests
import config

def scrape() -> str:
    """Make a request to the website and parse the data"""

    response = requests.get(config.URL, timeout=10)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, "html.parser")

    element = soup.select_one(config.SELECTOR)

    return element.get_text()
