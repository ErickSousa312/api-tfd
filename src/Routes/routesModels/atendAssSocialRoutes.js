const router = require('express').Router()
const AtendAssSocial = require('../../Controllers/AtendAssSocialController')

//Rotas Ass Social
router.post('/', AtendAssSocial.post);
router.get('/:id', AtendAssSocial.get);
router.delete('/:id', AtendAssSocial.delete);
router.put('/:id', AtendAssSocial.update);

module.exports = router   