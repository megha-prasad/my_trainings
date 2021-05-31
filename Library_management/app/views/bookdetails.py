import uuid
from app.app import db
from flask import jsonify,request,render_template,redirect, url_for
from flask_login import current_user
from app.models.usermodel import User
from app.models.bookmodels import bookInfo
from datetime import date

def logged_in():
    return render_template('logged_in.html')

def search():
    if request.method == 'POST':
        bookname = request.form["bookname"]
        books=bookInfo.objects(bookname=bookname).to_json()
        print(books)
        return render_template('search.html',books=books)
    return render_template("search.html")

    

def add():
    if request.method == 'POST':
        if(current_user.userrole=='admin'):
            bookname = request.form["bookname"]
            author = request.form["author"]
            serialno = request.form["serialno"]
            bookInfo.objects.create(bookname=bookname,author=author,serialno=serialno)
            return render_template('add.html')
    return render_template('add.html')

    

def update():
    if request.method == 'POST':
        if(current_user.userrole=='admin'):
            print(request.form)
            book_id=request.form["book_id"]
            book=bookInfo.objects.get(id=book_id)
            serialno = request.form["serialno"]
            newbookname = request.form["newbookname"]
            newauthor = request.form["newauthor"]
            book.bookname=newbookname
            book.author=newauthor
            book.serialno=serialno
            book.save()
            return render_template('update.html')
    return render_template('update.html')

def delete():
    if request.method == 'POST':
        if(current_user.userrole=='admin'):
            book_id=request.form["book_id"]
            book=bookInfo.objects.get(id=book_id)
            book.delete()
        return render_template('delete.html')
    return render_template('delete.html')

def fullbooks():
    if request.method == 'GET':
        book=bookInfo.objects.all().to_json()
        return render_template("fullbooks.html",book=book)
    return render_template("fullbooks.html")

def borrowedbooks():
    if request.method == 'GET' :
        if (current_user.userrole =="user"):
            new = bookInfo.objects(buser=current_user.id)
        return render_template("borrowedbooks.html",new=new)
    return render_template("borrowedbooks.html")


def borrowbooks():
    if request.method == 'GET':
        if (current_user.userrole == "user"):
            b=bookInfo.objects().to_json()
            return render_template("borrowbooks.html",b=b)
    if request.method == 'POST':
        if (current_user.userrole == "user"):
            book_id = request.form["book_id"]
            book = bookInfo.objects.get(id=book_id)
            issuser = current_user.id
            isdate=date.today().isoformat()
            book.buser=issuser
            book.issued_on=isdate
            book.save()
            return render_template("borrowbooks.html")
    return render_template("borrowbooks.html")



            
        






    
