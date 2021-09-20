from datetime import date

from functional import seq

from domain.model.Podcast import Podcast
from infrastructure.rss_parser import extract_podcasts


class ReadRss:
    def __init__(self) -> seq(date, Podcast):

        self.podcasts_by_date = (extract_podcasts()
                                 .group_by(lambda p: p.publication_date)
                                 .reduce_by_key(lambda p: max(p.duration)))

        for art in self.podcasts_by_date:
            print("> Element : ", art)
