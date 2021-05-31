
from app.app import db
from app.models.usermodel import User

class bookInfo(db.Document):
    bookname=db.StringField(required=True)
    author=db.StringField(required=True)
    serialno=db.StringField(required=True)
    buser=db.ReferenceField(User)
    issued_on=db.DateTimeField()
    to_be_returned=db.DateTimeField()
