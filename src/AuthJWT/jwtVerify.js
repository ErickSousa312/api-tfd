const jwt = require('jsonwebtoken')
require('dotenv').config();

function jwtVerify(req,res){
    const headerToken = req.headers.authorization
    if(!headerToken){
        return res.status(401).send({error: 'Token não informado'})
    }
    const [typeToken, token] = headerToken.split(" ")
    jwt.verify(token, process.env.Secret, (err, decoded) => {
        if (err) {
            return res.status(401).json({msg:"Token Inválido", error: err})
          } else {
            req.userData = decoded
            return res.status(200).json({msg:'Token Válido', data: req.userData})
          }
    })
}

module.exports = jwtVerify