const mongoose = require('mongoose');
const autoIncrement = require('mongoose-auto-increment');

autoIncrement.initialize(mongoose.connection);

const EntidadeSchema = new mongoose.Schema({
    NomeEntidade: { type: String, required: true },
    Cidade: { type: String, required: true },
    Estado: { type: String, required: true },
    Especialidades: [{
        Nome: { type: String, required: true }
    }],
    
});

EntidadeSchema.plugin(autoIncrement.plugin, { model: 'Entidade', field: '_id' });

const Entidade = mongoose.model('Entidade', EntidadeSchema);

module.exports = Entidade;
