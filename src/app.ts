const express = require('express');

const {configRotas} = require('./Routes/routes');
const cors = require('cors')
const app = express();
app.use(
    express.urlencoded({extended:true})
)
app.use(express.json())
app.use(cors())

configRotas(app)

export{app}