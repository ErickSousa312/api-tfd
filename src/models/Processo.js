const mongoose = require('mongoose');

const ProcessoSchema = new mongoose.Schema({
    IdPaciente: { type: mongoose.Schema.Types.ObjectId,ref:'Paciente', required: true},
    /*
        -NomePaciente
        -CPF
        -Idade
        -Endereço
        -Celular
        -Sexo
        -Menor de Idade
        -Acompanhante
    */
    DataViagem: { type: Number },
    DataAgendamento: { type: Date, required: true },
    PrevisaoRetorno: { type: Date, required: true },
    TipoAtendimento: { type: Number, required: true },
    Especialidade: { type: Number, required: true },
    IdFuncionario: { type: mongoose.Schema.Types.ObjectId,ref:'Funcionario', required: true},
    IdMedico: { type: mongoose.Schema.Types.ObjectId,ref:'MedProf', required: true},
    /*
        -Número CRM
    */
    Entidade: { type: mongoose.Schema.Types.ObjectId,ref:'Entidade', required: true},
    LocalOrigem: { type: String, required: true },
    CidadeDestino: { type: String, required: true },
    TipoDeslocamento: { type: String, required: true },
    EmpresaTransporte:{ type: String, required: true },
    TotalPassagem:{type:String, required: true},
    IdentTrajeto:{type: String, required: true},
    ObsAtendimento:{type: String, required: true},
    ObsPassagemAerea:{type: String, required: true},
    createdAt: { type: Date, default: Date.now }
});

EntidadeSchema.pre('save', async function(next) {
    const now = new Date()
    const year = now.getFullYear()
    const lastEntity = await Entidade.findOne({}, {}, { sort: { 'createdAt' : -1 } });
    let newCount = 1
    if (lastEntity && lastEntity.contador) {
        const [count, lastYear] = lastEntity.contador.split('/');
        if (Number(lastYear) === year) {
            newCount = Number(count) + 1;
        } else {
            newCount = 1; // Reinicia o contador para 1 se o ano for diferente
        }
    }
    const paddedCount = String(newCount) //caso queira numeros 0 antes use .padStart(4, '0')
    this.contador = `${paddedCount}/${year}`
    next();
});

const Processo = mongoose.model('Processo', ProcessoSchema);

module.exports = Processo;
