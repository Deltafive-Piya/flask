from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key= "qwerty1234"

# #ORIGINAL HOME ROUTE 
# @app.route('/')
# def home():
#     print(session)
#     return render_template('index.html')

# NEW HOME ROUTE with incrementor
@app.route('/')
def home():
    visit_count = session.get('visit_count', 0)                     #get visit_count || default of 0
    visit_count += 1                                                #incrementor
    session['visit_count'] = visit_count                            #set after increment
    return render_template('index.html', visit_count=visit_count)   #display set value

@app.route('/destroy_session')
def destroy_session():
    session.clear()                                                 #removes stored data
    return redirect(url_for('home'))                                #add dependency for IMPORT AT TOP





if __name__ == '__main__':                                          #Render the page---THIS GOES AT THE END OF THE FILE
    app.run(debug=True)
