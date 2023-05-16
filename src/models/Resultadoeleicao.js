const mongoose = require('mongoose')

const ResultadoEleicao = mongoose.model('resultadoEleicao', {
    eleicao:{type: mongoose.Schema.Types.ObjectId, ref: 'eleicoes', required: true},
    email:{type: String, required: true},
    voto:{type: String, required: true},
    hash: {type:String, required:false}
})

module.exports = ResultadoEleicao