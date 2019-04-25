from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///bookdetails.db', echo=True)
Base = declarative_base()

class Books(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    book_name = Column(String)
    author_name = Column(String)
    published_date = Column(String)
    number_of_books = Column(String)
    rack_number = Column(String)

    def __repr__(self):
        return "<Book: {}>".format(self.book_name)



# create tables
Base.metadata.create_all(engine)
