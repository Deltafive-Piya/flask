#import mysqlconnection
from mysqlconnection import connectToMySQL
#line this up with the schema in the database
class Gamers:                                   
    
    #This was copied to populate the below, may need to adjust to match table
    def __init__(self, data):
        self.id = data['id']                    
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.tag = data['tag']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.clan_id = data['clan_id']

    #CLASS METHOD
    @classmethod
    # get all the data from db and place it in our class USING A SELECT STATEMENT
    def get_all(cls):                            
        query = "SELECT * FROM gamers;"
        #Input name of schema used; .query_db allows us to query db with 'query' stated 1 line above
        results = connectToMySQL('gamers').query_db(query)      
        
        #This epmty list establishes a place to put our g
        gamers = []                                             
         # want to output as a list of 'gamer' objects; from dictionaries (sqldb) to objects(OOP language manipulateable)
        for g in results:
            #g for gamer, translate for the initiation-------------------------------further explain------------------------                                   
            gamers.append( cls(g) )
        #return back results of the work                            
        return gamers                                           