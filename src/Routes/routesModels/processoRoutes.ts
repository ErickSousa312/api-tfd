const router = require('express').Router()
import  ProcessoController from "../../Controllers/ProcessoController";

const Processo = new ProcessoController();

//Rotas Processos
router.post('/', Processo.post);
router.get('/:id', Processo.get);
router.get('/parecer/:id', Processo.getByIdPaciente)
router.delete('/:id', Processo.delete);
router.put('/:id', Processo.update);

module.exports = router