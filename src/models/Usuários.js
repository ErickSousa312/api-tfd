const mongoose = require('mongoose')

const UsuarioSchema = new mongoose.Schema(
    {
        _id: {type: Number, default:1, required: true},
        userName:{type: String, required: true},
        password:{type: String, required: true},
    }
)

UsuarioSchema.pre('save', async function(next) {
    if (!this.isNew) {
      return next();
    }
    const lastEntity = await Usuario.findOne({}, {}, { sort: { '_id' : -1 } });
    if (lastEntity && lastEntity._id) {
      this._id = lastEntity._id + 1;
    }
    next();
});

const Usuario = mongoose.model('Usuario', UsuarioSchema)

module.exports = Usuario