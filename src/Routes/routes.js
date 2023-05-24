
const PacienteRoutes = require ('./routesModels/pacienteRoutes')
const MedicoRoutes = require ('./routesModels/medicoRoutes')
const FuncionariosRoutes = require('./routesModels/funcionarioRoutes')
const EntidadeRoutes = require('./routesModels/entidadeRoutes')
const AtendAssSocialRoutes = require('./routesModels/atendAssSocialRoutes')
const ProcessoRoutes = require('./routesModels/processoRoutes')

function configRotas(app) {
    app.use('/paciente', PacienteRoutes);
    app.use('/med', MedicoRoutes);
    app.use('/func', FuncionariosRoutes);
    app.use('/entid', EntidadeRoutes);
    app.use('/atend', AtendAssSocialRoutes);
    app.use('/proce', ProcessoRoutes);
}

module.exports = configRotas