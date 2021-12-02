from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Query

from multiblog import tables


class DataBase:

    def __init__(self, db_url):
        engine = create_engine(db_url)
        Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)


    @staticmethod
    def add_author(session):
        authors = create_author()
        session.add_all(authors)
        session.commit()
        return authors


    @staticmethod
    def add_publications(session, authors):
        publications = create_publications(authors)
        db = DataBase(db_url)
        session.add_all(publications)
        session.commit()
        return publications



    @staticmethod
    def add_tags(session):
        tags = create_tags()
        session.add_all(tags)
        session.commit()
        return tags


    def create_session(self):
        session = self.maker()
        try:
            authors = self.add_author(session)
            publications = self.add_publications(session, authors)
            tags = self.add_tags(session)
            session.commit()
            query = Query(session)
            query.get_tags()
            query.get_authors()
        except:
            session.rollback()
            raise
        finally:
            session.close()


if __name__ == '__main__':
    db_url = "sqlite:///db.multiblog"
    print(1)