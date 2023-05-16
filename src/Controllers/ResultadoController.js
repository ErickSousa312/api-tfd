const ResultadoEleicao = require('../models/Resultadoeleicao')

class ResultadoController {
    async post (req,res){
        try {
            const {eleicao,email, voto, hash} = req.body
            const Voto = {
                eleicao,
                email,
                voto,
                hash
            }
            console.log(Voto)
            await ResultadoEleicao.create(Voto),
            res.status(201).json({msg:"Voto Registrado"})
        } catch (error){
            res.status(500).json({msg: error})
        }
    }
    async get(req, res) {
        try {
            ResultadoEleicao.find()
                .populate('eleicao')
                .exec((err, eleicoes) => {
                    if (err) {
                        res.status(400).json({ message: `${err.message} - Id da eleição não localizado` })
                    } else {
                        res.status(200).json(eleicoes)
                    }
                })
        } catch (error) {
            res.status(500).json({ msg: error })
        }
    }
    async getName(req, res) {
        try {
            const name = req.params.name;
            ResultadoEleicao.find({'nomeEleicao': name})
            .populate({
                path: 'eleicao',
                match: { nomeEleicao: name }
            })
            .exec((err, resultadoEleicao) => {
                if (err) {
                    res.status(400).json({ message: `${err.message} - Erro ao buscar resultados de eleição` })
                } else {
                    const data =  resultadoEleicao.filter((resultado) => resultado.eleicao !== null)
                    res.status(200).json(data)
                }
            });

        } catch (error) {
            res.status(500).json({ msg: error })
        }
    }
}

module.exports = new ResultadoController();