from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import mysql.connector

app = FastAPI()

# curl -d '{"db": "dct_mysql01", "q": "INSERT INTO `test` SET `id` = 1000; SELECT * FROM `test`;"}' -H "Content-Type: application/json" -X POST http://localhost:3000/q
@app.post("/q")
async def q(request: Request):
    req_data = await request.json()

    queries = req_data['q'].split(';');
    queries = list(filter(None, queries))

    q_res = []
    for q in queries:
        try:
            if req_data['db'] != '':
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="dct_mysql01",
                    password="123qwe",
                    database=req_data['db']
                )
            else:
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
            return JSONResponse(content={'res': 'NOK', 'err': str(err)})
    
    return JSONResponse(content={'res': 'OK', 'q_res': q_res})