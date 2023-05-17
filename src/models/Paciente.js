const mongoose = require('mongoose');

const PacienteSchema = new mongoose.Schema({
    ID: { type: Number, default: 1, required: true},
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
    DataCadastro: { type: Date, required: true },
    NomePaiouResponsavel: { type: String },
    NomeMae: { type: String, required: true },
    EstadoCivil: { type: String },
    Endereco: { type: String, required: true },
    Bairro: { type: String, required: true },
    UfCidade: { type: String, required: true },
    CEP: { type: String, required: true },
    Celular: [{
        Numero: { type: String, required: true },
    }],
    Email: { type: String },
    identZona: { type: String },
    TratamentoAtual: { type: String },
    Ocupacao: { type: String },
    GrauEstudo: { type: String },
    Conta: { type: Number },
});


PacienteSchema.pre('save', async function(next) {
    if (!this.isNew) {
      return next();
    }
    const lastEntity = await Paciente.findOne({}, {}, { sort: { 'contador' : -1 } });
    if (lastEntity && lastEntity.contador) {
      this.contador = lastEntity.contador + 1;
    }
    next();
  });


const Paciente = mongoose.model('Paciente', PacienteSchema);

module.exports = Paciente;
