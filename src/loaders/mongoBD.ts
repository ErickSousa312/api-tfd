const mongoose = require('mongoose')
import {app} from '../app'
import error from 'console'
import * as dotenv from 'dotenv';

dotenv.config();

const port: string | undefined = process.env.ServerPort;
const url: string = `${process.env.DB_url}`

async function startDB() {
  try {
    mongoose.set('strictQuery', true);
    await mongoose.connect(url);

    console.log('Conectado ao MongoDB!');
    app.listen(port, () => {
      console.log(`Servidor rodando na porta ${port}`);
    });
  } catch (error) {
    console.error('Erro ao conectar ao MongoDB:', error);
  }
}

module.exports = startDB;


