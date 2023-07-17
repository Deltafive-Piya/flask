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

@app.route("/edit/<int:id>")
def edit_user(id):
    data = User.get_one(id)     
    return render_template("edit.html", person = data)

@app.route("/user/update", methods = ["POST"])
def update_user():
    User.update(request.form)
    return redirect ("/")


@app.route("/user/add", methods = ["POST"])
def create_user():
    User.save(request.form)
    return redirect("/")

@app.route("/user/delete/<int:id>")
def delete_user(id):
    User.delete(id)

    return redirect('/')

@app.route("/user/show/<int:id>")
def show(id):
    data = User.get_one(id)
    return render_template("show.html", person = data)

#MAKE SURE THIS IS AT THE BOTTOM
if __name__=="__main__":
    app.run(host="localhost", port=5001,debug=True)