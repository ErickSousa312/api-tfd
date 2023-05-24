const router = require('express').Router()
const Medico = require('../../Controllers/MedProfController');

//Rotas medicos
router.post('/', Medico.post);
router.get('/:id', Medico.get);
router.delete('/:id', Medico.delete);
router.put('/:id', Medico.update);

module.exports = router;
