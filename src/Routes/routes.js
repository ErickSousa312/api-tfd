const cors = require('cors')
const routes = require('express').Router()
const teste = require('../Controllers/EleicaoController')

routes.use(cors())

routes.get('/', (req,res)=>{
    res.json({msg:"ta rodando pai"})
    console.log("hi")
})

// Rota Eleicao
routes.post('/teste', teste.post)

module.exports = routes