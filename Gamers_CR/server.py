from flask import Flask, render_template, request, redirect

from gamers import Gamers

app=Flask(__name__)

@app.route('/')                                             #redirecting index route to users page
def index():                                                #Index has function to resdirect to route(/gamers)
    return redirect('/gamers')

@app.route('/gamers')
def gamers():                                                       #gamers route has gamers() function
    return render_template("gamers.html", gamers=Gamers.get_all())  #runs the gamers.py function get_all()

@app.route('/gamers/new')
def new():                                                           #new() will display html new_gamer.html
    return render_template("new_gamer.html")


if __name__=="__main__":                                            #This black need to be last in file
    app.run(host='localhost', port=5002, debug=True)