from config.mysqlconnection import connectToMySQL #include config to reach folder


# global users_db === 'users'
class User:
    def __init__(self,data):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        #query, results, restore
        #query=mysql from line 1
        query = "SELECT * FROM users"
        # calling method from mysqlconnection, selecting data from db w/ above query
        results = connectToMySQL('users_db').query_db(query) #TO-DO change this to match the mysqldb db name---------------------------------------

        magicalZombies = []
        for zoro in results:
            magicalZombies.append(cls(zoro))
        return magicalZombies
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users(f_name,l_name, email) VALUES( %(f_name)s, %(l_name)s, %(email)s )"
        results = connectToMySQL('users_db').query_db(query, data) #REMEMBER- change this to match the mysqldb db name---------------------------------------
        return results
    
    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_db').query_db(query, { 'id': id })[0]
        return results

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET f_name = %(f_name)s, l_name = %(l_name)s, email = %(email)s WHERE id = %(id)s;"
        results = connectToMySQL('users_db').query_db(query, data)
        return results
    
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_db').query_db(query, { 'id': id })
        return results
    