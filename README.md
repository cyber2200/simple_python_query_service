# simple_python_query_service
<p>
Simple script to execute SQL queries on a server
</p>
<code>
curl -d '{"db": "dct_mysql01", "q": "INSERT INTO `test` SET `id` = 1000; SELECT * FROM `test`;"}' -H "Content-Type: application/json" -X POST http://localhost:3000/q
</code>
