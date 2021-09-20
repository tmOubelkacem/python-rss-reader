from infrastructure.rss_parser import extract_podcasts


def list_podcasts():
    podcasts_by_date = (extract_podcasts()
                        .group_by(lambda p: p.publication_date)
                        .reduce_by_key(lambda p: max(p.duration)))

    for art in podcasts_by_date:
        print("> Element : ", art)
