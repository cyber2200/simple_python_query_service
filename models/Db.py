import mysql.connector
import configparser
import json

class Db:
    # Get config from json file
    def getConfigData(self):
        f = open('config.json') 
        data = json.load(f)
        return data
    
    # get MySQL connection
    def getConnection(self, db):
        config = self.getConfigData()
        if db != '':
            connection = mysql.connector.connect(
                host=config['host'],
                user=config['user'],
                password=config['password'],
                database=db
            )
        else: # If there is no db selected
            connection = mysql.connector.connect(
                host=config['host'],
                user=config['user'],
                password=config['password']
            )
        return connection
    
    # Query and format the data
    def q(self, q, db):
        # Split query - if there is more than one
        queries = q.split(';');
        queries = list(filter(None, queries))

        res = []
        # Passing on all the queries
        qc = 0
        for q in queries:
            q_res = []
            try:
                connection = self.getConnection(db)
                
                cursor = connection.cursor()
                cursor.execute(q)
                for row in cursor:
                    t_row = []
                    for v in row: # Convert to strings
                        t_row.append(str(v))
                    q_res.append(t_row)
                
                # commit only when needed
                if q.lower().startswith('update') or q.lower().startswith('delete') or q.lower().startswith('insert'):
                    connection.commit()
                connection.close()

                # If the query is select * ... add the columns to the result
                if q.lower().strip().startswith('select * from'):
                    connection = self.getConnection(db)
                    table_name = q.strip().split(' ')[3]
                    cursor = connection.cursor()
                    cursor.execute('DESC ' + table_name)
                    table_desc = cursor.fetchall()
                    column_names = []
                    for column in table_desc:
                        column_names.append(column[0])
                    rows = []
                    print('---------------------')
                    for row2 in q_res:
                        t_row = {}
                        i = 0
                        for column_name in column_names:
                            print(row2)
                            print(i)
                            t_row[column_name] = row2[i]
                            i = i + 1
                        rows.append(t_row)

                    q_res = rows
                # Append to res and increase counter
                res.append({'q' + str(qc): q_res})
                qc = qc + 1
            except mysql.connector.Error as err:
                return {'res': 'NOK', 'err': str(err)}
        
        return {'res': 'OK', 'res': res}