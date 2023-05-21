const mongoose = require('mongoose');

const AtendAssSocialSchema = new mongoose.Schema({
    _id: { type: Number, default: 1, required: true},
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

AtendAssSocialSchema.pre('save', async function(next) {
    if (!this.isNew) {
      return next();
    }
    const lastEntity = await AtendAssSocial.findOne({}, {}, { sort: { '_id' : -1 } });
    if (lastEntity && lastEntity._id) {
      this._id = lastEntity._id + 1;
    }
    next();
  });

const AtendAssSocial = mongoose.model('AtendAssSocial', AtendAssSocialSchema);

module.exports = AtendAssSocial;