const router = require('express').Router()
const Paciente = require('../../Controllers/PacienteController');

//Rotas Pacientes
router.post('/', Paciente.post);
router.get('/:id', Paciente.get);
router.delete('/:id', Paciente.delete);
router.put('/:id', Paciente.update);

module.exports = router;