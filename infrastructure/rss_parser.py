from datetime import datetime, date

import requests
from bs4 import BeautifulSoup
from functional import seq
from pytimeparse.timeparse import timeparse

from domain.model.Podcast import Podcast

rss_url = 'https://feeds.audiomeans.fr/feed/d7c6111b-04c1-46bc-b74c-d941a90d37fb.xml'


def extract_podcasts():
    global response, soup
    try:
        response = requests.get(rss_url)
    except Exception as e:
        print('Error fetching the URL: ', rss_url)
        print(e)

    try:
        soup = BeautifulSoup(response.text, 'xml')
    except Exception as e:
        print('Could not parse the xml: ', rss_url)
        print(e)

    return (seq(soup.findAll('item'))
            .map(rss_feed_to_podcast))


def rss_feed_to_podcast(element) -> Podcast:
    return Podcast(
        element.find('title').string,
        str_to_date(element.find('pubDate').string),
        str_to_duration(element.find('duration').string),
        element.find('enclosure')['url']
    )


def str_to_date(date_str: str) -> date:
    return (datetime
            .strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
            .date())


def str_to_duration(str_duration: str) -> int:
    return timeparse(str_duration)
