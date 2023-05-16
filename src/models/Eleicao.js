const mongoose = require('mongoose');
const autoIncrement = require('mongoose-auto-increment');

autoIncrement.initialize(mongoose.connection);

const eleicoesSchema = new mongoose.Schema({
  nomeEleicao: { type: String, required: true },
  celular: [{
    chave: { type: String, required: true },
    valor: { type: Number, required: true }
  }],
  hash: { type: String, required: true },
});

eleicoesSchema.plugin(autoIncrement.plugin, { model: 'Eleicoes', field: '_id' });

const Eleicoes = mongoose.model('Eleicoes', eleicoesSchema);

module.exports = Eleicoes;
