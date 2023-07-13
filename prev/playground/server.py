from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def hello():
    return 'Welcome to the Playground!'

@app.route('/play/<int:x>')                     #Adjustment from /play to /play/num_goes_here
def play_number(x):
    return render_template('play.html', x=x)    #Redundant Assignment

@app.route('/play/<int:x>/<color>')             #Adjustment from /play to /play/num/color_goes_here
def play_numbers_colors(x, color):
    return render_template('play.html', x=x, color=color)

if __name__ == '__main__':
    app.run()