from mysqlconnection import connectToMySQL


# global users_db === 'users'
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['f_name']
        self.last_name = data['l_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod

    def get_all(cls):
        'tyler'
        #query, results, restore
        #query=mysql from line 1
        query = 'SELECT * FROM users'
        # calling method from mysqlconnection, selecting data from db w/ above query
        results = connectToMySQL('users').query_db(query) #TO-DO change this to match the mysqldb db name---------------------------------------


        users = []

        for user in results:
            users.append(cls(user))

        return users
    
    @classmethod

    def save(cls, data):
        query = "INSERT INTO users(f_name,l_name, email) VALUES( %(f_name)s, %(l_name)s, %(email)s )"

        results = connectToMySQL('users').query_db(query, data) #TO-DO change this to match the mysqldb db name---------------------------------------

        return results
