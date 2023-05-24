const router = require('express').Router()
const Funcionario = require('../../Controllers/FuncionarioController');

//Rotas Funcionario
router.post('/', Funcionario.post);
router.get('/:id', Funcionario.get);
router.delete('/:id', Funcionario.delete);
router.put('/:id', Funcionario.update);

module.exports = router;