const AtendAssSocial = require('../models/AtendAssSocial')

class AtendAssSocialController{
    async post(req, res){
        try {
            await AtendAssSocial.create(req.body)
            .then((response) => {
                if (!response) {
                  return res.status(400).json({msg: 'Atendimento não foi cadastrada com sucesso'})
                } else {
                  return res.status(201).json({ msg: 'Atendimento cadastrado com sucesso' });
                }
              })
              
        } catch (error) {
            return res.status(400).json({err: error})
        }
    }
    async get(req, res){
        try {
            const {id} = req.params
            await AtendAssSocial.find({_id: id})
            .then((atendAssSocial)=>{
                if(!atendAssSocial){
                    return res.status(404).json({msg:"Atendimento não encontrado"})
                }else{
                    return res.status(201).json(atendAssSocial)
                }
            })
        } catch (error) {
            return res.status(500).json({err: error})
        }
    }
    async delete(req,res){
        try {
            const {id} = req.params
            await AtendAssSocial.findOneAndDelete({_id:id}, {new:true})
            .then((atendAssSocial)=>{
                if(!atendAssSocial){
                    return res.status(404).json({msg:"Atendimento não encontrado"})
                }else{
                    return res.status(201).json({msg:"Atendimento deletado com sucesso"})
                }
            })
        } catch (error) {
            return res.status(500).json({err: error})
        }
    }
    async update(req,res){
        try {
            const{id}= req.params
            await AtendAssSocial.findOneAndUpdate({_id: id},req.body, {new:true})
            .then((atendAssSocial)=>{
                if(!atendAssSocial){
                    return res.status(404).json({msg:"Atendimento não encontrado"})
                }else{
                    return res.status(201).json({msg:"Atendimento atualizado com sucesso"})
                }
            })
        } catch (error) {
            return res.status(500).json({err: error})
        }
    }

}

module.exports = new AtendAssSocialController()