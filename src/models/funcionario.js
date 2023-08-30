const mongoose = require('mongoose');

const FuncionarioSchema = new mongoose.Schema({
    _id: { type: Number, default: 1, required: true},
    nomeFuncionario: { type: String, required: true },
    CPF: { type: String, required: true },
    Rg: { type: Number, required: true },
    NumeroMatricula: { type: Number, required: true },
    NumeroPortaria: { type: Number, required: true },
    Cidade: { type: String, required: true },
    UfCidade: { type: String, required: true },
    CEP: { type: String, required: true },
    Celular: [{
        Numero: { type: Number, required: true }
    }],
    AtividadeExercida: { type: String, required: true },
    DataNascimento: { type: String, required: true },
    CentroDeSaude: { type: String, required: true },
    DataCadastro: { type: String, required: true },
    Observacao: { type: String, required: true }
});


FuncionarioSchema.pre('save', async function(next) {
    if (!this.isNew) {
      return next();
    }
    const lastEntity = await Funcionario.findOne({}, {}, { sort: { '_id' : -1 } });
    if (lastEntity && lastEntity._id) {
      this._id = lastEntity._id + 1;
    }
    next();
  });
  
const Funcionario = mongoose.model('Funcionario', FuncionarioSchema);

module.exports = Funcionario;