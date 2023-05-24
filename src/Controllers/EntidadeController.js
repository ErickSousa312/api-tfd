const Entidade = require('../models/Entidade')

class EntidadeController{
    async post(req, res){
        try {
            await Entidade.create(req.body)
            .then((response)=>{
                if(!response){
                    return res.status(400).json({msg: 'Entidade não foi cadastrada com sucesso'})
                }else{
                    return res.status(201).json({msg: "Entidade cadastrada com sucesso"})
                }
            })
        } catch (error) {
            return res.status(400).json({err: error})
        }
    }
    async get(req, res){
        try {
            const{id}= req.params
            await Entidade.find({_id: id})
            .then((response)=>{
                if(!response){
                    return res.status(404).json({err: "Entidade não encontrada"})
                }else{
                    return res.status(201).json(response)
                }
            })
        } catch (error) {
            return res.status(500).json({err: error})
        }
    }

    async delete(req,res){
        try {
            const {id} = req.params
            await Entidade.findOneAndDelete({_id: id}, {new:true})
            .then((response)=>{
                if(!response){
                    return res.status(404).json({err: "Entidade não encontrada"})
                }else{
                    return res.status(201).json({msg: "Entidade deletada com sucesso"})
                }
            })
        } catch (error) {
            return res.status(500).json({msg:"Erro ao deletar a Entidade",err: error})
        }
    }

    async update (req, res){
        try {
            const {id} = req.params
            await Entidade.findOneAndUpdate({_id:id}, req.body, {new:true})
            .then((response)=>{
                if(!response){
                    return res.status(404).json({err: "Entidade não encontrada"})
                }else{
                    return res.status(201).json({msg: "Entidade atualizada com sucesso"})
                }
            })
        } catch (error) {
            return res.status(500).json({msg:"Erro ao atualizar a Entidade",err: error})
        }
    }
}

module.exports = new EntidadeController()