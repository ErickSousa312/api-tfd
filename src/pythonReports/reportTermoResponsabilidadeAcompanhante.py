import sys
import json
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate
from reportlab.platypus import Table, TableStyle
import textwrap
import datetime
import locale

import os
# Dados do paciente
dados_paciente = {
    "_id": "4/2023",
    "IdPaciente": {
        "_id": 1,
        "DataNascimento": "16/06/2001",
        "NumeroCPF": "123.456.789-01",
        "NumeroRG": "8260336",
        "OrgaoEmissor": "SSP",
        "NumeroCartaoSUS": "124.2541.2548.2415",
        "NumeroTituloEleitor": 12345,
        "eleitorUF": "SP",
        "NomePaciente": "João da Silva",
        "NomeSocial": "",
        "Sexo": "Masculino",
        "Idade": 32,
        "Sangue": "O+",
        "DataCadastro": "2023-05-17T00:00:00.000Z",
        "NomePaiouResponsavel": "",
        "NomeMae": "Maria Oliveira",
        "EstadoCivil": "Solteiro(a)",
        "Endereco": "Rua das Flores, 123",
        "Bairro": "Centro",
        "Cidade": "Marabá",
        "UF": "PA",
        "CEP": "01234567",
        "Referencia": "Proximo a igreja bastista",
        "Celular": [
                {
                    "Numero": "987654321",
                    "_id": "6464f2a90d7165b8d1a1a4b7"
                }
        ],
        "Acompanhantes": [
            {
                "nomeAcompanhante": "Maria Oliveira do Carmo de Sandra Oliveira",
                "NumeroCPF": "123.456.789-01",
                "NumeroRG": "8260336",
                "DataNascimento": "16/06/2001",
                "Endereco": "Rua das Flores, 123",
                "Bairro": "Centro",
                "Cidade": "Marabá",
                "UF": "PA",
                "CEP": "01234567",
                "Referencia": "Proximo a igreja bastista",
                "_id": "6464f2a90d7165b8d1a1a4b7"
            }
        ],
        "Email": "joao.silva@example.com",
        "identZona": "Zona Urbana",
        "TratamentoAtual": "Tratamento X",
        "Ocupacao": "Engenheiro",
        "GrauEstudo": "Ensino Superior",
        "Conta": 12345,
        "__v": 0
    },
    "DataViagem": 1654321000,
    "DataAgendamento": "01/12/2023",
    "PrevisaoRetorno": "20/12/2023",
    "TipoAtendimento": "consulta-médica",
    "Especialidade": "Oftamologista",
    "IdFuncionario": {
        "_id": 2,
        "nomeFuncionario": "Nome do Funcionário",
        "CPF": "123.456.789-00",
        "Rg": 1234567,
        "NumeroMatricula": 98765,
        "NumeroPortaria": 54321,
        "Cidade": "Nome da Cidade",
        "UfCidade": "UF",
        "CEP": "12345-678",
        "Celular": [
            {
                    "Numero": 987654321,
                    "_id": "64663989bf820c51ec10e485"
            },
            {
                "Numero": 123456789,
                "_id": "64663989bf820c51ec10e486"
            }
        ],
        "AtividadeExercida": "Atividade",
        "DataNascimento": "01/01/1990",
        "CentroDeSaude": "Nome do Centro de Saúde",
        "DataCadastro": "01/01/2023",
        "Observação": "Observação sobre o funcionário",
        "__v": 0
    },
    "IdMedico": {
        "_id": 2,
        "IdentProfissional": 54321,
        "NomeCompleto": "Samuel garcias de sousa",
        "NumeroRegistro": 98765,
        "UF": 34,
        "CPF": "987.654.321-00",
        "DataNascimento": "02/02/1995",
        "Cargo": "Enfermeiro",
        "CodigoCBO": "654321",
        "Especialidades": [
                {
                    "Nome": "Pneumologia",
                    "_id": "646622179fa83c663aa1feeb"
                },
            {
                    "Nome": "Especialidade 4",
                    "_id": "646622179fa83c663aa1feec"
                    }
        ],
        "CentroDeSaude": "Outro Centro de Saúde",
        "DataCadastro": "02/02/2023",
        "Afastamento": "Motivo de afastamento",
        "__v": 0
    },
    "Entidade": {
        "_id": 2,
        "NomeEntidade": "Nome da Entidade 2",
        "Cidade": "Cidade 2",
        "Estado": "Estado 2",
        "Especialidades": [
                {
                    "Nome": "Especialidade 3",
                    "_id": "64666c2b5ef03f00b39f2033"
                },
            {
                    "Nome": "Especialidade 4",
                    "_id": "64666c2b5ef03f00b39f2034"
            }
        ],
        "__v": 0
    },
    "LocalOrigem": "Marabá",
    "LocalAtendimento": "hiroshi Matsuda",
    "Destino": "São Paulo",
    "TipoDeslocamento": "UTI Terrestre",
    "EmpresaTransporte": "Companhia Aérea XYZ",
    "TotalPassagem": {
        "ida": 2,
        "volta": 2
    },
    "IdentTrajeto": "ABC123XYZ",
    "ObsAtendimento": "Nesse exemplo, o texto será ajustado para caber na largura especificada usando a função textwrap fill. Em seguida, o texto ajustado é dividido em várias ",
    "ObsPassagemAerea": "Preferência por janela",
    "createdAt": "2023-05-19T19:12:42.910Z",
    "__v": 0
}


def CentralizarTexto(text, fontSize, c):
    page_width, page_height = c._pagesize
    text_width = c.stringWidth(text, "Helvetica", fontSize)
    return (page_width - text_width) / 2


def AjustarTexto(texto, width2):
    texto_ajustado = textwrap.fill(texto, width=width2)
    # Divide o texto ajustado em várias linhas
    linhas = texto_ajustado.split('\n')
    return linhas

# alinha o nome da pessoa a linha de assinatura na parte inferior do documento


def alinharAssinatura(texto, rect_x, rect_width, c):
    text_width = c.stringWidth(texto, "Helvetica-Bold", 6)
    x = rect_x + (rect_width - text_width) / 2
    return x


# Aqui inicia a função que gera dados
def gerar_relatorio_pdf(dados):
    caminho_completo = os.path.join(os.path.dirname(
        __file__), 'Termo de Responsabilidade Acompanhante.pdf')
    # Configuração do documento PDF
    c = canvas.Canvas(caminho_completo, pagesize=A4)

    # Configurar o idioma para português brasileiro
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

    # Configurações dos retângulos e data
    rect_width = 400
    rect_height = 14
    rect_margin = 10
    rect_corner_radius = 5
    data_atual = datetime.date.today()
    data_formatada = data_atual.strftime("%d de %B de %Y")
    data_formatada_numero = data_atual.strftime("%d/%m/%Y")


# Cabeçalho
    c.roundRect(30, 773, 540, 50, rect_corner_radius, stroke=1, fill=0)
    image_path = os.path.join('src', 'pythonReports', 'images', 'brasao.png')
    c.drawImage(image_path, 35, 773, 45, 45, mask='auto')

    image_path = os.path.join('src', 'pythonReports',
                              'images', 'smsPrefeitura.png')
    c.drawImage(image_path, 450, 766, 120, 60, mask='auto')

    c.setFont("Helvetica-Bold", 10)
    text = "SECRETARIA MUNICIPAL DE SAÚDE DE MARABÁ"
    c.drawString(CentralizarTexto(text, 10, c), 810, text)

    c.setFont("Helvetica-Bold", 8)
    text = "TRATAMENTO FORA DE COMICÍLIO - TFD"
    c.drawString(CentralizarTexto(text, 8, c), 800, text)

    c.setFont("Helvetica", 7.5)
    text = "AGRÓPOLIS DO INCRA, SN - AMAPÁ MARABA/PA"
    c.drawString(CentralizarTexto(text, 7.5, c), 790, text)

    c.setFont("Helvetica", 7.5)
    text = "CNPJ: 11.111.111/0001-11  INSC. EST:ISENTO"
    c.drawString(CentralizarTexto(text, 7.5, c), 780, text)

# DADOS GERAIS
    # Label Principal
    # c.saveState()  # Salva o estado atual do canvas
    # c.setFillColorRGB(0.8, 0.8, 0.8)
    c.rect(165, 741, 280, 0.9, stroke=0, fill=1)

    # c.restoreState()  # Restaura o estado anterior do canvas

    c.setFont("Helvetica-Bold", 12)
    text = "Termo de Responsabilidade do Acompanhante"
    c.drawString(CentralizarTexto(text, 12, c), 745, text)

    # 14 entre paragrafos
    # 11 entre linhas

    # Declaro que recebi...
    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str(f"                 Eu, {dados['IdPaciente']['Acompanhantes'][0]['nomeAcompanhante']}, nascido(a) em {dados['IdPaciente']['Acompanhantes'][0]['DataNascimento']}, \
                            CPF Nº {dados['IdPaciente']['Acompanhantes'][0]['NumeroCPF']} e residente(a) à {dados['IdPaciente']['Acompanhantes'][0]['Endereco']} - {dados['IdPaciente']['Acompanhantes'][0]['Bairro']} {dados['IdPaciente']['Acompanhantes'][0]['Cidade']} / {dados['IdPaciente']['Acompanhantes'][0]['UF']} CEP: {dados['IdPaciente']['Acompanhantes'][0]['CEP']} - \
{dados['IdPaciente']['Acompanhantes'][0]['Bairro']} \
                            "), 120)
    y = 689
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    c.setFont("Helvetica", 10)
    c.drawString(
        50, 650, f"Domiciliado(a) no município de {dados['IdPaciente']['Acompanhantes'][0]['Cidade']} / {dados['IdPaciente']['Acompanhantes'][0]['UF']}.")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str(f"Portador do RG nº {dados['IdPaciente']['Acompanhantes'][0]['NumeroRG']}, venho de livre e espontânea vontade assumir o compromisso de\
                            acompanhar o paciente {dados['IdPaciente']['NomePaciente']}, Processo nº {dados['_id']}. \
                            "), 120)
    y = 622
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str(f"                 Comprometendo-me a prestar completa assistência durante todo o seu tratamento assim\
                            como, não desistir deste compromisso em hipótese alguma. \
                            "), 120)
    y = 583
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str(f"                 Deverei também, comparecer ao serviço de TFD do município de Marabá-PA, munido do\
                            processo, para receber orientações quanto ao tratamento do paciente e quando ocorrer qualquer \
                            intercorrências. \
                            "), 120)
    y = 544
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str(f"                 OBS: A troca do acompanhante só será permitida, mediante necessidade extrema e com justificativa por\
                            escrito e após avaliação do Assistente Social do TFD. \
                            "), 120)
    y = 494
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    # 14 entre paragrafos
    # 11 entre linhas

    # Fechar o arquivo PDF
    c.save()


# Ler os dados passados como argumento de linha de comando
print('PDF Gerado')

gerar_relatorio_pdf(dados_paciente)
