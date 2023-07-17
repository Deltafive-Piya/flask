Altered Fork of: https://github.com/immanuelvatta/Python/commits?author=immanuelvatta

workflow:
env:mySQL WorkBench
        make diagram(s)
            make table(s)
        

# Pre-checklist install
installing pipenv on a global scope
`!Only needs to be done once!`

```console
pip install pipenv
``` 

# Start of checklist
- Create a folder for our new assignment
- go into that folder
- create the virtual env with flask

```console
pipenv install flask PyMySQL
```
- WARNING! Make sure pipfile & pipfile.lock are there!! If not FIX THIS NOW!!!
- activate virtual env
```console
pipenv shell
```

---
- Create folder structure
- Flask_MySQL DynoCap


```
- flask_app(📂)
    - config (📂)
        - mysqlconnection.py(📄)
    - controllers (📂)
        # You will have a controller file for every table table in your database
        -controller_user.py(📄)
    - models (📂)
        # You will have a model file for every table in your database
        model_user.py(📄)
    - static (📂)
        - css(📂)
            - styles.css (📄)
        - img (📂)
        - js(📂)
    - templates (📂)
        - index.html (📄)
    - __init__.py (📄)
- pipfile(📄)
- pipfile.lock(📄)
- server.py(📄)
```

## Create server.py

```Py
from flask import Flask, render_template, request, redirect

app=Flask(__name__)

@app.route('/')                                             #redirecting index route to users
def index():
    return redirect('/users')

if __name__=="__main__":                                    #This black need to be last in file
    app.run(host='localhost', port=5002, debug=True)


```
- Create templates folder
- add index.html in templates folder
- Test it out

## Create mysqlconnection.py file

```PY
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = False)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query:str, data:dict=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
```

## create model file
```PY
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for dict in results:
            friends.append( cls(dict) )
        #friends become a list of objects
        return friends
```

## create controller.py file
```
```

## create  \_\_init__.py file
```PY
from flask import Flask, render_template, session, request, redirect
#app = instance of Flask (class)
app = Flask(__name__)
app.secret_key = "do not forget to add secret key"
```