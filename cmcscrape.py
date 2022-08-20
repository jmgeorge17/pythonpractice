import requests
from bs4 import BeautifulSoup
from lxml import html


def access_websites():
    names = token_names()

    # Iterate through each token url
    for name in names:
        url = "https://coinmarketcap.com" + name
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        tags = soup.find_all(
            "a", class_="link-button", lang="en", rel="nofollow noopener"
        )
        print(tags[0]["href"])


def token_names():
    # Access the 'New Cryptocurrencies' from CMC website and pass through BS4
    url = "https://coinmarketcap.com/new/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # Find the 'a' tags that posses a class of 'cmc-link'
    tags = soup.find_all("a", class_="cmc-link")

    # Filter through tags and find the relevant 'href' links
    hrefs = []
    for tag in tags:
        try:
            if "/currencies/" in tag["href"]:
                hrefs.append(tag["href"])
        except KeyError:
            pass

    # Return the list of links for use in the main function
    return hrefs


access_websites()
