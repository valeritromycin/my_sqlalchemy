import tables


class Query:

    def __init__(self, session):
        self.session = session

    def get_authors(self):
        tag = self.session.query(tables.Tag).first()
        authors = set()
        for itm in tag.publications:
            authors.add(itm.author)
        return list(authors)

    def get_tags(self):
        publications = self.session.query(tables.Publication).filter(tables.Publication.author_id == 1).all()
        tags = []
        for itm in publications:
            if itm.tags:
                tags.extend(itm.tags)
        return set(tags)