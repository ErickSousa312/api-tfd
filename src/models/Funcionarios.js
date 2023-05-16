const mongoose = require('mongoose');
const autoIncrement = require('mongoose-auto-increment');

autoIncrement.initialize(mongoose.connection);

const FuncionarioSchema = new mongoose.Schema({
    nomeFuncionario: { type: Number, required: true },
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
    Observação: { type: String }
});

FuncionarioSchema.plugin(autoIncrement.plugin, { model: 'Funcionario', field: '_id' });

const Funcionario = mongoose.model('Funcionario', FuncionarioSchema);

module.exports = Funcionario;