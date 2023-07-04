const Processo = require('../models/Processo')

class ProcessoController {
    async post(req,res){
        try {
            await Processo.create(req.body)
            .then((response)=>{
                if(!response){
                    return res.status(400).json({msg:"Erro ao criar o processo"})
                }else{
                    return res.status(201).json({msg:"Processo criado com sucesso",data:response})
                }
            })
        } catch (error) {
            return res.status(400).json({msg:"Erro ao criar o processo",error:error})
        }
    }
    async get(req,res){
        try {
            const {id}= req.params
            console.log(id)
            await Processo.findOne({_id:"4/2023"}).populate('IdPaciente IdFuncionario IdMedico Entidade')
            .then((response)=>{
                console.log(response)
                if(!response){
                    return res.status(400).json({msg:"Processo não encontrado"})
                }else{
                    return res.status(200).json({msg:"Processo encontrado com sucesso",data:response})
                }
            })
        } catch (error) {
            return res.status(400).json({msg:"Erro ao buscar o processo",error:error})
        }
    }
    async delete(req,res){
        try {
            const {id} = req.params
            await Processo.findOneAndDelete({_id: id}, {new :true})
            .then((response)=>{
                if(!response){
                    return res.status(400).json({msg:"Erro ao deletar o processo"})
                }else{
                    return res.status(200).json({msg:"Processo deletado com sucesso",data:response})
                }
            })
        } catch (error) {
            return res.status(400).json({msg:"Erro ao deletar o processo",error:error})
        }
    }
    async update(req,res){
        try {
            const {id} = req.params
            await Processo.findOneAndUpdate({_id: id}, req.body, {new: true})
            .then((response)=>{
                if(!response){
                    return res.status(400).json({msg:"Erro ao atualizar o processo"})
                }else{
                    return res.status(200).json({msg:"Processo atualizado com sucesso",data:response})
                }
            })
        } catch (error) {
            return res.status(400).json({msg:"Erro ao atualizar o processo",error:error})
        }
    }
}

module.exports = new ProcessoController()