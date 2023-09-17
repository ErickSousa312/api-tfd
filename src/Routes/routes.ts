import { Express } from 'express';

const PacienteRoutes = require ('./routesModels/pacienteRoutes')
const MedicoRoutes = require ('./routesModels/medicoRoutes')
const FuncionariosRoutes = require('./routesModels/funcionarioRoutes')
const EntidadeRoutes = require('./routesModels/entidadeRoutes')
const AtendAssSocialRoutes = require('./routesModels/atendAssSocialRoutes')
const ProcessoRoutes = require('./routesModels/processoRoutes')
const UsuariosRoutes = require('./routesModels/authRoutes')
const ReportEntidade = require('./routesModels/reportRoutes')


const TokenJWTmiddleware = require('../AuthJWT/jwtMiddleware')
const TokenVerify = require('../AuthJWT/jwtVerify')

function configRotas(app:Express) {
    app.use('/paciente', PacienteRoutes);//ok
    app.use('/med',TokenJWTmiddleware, MedicoRoutes);//ok
    app.use('/func',TokenJWTmiddleware, FuncionariosRoutes);//ok
    app.use('/entid',TokenJWTmiddleware, EntidadeRoutes);//ok
    app.use('/atend',TokenJWTmiddleware, AtendAssSocialRoutes);//ok
    app.use('/processo',TokenJWTmiddleware, ProcessoRoutes);//ok
    app.use('/login', UsuariosRoutes);//ok
    app.use('/verifyToken', TokenVerify)
    app.use('/Report', ReportEntidade)
}

export{configRotas}