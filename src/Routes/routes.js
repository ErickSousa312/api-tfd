const PacienteRoutes = require ('./routesModels/pacienteRoutes')
const MedicoRoutes = require ('./routesModels/medicoRoutes')
const FuncionariosRoutes = require('./routesModels/funcionarioRoutes')
const EntidadeRoutes = require('./routesModels/entidadeRoutes')
const AtendAssSocialRoutes = require('./routesModels/atendAssSocialRoutes')
const ProcessoRoutes = require('./routesModels/processoRoutes')

function configRotas(app) {
    app.use('/paciente', PacienteRoutes);//ok
    app.use('/med', MedicoRoutes);//ok
    app.use('/func', FuncionariosRoutes);//ok
    app.use('/entid', EntidadeRoutes);//ok
    app.use('/atend', AtendAssSocialRoutes);//ok
    app.use('/processo', ProcessoRoutes);//ok
}

module.exports = configRotas