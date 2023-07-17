from flask import Flask, render_template, request, redirect

from gamers import Gamers

app=Flask(__name__)

@app.route('/')                                             #redirecting index route to users
def index():
    return redirect('/gamers')

@app.route('/gamers')
def gamers():
    return render_template("gamers.html", gamers=Gamers.get_all())

if __name__=="__main__":                                    #This black need to be last in file
    app.run(host='localhost', port=5002, debug=True)