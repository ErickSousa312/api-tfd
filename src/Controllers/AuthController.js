const bcrypt = require('bcrypt')
const jwt = require('jsonwebtoken')
require('dotenv').config();
const Usuario = require('../models/Usuários')

class UsuarioController{
    async signUp (req, res){
         const {userName, password, root} = req.body
         console.log(userName, password)
         try {
            await Usuario.findOne({userName:userName})
            .then((response)=>{
                if(response){
                    return res.status(409).json({ error: 'O usuário já existe' });
                }else{
                    bcrypt.hash(password, 10, async (err, hash) => {
                        const usuario={
                            userName,
                            password: hash
                        }
                        await Usuario.create(usuario)
                        .then((response)=>{
                            if(!response){
                                return res.status(400).json({msg:"Erro ao registrar  Usuario"})
                            }else{
                                res.status(201).json({ msg: 'Usuário registrado com sucesso' });
                            }
                        })
                    })
                }
            })
         } catch (error) {
            return res.status(400).json({msg:"Erro ao cadastrar Usuario", err: error})
         }
    }
    async signIn(req, res){
        const {userName, password} = req.body
        try {
            await Usuario.findOne({userName: userName})
            .then((response)=>{
                if(!response){
                    return res.status(401).json({ error: 'Credenciais inválidas' }); 
                }else{
                    bcrypt.compare(password, response.password, (err, isPasswordValid) => {
                        if (!isPasswordValid) {
                            return res.status(401).json({ msg: 'Credenciais inválidas' , error:err});
                        }else{
                            jwt.sign({ userId: response._id, userName: response.userName }, process.env.Secret, (err, token)=>{
                                if(err){
                                    return res.status(400).json({msg:"Erro ao gerar token"})
                                }else{
                                    return res.status(201).json({token})
                                }
                            });
                        }
                    })
                }
            })
        } catch (error) {
            res.status(500).json({ msg: 'Erro interno do servidor', err: error });
        }
    }
}

module.exports = new UsuarioController()