import mysql.connector

class Db:
    def getConnection(self, db):
        if db != '':
            connection = mysql.connector.connect(
                host="localhost",
                user="dct_mysql01",
                password="123qwe",
                database=db
            )
        else: # If there is no db selected
            connection = mysql.connector.connect(
                host="localhost",
                user="dct_mysql01",
                password="123qwe"
            )
        return connection
    def q(self, q, db):
        # Split query
        queries = q.split(';');
        queries = list(filter(None, queries))

        q_res = []
        for q in queries:
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

                if q.lower().startswith('select * from'):
                    connection = self.getConnection(db)
                    table_name = q.split(' ')[3]
                    cursor = connection.cursor()
                    cursor.execute('DESC ' + table_name)
                    table_desc = cursor.fetchall()
                    column_names = []
                    for column_name in table_desc:
                        column_names.append(column_name[0])
                    
                    rows = []
                    for row in q_res:
                        t_row = {}
                        i = 0
                        for column_name in column_names:
                            t_row[column_name] = row[i]
                            i = i + 1
                        rows.append(t_row)

                    q_res = rows
                    
            except mysql.connector.Error as err:
                return {'res': 'NOK', 'err': str(err)}
        
        return {'res': 'OK', 'q_res': q_res}