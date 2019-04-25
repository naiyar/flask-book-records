# forms.py

from wtforms import Form, StringField, SelectField, validators

class BooksSearchForm(Form):
    search = StringField('')

class BooksForm(Form):
    book_name = StringField('Book Name')
    author_name = StringField('Auther Name')
    published_date = StringField('Published Date')
    number_of_books = StringField('Number Of Books')
    rack_number = StringField('Rack Number')
