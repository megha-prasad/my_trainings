from app.app import api, app, login_manager
from app.models.usermodel import User
from app.views.userdetails import userregister,userlogin
from app.views.bookdetails import search,add,update,delete,fullbooks,logged_in,borrowbooks,borrowedbooks
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user):
    """current user details"""
    return User.objects.get(id=user)
#for login
app.add_url_rule("/", view_func=userlogin, methods=["GET","POST"])
#for user register
app.add_url_rule("/register",view_func=userregister,methods=["GET","POST"])
#your home page
app.add_url_rule("/logged_in",view_func=logged_in,methods=["GET","POST"])
#to display all available books
app.add_url_rule("/fullbooks",view_func=fullbooks,methods=["GET","POST"])
#to borrow books
app.add_url_rule("/borrowbooks",view_func=borrowbooks,methods=["GET","POST"])
#borrowed books
app.add_url_rule("/borrowedbooks",view_func=borrowedbooks,methods=["GET","POST"])
#to search
app.add_url_rule("/search",view_func=search,methods=["GET","POST"])
#to add
app.add_url_rule("/add",view_func=add,methods=["GET","POST"])
#to update
app.add_url_rule("/update",view_func=update,methods=["GET","POST"])
#to delete
app.add_url_rule("/delete",view_func=delete,methods=["GET","POST"])
