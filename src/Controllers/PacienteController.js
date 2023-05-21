const Paciente = require('../models/paciente')

class PacienteControler{

    async post(req, res){
        try {
            const {DataNascimento, numeroCPF, orgaoEmissor, NumeroCartaoSUS, NumeroTituloEleitor, UF
                 , NomePaciente, NomeSocial, Sexo, Idade, Sangue, DataCadastro, NomePaiouResponsavel,
                NomeMae, EstadoCivil, Endereco, Bairro, UfCidade, CEP, Celular, Email, identZona,
                TratamentoAtual, Ocupacao, GrauEstudo, Conta}=req.body

            const paciente = {
                DataNascimento, numeroCPF, orgaoEmissor, NumeroCartaoSUS, NumeroTituloEleitor, UF
                 , NomePaciente, NomeSocial, Sexo, Idade, Sangue, DataCadastro, NomePaiouResponsavel,
                NomeMae, EstadoCivil, Endereco, Bairro, UfCidade, CEP, Celular, Email, identZona,
                TratamentoAtual, Ocupacao, GrauEstudo, Conta
            }
            console.log(paciente)
            await Paciente.create(paciente)
            .then(res.status(201).json({msg: "Paciente Cadastrado com sucesso"}))
        } catch (error) {
            return res.status(400).json({err: error})
        }
    }

    async get (req,res){
        try {
            const {id}=req.params
            Paciente.find({_id: id})
            .then((paciente)=>{
                return res.status(200).json(paciente)
            })
        } catch (error) {
            return res.status(400).json({err: error})
        }
    }

    async delete (req,res){
        try {
            const{id}= req.params
            await Paciente.findOneAndDelete({_id: id}, {new:true})
            .then((paciente)=>{
                if(!paciente){
                    return res.status(404).json({msg: "Paciente não encontrado"})
                }else{
                    return res.status(200).json({msg: "Paciente deletado com sucesso"})
                }
            })
        } catch (error) {
            return res.status(500).json({err: error})
        }
    }

    async update(req,res){
        try {
            const{id} = req.params
            await Paciente.findOneAndUpdate({_id: id}, req.body, {new: true})
            .then((paciente)=>{
                if(!paciente){
                    return res.status(404).json({msg: "paciente não encontrado"})
                }else{
                    return res.status(201).json(paciente)
                }
            })
            
        } catch (error) {
            return res.status(500).json({err: error})
        }
    }

}

module.exports = new PacienteControler()