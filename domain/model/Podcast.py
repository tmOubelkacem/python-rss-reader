from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Podcast():
    title: str
    publication_date: date
    duration: int
    url: str
