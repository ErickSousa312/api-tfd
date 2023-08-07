const mongoose = require('mongoose');

const EntidadeSchema = new mongoose.Schema({
    _id: { type: Number, default: 1, required: true},
    NomeEntidade: { type: String, required: true },
    Cidade: { type: String, required: true },
    Estado: { type: String, required: true },
    Especialidades: [{
        Nome: { type: String, required: true }
    }],
});

EntidadeSchema.pre('save', async function(next) {
    if (!this.isNew) {
      return next();
    }
    const lastEntity = await Entidade.findOne({}, {}, { sort: { '_id' : -1 } });
    if (lastEntity && lastEntity._id) {
      this._id = lastEntity._id + 1;
    }
    next();
  });

const Entidade = mongoose.model('Entidade', EntidadeSchema);

module.exports = Entidade;