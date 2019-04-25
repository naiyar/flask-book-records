from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    book_name = Col('Book Name')
    author_name = Col('Auther Name')
    published_date = Col('Published Date')
    number_of_books = Col('Number Of Books')
    rack_number = Col('Rack Number')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))


