from app import db

class Books(db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String)
    author_name = db.Column(db.String)
    published_date = db.Column(db.String)
    number_of_books = db.Column(db.String)
    rack_number = db.Column(db.String)

    def __repr__(self):
        return "<Book: {}>".format(self.book_name)

