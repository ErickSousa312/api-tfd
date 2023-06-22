const mongoose = require('mongoose')
const app = require('../app')
require('dotenv').config();

const port = process.env.ServerPort;
const url = `${process.env.DB_url}`

async function startDB(){
  mongoose.set("strictQuery", true)
  await mongoose.connect(
      url
  )
  .then(
      console.log('Conectado ao MongoBD!'),
      app.listen(port, ()=>{
        console.log(`Servidor rodando na porta ${port}`)
      })
  )
  .catch(
      error=>console.log(error)
  )
}
module.exports = startDB;


