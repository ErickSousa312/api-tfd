const mongoose = require('mongoose');
const autoIncrement = require('mongoose-auto-increment');

autoIncrement.initialize(mongoose.connection);

const PacienteSchema = new mongoose.Schema({
    DataNascimento: { type: Number, required: true },
    numeroCPF: { type: String, required: true },
    orgaoEmissor: { type: String, required: true },
    NumeroCartaoSUS: { type: Number, required: true },
    numeroTituloEleitor: { type: Number, required: true },
    UF: { type: String, required: true },
    NomePaciente: { type: String, required: true },
    NomeSocial: { type: String },
    Sexo: { type: String, required: true },
    Idade: { type: Number, required: true },
    Sangue: { type: String },
    dataCadastro: { type: Date, required: true },
    NomePaiouResponsavel: { type: String },
    NomeMae: { type: String, required: true },
    EstadoCivil: { type: String },
    Endereco: { type: String, required: true },
    Bairro: { type: String, required: true },
    UfCidade: { type: String, required: true },
    CEP: { type: String, required: true },
    celular: [{
        chave: { type: String, required: true },
        valor: { type: Number, required: true }
    }],
    Email: { type: String },
    identZona: { type: String },
    TratamentoAtual: { type: String },
    Ocupacao: { type: String },
    GrauEstudo: { type: String },
    Conta: { type: Number },
    hash: { type: String, required: true },
});

PacienteSchema.plugin(autoIncrement.plugin, { model: 'Paciente', field: '_id' });

const Paciente = mongoose.model('Paciente', PacienteSchema);

module.exports = Paciente;
