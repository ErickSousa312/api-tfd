const router = require('express').Router()
const Usuario = require('../../Controllers/AuthController')

//Rotas Usuarios
router.post('/signUp', Usuario.signUp)
router.post('/signIn', Usuario.signIn)

module.exports = router;