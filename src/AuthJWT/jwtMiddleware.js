const jwt = require('jsonwebtoken')
require('dotenv').config();

function jwtMiddleware(req,res, next){
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
            next();
          }
    })
}

module.exports = jwtMiddleware