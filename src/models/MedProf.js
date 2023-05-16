const mongoose = require('mongoose');
const autoIncrement = require('mongoose-auto-increment');

autoIncrement.initialize(mongoose.connection);

const MedProfSchema = new mongoose.Schema({
    IdentProfissional: { type: Number, required: true },
    NomeCompleto: { type: String, required: true },
    NumeroRegistro: { type: Number, required: true },
    UF: { type: Number, required: true, maxlength: 2},
    CPF: { type: String, required: true },
    DataNascimento: { type: String, required: true },
    Cargo: { type: String, required: true},
    CodigoCBO: { type: String, required: true },
    Especialidades: [{
        Nome: { type: String, required: true }
    }],
    DataNascimento: { type: String, required: true },
    CentroDeSaude: { type: String, required: true },
    DataCadastro: { type: String, required: true },
    Afastamento: { type: String }
});

MedProfSchema.plugin(autoIncrement.plugin, { model: 'MedProf', field: '_id' });

const MedProf = mongoose.model('MedProf', MedProfSchema);

module.exports = MedProf;