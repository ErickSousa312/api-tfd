const cors = require('cors')
const routes = require('express').Router()
const teste = require('../Controllers/EleicaoController')
const Paciente = require('../Controllers/PacienteController')
const Medico = require('../Controllers/MedProfController')
const Funcionario = require('../Controllers/FuncionarioController')
const Entidade = require('../Controllers/EntidadeController')
const AtendAssSocial = require('../Controllers/AtendAssSocialController')
const Processo = require('../Controllers/ProcessoController')

routes.use(cors())

routes.get('/', (req,res)=>{
    res.json({msg:"ta rodando pai"})
    console.log("hi")
})
// Rotas Paciente
routes.post('/teste', Paciente.post);
routes.get('/teste/:id', Paciente.get);
routes.delete('/teste/:id', Paciente.delete);
routes.put('/teste/:id', Paciente.update);

// Rotas Medico
routes.post('/med', Medico.post);
routes.get('/med/:id', Medico.get);
routes.delete('/med/:id', Medico.delete);
routes.put('/med/:id', Medico.update);

// Rotas Funcionario
routes.post('/func', Funcionario.post);
routes.get('/func/:id', Funcionario.get);
routes.delete('/func/:id', Funcionario.delete);
routes.put('/func/:id', Funcionario.update);

// Rotas Entidade
routes.post('/ent', Entidade.post);
routes.get('/ent/:id', Entidade.get);
routes.delete('/ent/:id', Entidade.delete);
routes.put('/ent/:id', Entidade.update);

// Rotas AtendAssSocial
routes.post('/atend', AtendAssSocial.post);
routes.get('/atend/:id', AtendAssSocial.get);
routes.delete('/atend/:id', AtendAssSocial.delete);
routes.put('/atend/:id', AtendAssSocial.update);

// Rotas Processo
routes.post('/processo', Processo.post);
routes.get('/processo/:id', Processo.get);
routes.delete('/processo/:id', Processo.delete);
routes.put('/processo/:id', Processo.update);

module.exports = routes