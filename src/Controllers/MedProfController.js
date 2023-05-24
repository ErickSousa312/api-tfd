const MedProf = require('../models/MedProf')

class MedProfController {
    async post(req, res) {
        try {
            const {
                IdentProfissional,
                NomeCompleto,
                NumeroRegistro,
                UF,
                CPF,
                DataNascimento,
                Cargo,
                CodigoCBO,
                Especialidades,
                CentroDeSaude,
                DataCadastro,
                Afastamento
              }= req.body

            const medProf = {
                IdentProfissional,
                NomeCompleto,
                NumeroRegistro,
                UF,
                CPF,
                DataNascimento,
                Cargo,
                CodigoCBO,
                Especialidades,
                CentroDeSaude,
                DataCadastro,
                Afastamento
            }
            await MedProf.create(req.body)
            res.status(201).json({msg:"Médico ou profissional cadastrado com sucesso"})
        } catch (error) {
            res.status(500).json({err: error})
        }

    }
    async get (req,res){
        try {
            const {id} = req.params
            console.log(id)
            await MedProf.find({_id: id})
            .then((medProf)=>{
                if(!medProf){
                    return res.status(404).json({err:"Médico ou profissional não encontrado"})
                }else{
                    return res.status(201).json(medProf)
                }
            })
        } catch (error) {
            return res.status(500).json({err: error})
        }
    }
    async delete (req,res){
        try {
            const{id}= req.params
            await MedProf.findOneAndDelete({_id: id}, {new: true})
            .then((medProf)=>{
                if(!medProf){
                    return res.status(404).json({msg: "profissional não encontrado"})
                }else{
                    return res.status(201).json({msg: "profissional deletado com sucesso"})
                }
            })
        } catch (error) {
            return res.status(500).json({err: error})
        }
    }
    async update (req,res){
        try {
            const{id}= req.params
            await MedProf.findOneAndUpdate({_id: id}, req.body,{new:true})
            .then((medProf)=>{
                if(!medProf){
                    return res.status(404).json({msg: "profissional não encontrado"})
                }else{
                    return res.status(201).json({medProf})
                }
            })
        } catch (error) {
            return res.status(500).json({err: error})
        }
    }

}

module.exports = new MedProfController()