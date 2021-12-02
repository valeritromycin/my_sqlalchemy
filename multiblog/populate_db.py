import random
from datetime import datetime

import tables
from multiblog.constants import TEXT, NAMES, SURNAMES, TAGS


def while_deco(func):
    def wrapper(self):
        objects = []
        while self.count:
            instance = func(self)
            objects.append(instance)
            self.count -= 1
        return objects

    return wrapper


@while_deco
def create_authors(self):
    author = tables.Author(
       author_name=self.random(NAMES),
       author_surname=self.random(SURNAMES)
    )
    return author


@while_deco
def create_publications(self, authors):
    publications = []
    for elem in authors:
        publics_count = self.count if self.count else random.randint(50, 100)
        while publics_count:
            content = self.random_text(TEXT)
            publication = tables.Publication(
                post_title=content[:content.find(" ")],
                post_date=self.random_date(datetime))
            publications.append(publication)
            publics_count -= 1
    return publications


@while_deco
def create_tags(self):
    tag = tables.Tag(
        tag_title=self.random(TAGS)
    )
    return tag

