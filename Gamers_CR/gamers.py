from mysqlconnection import connectToMySQL      #import mysqlconnection

class Gamers:                                   #line this up with the schema in the database
    #Include the respective tables' columns
    def __init__(self, data):
        self.id = data['id']                    #This was copied to populate the below, may need to adjust to match table
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.tag = data['tag']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.clan_id = data['clan_id']

    #CLASS METHOD
    @classmethod
    def get_all(cls):                            # get all the data from db and place it in our class USING A SELECT STATEMENT
        query = "SELECT * FROM gamers;"
        results = connectToMySQL('gamers').query_db(query)      #Input name of schema used; .query_db allows us to query db with 'query' stated 1 line above
        
        gamers = []                                             #This epmty list establishes a place to put our g
        for g in results:                                       # want to output as a list of 'gamer' objects; from dictionaries (sqldb) to objects(OOP language manipulateable)
            gamers.append( cls(g) )                               #g for gamer, translate for the initiation-------------------------------further explain------------------------
        return gamers                                           #return back results of the work