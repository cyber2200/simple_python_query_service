import mysql.connector

class Db:
    def q(self, q, db):
        # Split query
        queries = q.split(';');
        queries = list(filter(None, queries))

        q_res = []
        for q in queries:
            try:
                #if db is selected
                if db != '':
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="dct_mysql01",
                        password="123qwe",
                        database=db
                    )
                else: # If there is no db selected
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="dct_mysql01",
                        password="123qwe"
                    )
                mycursor = mydb.cursor()
                mycursor.execute(q)
                for row in mycursor:
                    q_res.append(row)
                
                # commit only when needed
                mydb.commit()
                mydb.close()
            except mysql.connector.Error as err:
                return {'res': 'NOK', 'err': str(err)}
        
        return {'res': 'OK', 'q_res': q_res}