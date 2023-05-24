const router = require('express').Router()
const Entidade = require('../../Controllers/EntidadeController')

// Rotas Entidade
router.post('/', Entidade.post);
router.get('/:id', Entidade.get);
router.delete('/:id', Entidade.delete);
router.put('/:id', Entidade.update);

module.exports = router;