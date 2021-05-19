from app.app import app
from app.view import home,addition,subtraction,multiplication,division


#home page
app.add_url_rule("/", view_func=home, methods=["GET","POST"])
#addition
app.add_url_rule("/addition",view_func=addition,methods=["GET","POST"])
#subtraction
app.add_url_rule("/subtraction",view_func=subtraction,methods=["GET","POST"])
#multiplication
app.add_url_rule("/multiplication",view_func=multiplication,methods=["GET","POST"])
#division
app.add_url_rule("/division",view_func=division,methods=["GET","POST"])