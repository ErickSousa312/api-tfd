const mongoose = require('mongoose');

const PacienteSchema = new mongoose.Schema({
    _id: { type: Number, default: 1, required: true},
    DataNascimento: { type: Number, required: true },
    numeroCPF: { type: String, required: true },
    orgaoEmissor: { type: String, required: true },
    NumeroCartaoSUS: { type: Number, required: true },
    NumeroTituloEleitor: { type: Number, required: true },
    UF: { type: String, required: true, maxlength: 2 },
    NomePaciente: { type: String, required: true },
    NomeSocial: { type: String },
    Sexo: { type: String, required: true },
    Idade: { type: Number, required: true },
    raca:{type:String, required: true},
    cor:{type:String, required: true},
    Sangue: { type: String, maxlength: 3},
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
    Email: { type: String , required: true},
    identZona: { type: String , required: true},
    TratamentoAtual: { type: String , required: true},
    Ocupacao: { type: String, required: true },
    GrauEstudo: { type: String , required: true},
    Conta: { type: Number , required: true},
});


PacienteSchema.pre('save', async function(next) {
    if (!this.isNew) {
      return next();
    }
    const lastEntity = await Paciente.findOne({}, {}, { sort: { '_id' : -1 } });
    if (lastEntity && lastEntity._id) {
      this._id = lastEntity._id + 1;
    }
    next();
  });


const Paciente = mongoose.model('Paciente', PacienteSchema);

module.exports = Paciente;


/*JSON Exemplo
{
    "DataNascimento": 1990,
    "numeroCPF": "12345678901",
    "orgaoEmissor": "SSP",
    "NumeroCartaoSUS": 987654321,
    "NumeroTituloEleitor": 12345,
    "UF": "SP",
    "NomePaciente": "João da Silva",
    "NomeSocial": "",
    "Sexo": "M",
    "Idade": 32,
    "Sangue": "O+",
    "DataCadastro": "2023-05-17",
    "NomePaiouResponsavel": "",
    "NomeMae": "Maria Oliveira",
    "EstadoCivil": "Solteiro(a)",
    "Endereco": "Rua das Flores, 123",
    "Bairro": "Centro",
    "UfCidade": "SP",
    "CEP": "01234567",
    "Celular": [
      {
        "Numero": "987654321"
      }
    ],
    "Email": "joao.silva@example.com",
    "identZona": "Zona Urbana",
    "TratamentoAtual": "Tratamento X",
    "Ocupacao": "Engenheiro",
    "GrauEstudo": "Ensino Superior",
    "Conta": 12345
  }
  */