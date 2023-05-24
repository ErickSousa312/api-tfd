const Funcionario = require('../models/Funcionario');

class FuncionarioController{
    async post(req,res){
        try {
            await Funcionario.create(req.body)
            .then((response)=>{
                res.status(201).json({msg:"Funcionario cadastrado com sucesso"})
            })
        } catch (error) {
            res.status(500).json({err: error})
        }
    }
    async get (req, res){
        try {
            const {id} = req.params
            await Funcionario.findOne({_id:id})
            .then((funcionario)=>{
                if(!funcionario){
                    res.status(404).json({msg:"Funcionario não encontrado"})
                }else{
                    res.status(200).json(funcionario)
                }
            })
        } catch (error) {
            res.status(500).json({err: error})
        }
    }
    async delete(req, res){
        try {
            const {id} = req.params
            await Funcionario.findOneAndDelete({_id:id},{new:true})
            .then((funcionario)=>{
                if(!funcionario){
                    res.status(404).json({msg:"Funcionario não encontrado"})
                }else{
                    res.status(201).json({msg:"Funcionario deletado com sucesso"})
                }
            })
        } catch (error) {
            res.status(500).json({err: error})
        }
    }
    async update(req,res){
        try {
            const {id} = req.params
            await Funcionario.findOneAndUpdate({_id:id},req.body,{new:true})
            .then((funcionario)=>{
                if(!funcionario){
                    res.status(404).json({msg:"Funcionario não encontrado"})
                }else{
                    res.status(201).json({msg:"Funcionario atualizado com sucesso"})
                }
            })
        } catch (error) {
            res.status(500).json({err: error})
        }
    }

}

module.exports = new FuncionarioController()