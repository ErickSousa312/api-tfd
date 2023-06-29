const Entidade = require('../models/Entidade')

const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

class ReportController{
    async get(req,res){

        const {id} = req.params
        await Entidade.findOne({_id : id})
        .then((entidade)=>{
            const entidadeJSON = JSON.stringify(entidade);
            const relatorioPath = path.join(__dirname, 'relatorio.pdf');
            const comando = `python src/pythonReports/reportEntidade.py ${entidadeJSON} ${relatorioPath}`;

            exec(comando, (error, stdout, stderr) => {
                if (error) {
                  console.error(`Erro ao executar o script Python: ${error}`);
                  return;
                }
                console.log(`Saída do script Python: ${stdout}`);
          
                // Ler o relatório gerado em PDF
                const relatorioPDF = fs.readFileSync(relatorioPath);
          
                // Enviar o relatório como resposta HTTP
                res.contentType('application/pdf');
                res.send(relatorioPDF);
          
                // Remover o arquivo temporário do relatório
                fs.unlinkSync(relatorioPath);
              });
        })    
    }
}

module.exports = new ReportController()