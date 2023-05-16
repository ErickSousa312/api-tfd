const Eleicao = require('../models/Eleicao')

class ContVotoController{
    async post (req,res){
        try {
            const { opcao, idEleicao }=req.body
            Eleicao.findOneAndUpdate({_id: idEleicao, 'opcoes.chave': opcao},
            { $inc: { 'opcoes.$.valor': 1 } },
            { new: true })
            .then((data)=>{
                res.status(200).json(data)
            })

        } catch (error) {
            
        }
    }
}

module.exports = new ContVotoController();