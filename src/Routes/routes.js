const PacienteRoutes = require ('./routesModels/pacienteRoutes')
const MedicoRoutes = require ('./routesModels/medicoRoutes')
const FuncionariosRoutes = require('./routesModels/funcionarioRoutes')
const EntidadeRoutes = require('./routesModels/entidadeRoutes')
const AtendAssSocialRoutes = require('./routesModels/atendAssSocialRoutes')
const ProcessoRoutes = require('./routesModels/processoRoutes')
const UsuariosRoutes = require('./routesModels/authRoutes')

const TokenVerify = require('../AuthJWT/jwtMiddleware')

function configRotas(app) {
    app.use('/paciente',TokenVerify, PacienteRoutes);//ok
    app.use('/med',TokenVerify, MedicoRoutes);//ok
    app.use('/func',TokenVerify, FuncionariosRoutes);//ok
    app.use('/entid',TokenVerify, EntidadeRoutes);//ok
    app.use('/atend',TokenVerify, AtendAssSocialRoutes);//ok
    app.use('/processo',TokenVerify, ProcessoRoutes);//ok
    app.use('/login', UsuariosRoutes);//ok
}

module.exports = configRotas