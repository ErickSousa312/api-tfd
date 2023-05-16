const mongoose = require('mongoose');
const autoIncrement = require('mongoose-auto-increment');

autoIncrement.initialize(mongoose.connection);

const MedProfSchema = new mongoose.Schema({
    IdPaciente: { type: mongoose.Schema.Types.ObjectId,ref:'Paciente', required: true},
    /*
        -NomePaciente
        -CPF
        -Idade
        -Endereço
        -Celular
        -Sexo
        -Menor de Idade
    */
    IdProcesso: { type: mongoose.Schema.Types.ObjectId,ref:'Processo', required: true},
    Entidade: { type: mongoose.Schema.Types.ObjectId,ref:'Entidade', required: true},
    TranscriParicaoMedico: { type: String, required: true },
    NumeroPortaria: { type: Number, required: true },
    Justificativa: { type: String, required: true },
});

MedProfSchema.plugin(autoIncrement.plugin, { model: 'ParecerMedico', field: '_id' });

const ParecerMedico = mongoose.model('ParecerMedico', MedProfSchema);

module.exports = ParecerMedico;