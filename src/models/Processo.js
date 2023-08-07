const mongoose = require('mongoose');

const ProcessoSchema = new mongoose.Schema({
    _id : {type:String, default: '1/2023', required: true},
    IdPaciente: { type: Number,ref:'Paciente', required: true},
    DataViagem: { type: Number },
    DataAgendamento: { type: Date, required: true },
    PrevisaoRetorno: { type: Date, required: true },
    TipoAtendimento: { type: Number, required: true },
    Especialidade: { type: Number, required: true },
    IdFuncionario: { type: Number,ref:'Funcionario', required: true},
    IdMedico: { type: Number,ref:'MedProf', required: true},
    Entidade: { type: Number,ref:'Entidade', required: true},
    LocalOrigem: { type: String, required: true },
    LocalAtendimento: {type:String, required: true},
    Destino: { type: String, required: true },
    TipoDeslocamento: { type: String, required: true },
    EmpresaTransporte:{ type: String, required: true },
    TotalPassagem:{
        ida:{type:Number, maxlength:3},
        volta:{type:Number, maxlength:3}
    },
    IdentTrajeto:{type: String, required: true},
    ObsAtendimento:{type: String, required: true},
    ObsPassagemAerea:{type: String, required: true},
    createdAt: { type: Date, default: Date.now }
});

ProcessoSchema.pre('save', async function(next) {
    const now = new Date()
    const year = now.getFullYear()
    const lastEntity = await Processo.findOne({}, {}, { sort: { 'createdAt' : -1 } });
    let newCount = 1
    if (lastEntity && lastEntity._id) {
        const [count, lastYear] = lastEntity._id.split('/');
        if (Number(lastYear) === year) {
            newCount = Number(count) + 1;
        } else {
            newCount = 1; // Reinicia o _id para 1 se o ano for diferente
        }
    }
    const paddedCount = String(newCount) //caso queira numeros 0 antes use .padStart(4, '0')
    this._id = `${paddedCount}/${year}`
    next();
});

const Processo = mongoose.model('Processo', ProcessoSchema);

module.exports = Processo;