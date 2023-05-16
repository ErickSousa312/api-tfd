const Eleicao = require('../models/Eleicao')

class EleicaoController{
    async post(req,res){
        try {
            const{nomeEleicao, celular, hash}=req.body
            const eleicao = {
                nomeEleicao,
                celular,
                hash
            }
            console.log("hi2")
            await Eleicao.create(eleicao)
            res.status(201).json({msg:"Eleição criada com sucesso"})
        } catch (error) {
            res.status(500).json({msg: error})
        }
    }
    async get(req,res){
      Eleicao.find()
        .then((eleicao) => {
          res.status(201).json(eleicao);
        })
        .catch((err) => {
          console.error(err);
          res.status(500).json({ message: 'Erro ao buscar eleições' });
        });
    }
    async deleteId (req,res){
        const id = req.parms.id
        const eleicao = await Eleicao.findOne({_id:id})
        if (!eleicao) {
            res.status(422).json({ message: "Id não encontrado!" })
            return
        }
        try {
            await Eleicao.deleteOne({ _id: id })
            res.status(201).json({ msg: "Úsuario deletado" })
        } catch (error) {
            res.status(500).json({error})
        }
    }
    async getName(req, res) {
        try {
          const name = req.params.name;
          const resultadoEleicao = await Eleicao.find({ nomeEleicao: name }).exec();
          if (resultadoEleicao.length === 0) {
            res.status(404).json({ message: `Nenhuma eleição encontrada com o nome ${name}` });
          } else {
            res.status(200).json(resultadoEleicao);
          }
        } catch (error) {
          res.status(500).json({ error });
        }
      }
    async postVoto(req,res){
      try {
        
      } catch (error) {
        
      }
    }
      
}

module.exports = new EleicaoController();