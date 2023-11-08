const mongoose = require('mongoose');

const MedProfSchema = new mongoose.Schema({
    _id: { type: Number, default: 1, required: true},
    IdentProfissional: { type: Number, required: true },
    NomeCompleto: { type: String, required: true },
    NumeroRegistro: { type: Number, required: true },
    UF: { type: String, required: true, maxlength: 2},
    CPF: { type: String, required: true },
    DataNascimento: { type: String, required: true },
    Cargo: { type: String, required: true},
    CodigoCBO: { type: String, required: true },
    Especialidades: [{
        Nome: { type: String }
    }],
    CentroDeSaude: { type: String, required: true },
    DataCadastro: { type: String, required: true },
    Afastamento: { type: String }
});

MedProfSchema.pre('save', async function(next) {
    if (!this.isNew) {
      return next();
    }
    const lastEntity = await MedProf.findOne();
    if (lastEntity && lastEntity._id) {
      this._id = lastEntity._id + 1;
    }
    next();
});

const MedProf = mongoose.model('MedProf', MedProfSchema);

module.exports = MedProf;