const router = require('express').Router()
const Processo = require('../../Controllers/ProcessoController')

//Rotas Processos
router.post('/', Processo.post);
router.get('/:id', Processo.get);
router.delete('/:id', Processo.delete);
router.put('/:id', Processo.update);

module.exports = router;