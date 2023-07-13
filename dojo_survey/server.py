from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key= "qwerty1234"

#HOME ROUTE 
@app.route('/')
def home():
    print(session)
    return render_template('index.html')




# @app.route('/process', methods=['POST'])
# def process():
#     session['name'] = request.form.get('name')
#     session['location'] = request.form.get('location')
#     session['language'] = request.form.get('language')
#     session['comment'] = request.form.get('comment')
#     return redirect('/result')

# @app.route('/result')
# def result():
#     return render_template('result.html')




if __name__ == '__main__':                                          #Render the page---THIS GOES AT THE END OF THE FILE
    app.run(debug=True)
