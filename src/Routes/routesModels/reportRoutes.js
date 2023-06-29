const router = require('express').Router()
const ReportEntidade=require('../../Controllers/reportController')

router.get('/:id', ReportEntidade.get)

module.exports = router