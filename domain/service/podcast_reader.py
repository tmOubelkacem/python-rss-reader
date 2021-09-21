from collections import Sequence

from domain.model.Podcast import Podcast
from infrastructure.rss_parser import extract_podcasts


def list_podcasts() -> Sequence[Podcast]:
    return (extract_podcasts()
            .group_by(lambda p: p.publication_date)
            .reduce_by_key(lambda p: max(p.duration))
            .map(lambda tu: tu[1][0]))
