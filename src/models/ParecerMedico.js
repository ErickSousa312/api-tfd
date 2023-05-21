const mongoose = require('mongoose');

const MedProfSchema = new mongoose.Schema({
    ID: { type: Number, default: 1, required: true},
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

PacienteSchema.pre('save', async function(next) {
    if (!this.isNew) {
      return next();
    }
    const lastEntity = await Paciente.findOne({}, {}, { sort: { 'ID' : -1 } });
    if (lastEntity && lastEntity.ID) {
      this.ID = lastEntity.ID + 1;
    }
    next();
  });

const ParecerMedico = mongoose.model('ParecerMedico', MedProfSchema);

module.exports = ParecerMedico;