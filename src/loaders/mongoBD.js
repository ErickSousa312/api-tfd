const MongoClient = require('mongodb').MongoClient;
const app = require('../app')

const mongoose = require('mongoose')

const port = 3000;
const uri = 'mongodb://127.0.0.1:27017';

const url = `mongodb://127.0.0.1:27017/db-teste'`

async function startDB(){
  mongoose.set("strictQuery", true)
  await mongoose.connect(
      url
  )
  .then(
      console.log('Conectado ao MongoBD!'),
      app.listen(3000)
  )
  .catch(
      error=>console.log(error)
  )
}
module.exports = startDB;


