const { Pool, Client } = require('pg')
const express = require('express')
const app = express()
const port = 3000

// connections string: postgres://{user}:{password}@{hostname}:{port}/{database-name}
const client = new Client({
  user: 'my_db_user',
  host: 'localhost',
  database: 'my_db',
  password: 'password',
  port: 5432, // This is the default port for PostgreSQL
})
client.connect()

app.get('/', async (req, res) => {
  const response = await (await client.query('SELECT * FROM Users')).rows  
  res.send(response)
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})