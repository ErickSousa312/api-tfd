const router = require('express').Router()
const MedicoController = require('../../Controllers/MedProfController');

//Rotas medicos
router.post('/', MedicoController.post);
router.get('/:id', MedicoController.get);
router.delete('/:id', MedicoController.delete);
router.put('/:id', MedicoController.update);

module.exports = router;
