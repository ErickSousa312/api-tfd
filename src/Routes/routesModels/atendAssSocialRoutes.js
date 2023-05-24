const router = require('express').Router()
const AtendAssSocial = require('../../Controllers/AtendAssSocialController')

//Rotas Ass Social
router.post('/atend', AtendAssSocial.post);
router.get('/atend/:id', AtendAssSocial.get);
router.delete('/atend/:id', AtendAssSocial.delete);
router.put('/atend/:id', AtendAssSocial.update);

module.exports = router