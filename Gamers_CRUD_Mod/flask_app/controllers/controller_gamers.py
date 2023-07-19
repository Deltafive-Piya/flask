from flask import render_template, request, redirect

from flask_app import app

from flask_app.model.gamers import Gamers



# HOME
@app.route("/")  # redirecting index route to users page
def index():  # Index has function to resdirect to route(/gamers)
    return redirect("/gamers")

# REDIRECT.HOME
@app.route("/gamers")
def gamers():  # gamers route has gamers() function
    return render_template(
        "gamers.html", gamers=Gamers.get_all()
    )  # runs the gamers.py function get_all()



# CREATE DISPLAY
@app.route("/gamers/new")
def new():  # new() will display html new_gamer.html
    return render_template("new_gamer.html")

# CREATE ACTION
@app.route(
    "/gamers/create", methods=["POST"]
)  # requires a post method to post inputed data from html
def create():
    print(request.form)
    Gamers.save(
        request.form
    )  # This line added to allow for input passing on new_gamers (where def save() is called)
    return redirect("/gamers")



# SHOW DISPLAY
@app.route("/gamers/show/<int:id>")  # <int:id>
def show(id):
    data = {"id": id}
    return render_template("show_gamer.html", gamers=Gamers.get_one(data))



# UPDATE DISPLAY
@app.route("/gamers/update/<int:id>")  # <int:id>
def edit(id):
    data = {"id": id}
    return render_template("update_gamer.html", gamers=Gamers.get_one(data))

# UPDATE ACTION
@app.route("/gamers/update", methods=["POST"])  # METHODS NOT METHOD
def update():
    Gamers.update(request.form)
    return redirect("/gamers")



# DESTROY (ACTION ONLY; RELIANT ON HOME DISPLAY)
@app.route("/gamers/destroy/<int:id>")
def destroy(id):
    data = {"id": id}
    Gamers.destroy(data)  # The action to destroy lives in GamersDotPy
    return redirect("/gamers")