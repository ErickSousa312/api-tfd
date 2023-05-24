const ParecerMedico = require('../models/ParecerMedico')

class ParecerMedicoController {

    async post(req, res) {
        try {
            await ParecerMedico.create(req.body)
                .then((response) => {
                    if (!response) {
                        return res.status(400).json({ msg: "Erro ao criar Parecer Médico" })
                    } else {
                        return res.status(201).json({ msg: "Parece Médico criado com sucesso", data: response })
                    }
                })
        } catch (error) {
            return res.status(400).json({ msg: 'Erro ao criar o parecer médico', error: error });
        }
    }

    async get(req, res) {
        try {
            const { id } = req.params;
            await ParecerMedico.find({_id: id})
            .then((response) => {
                if (!response) {
                  return res.status(404).json({ msg: 'Parecer médico não encontrado' });
                }
                return res.status(200).json({ msg: 'Parecer médico encontrado com sucesso', data: response });
              })
        } catch (error) {
            return res.status(400).json({ msg: 'Erro ao buscar o parecer médico', error: error });
        }
    }

    async delete(req,res){
        try {
            const {id} = req.parms
            await ParecerMedico.findOneAndDelete({_id: id}, {new :true})
            .then((response)=>{
                if(!response){
                    return res.status(400).json({msg:"Erro ao deletar o Parecer Medico"})
                }else{
                    return res.status(200).json({msg:"Parecer Medico deletado com sucesso",data:response})
                }
            })
        } catch (error) {
            return res.status(400).json({msg:"Erro ao deletar o Parecer Medico",error:error})
        }
    }

    async update(req,res){
        try {
            const {id} = req.parms
            await ParecerMedico.findOneAndUpdate({_id: id}, req.body, {new: true})
            .then((response)=>{
                if(!response){
                    return res.status(400).json({msg:"Erro ao atualizar o Parecer Medico"})
                }else{
                    return res.status(200).json({msg:"Parecer Medico atualizado com sucesso",data:response})
                }
            })
        } catch (error) {
            return res.status(400).json({msg:"Erro ao atualizar o Parecer Medico",error:error})
        }
    }
}