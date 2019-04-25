# main.py

import os

from flask import flash, redirect, render_template, request, session

from app import app
from db_setup import init_db, db_session
from forms import BooksForm, BooksSearchForm
from models import Books
from tables import Results

init_db()

# To Kill Process
# ps -fA | grep python

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return index()
    else:
        #flash('wrong password!')
        return home()

@app.route('/do_login')
def home():
    if not session.get('logged_ino'):
        return render_template('login.html')
    else: return """MOTHING  """

@app.route('/', methods=['GET', 'POST'])
def index():
    search = BooksSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
        qry = db_session.query(Books)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)

def save_changes(book, form, new=False):
    """
    Save the changes to the database
    """
    book.book_name = form.book_name.data
    book.author_name = form.author_name.data
    book.published_date = form.published_date.data
    book.number_of_books = form.number_of_books.data
    book.rack_number = form.rack_number.data

    if new:
        # Add the new book record to the database
        db_session.add(book)

    # commit the data to the database
    db_session.commit()

@app.route('/create', methods=['GET', 'POST'])
def create():
    """
    Add a new record
    """
    form = BooksForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the record
        book = Books()
        save_changes(book, form, new=True)
        flash('Record created successfully!')
        return redirect('/')

    return render_template('create.html', form=form)

@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Books).filter(
        Books.id==id)
    book = qry.first()

    if book:
        form = BooksForm(formdata=request.form, obj=book)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(book, form)
            flash('Record updated successfully!')
            return redirect('/')
        return render_template('edit.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='127.0.0.1', port=5000)
