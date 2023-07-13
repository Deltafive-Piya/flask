from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)


@app.route("/")
def read():

    user = User.get_all()
    return render_template('read.html', all_users = user)




@app.route("/user/create")
def read_user():

    return render_template("create.html")



@app.route("/user/add", methods = ["POST"])
def create_user():
    User.save(request.form)
    return redirect("/")




#MAKE SURE THIS IS AT THE BOTTOM
if __name__=="__main__":
    app.run(debug=True)