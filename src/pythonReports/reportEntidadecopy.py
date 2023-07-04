import sys
import json
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate
from reportlab.platypus import Table, TableStyle
import textwrap

import os
# Dados do paciente
dados_paciente = {
        "_id": "4/2023",
        "IdPaciente": {
            "_id": 1,
            "DataNascimento": "16/06/2001",
            "numeroCPF": "12345678901",
            "orgaoEmissor": "SSP",
            "NumeroCartaoSUS": 987654321,
            "NumeroTituloEleitor": 12345,
            "UF": "SP",
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
            "UF":"PA",
            "CEP": "01234567",
            "Referencia": "Proximo a igreja bastista",
            "Celular": [
                {
                    "Numero": "987654321",
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
        "DataAgendamento": "2023-05-19T10:00:00.000Z",
        "PrevisaoRetorno": "2023-05-20T15:30:00.000Z",
        "TipoAtendimento": 1,
        "Especialidade": 2,
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
        "LocalOrigem": "Hospital ABC",
        "CidadeDestino": "São Paulo",
        "TipoDeslocamento": "Avião",
        "EmpresaTransporte": "Companhia Aérea XYZ",
        "TotalPassagem": "R$500,00",
        "IdentTrajeto": "ABC123XYZ",
        "ObsAtendimento": "Nesse exemplo, o texto será ajustado para caber na largura especificada usando a função textwrap fill. Em seguida, o texto ajustado é dividido em várias ",
        "ObsPassagemAerea": "Preferência por janela",
        "createdAt": "2023-05-19T19:12:42.910Z",
        "__v": 0
    }

def CentralizarTexto(text,fontSize,c):
    page_width, page_height = c._pagesize
    text_width = c.stringWidth(text, "Helvetica", fontSize)
    return (page_width - text_width) / 2
    
def AjustarTexto(texto, width2):
    texto_ajustado = textwrap.fill(texto, width=width2)
    print(texto_ajustado)
    # Divide o texto ajustado em várias linhas
    linhas = texto_ajustado.split('\n')
    print(linhas)
    return linhas

def gerar_relatorio_pdf(dados):
    caminho_completo = os.path.join(os.path.dirname(__file__), 'teste.pdf')
    # Configuração do documento PDF
    c = canvas.Canvas(caminho_completo, pagesize=A4)
    
    # Configurações dos retângulos
    rect_width = 400
    rect_height = 20
    rect_margin = 10
    rect_corner_radius = 5
    
#Cabeçalho
    c.roundRect(30, 773, 540, 50, rect_corner_radius, stroke=1, fill=0)
    image_path = os.path.join('src','pythonReports','images', 'brasao.png')
    c.drawImage(image_path, 35, 773, 45, 45, mask='auto')
    
    image_path = os.path.join('src','pythonReports','images', 'smsPrefeitura.png')
    c.drawImage(image_path, 450, 766, 120, 60, mask='auto')
    
    c.setFont("Helvetica-Bold", 10)
    text = "SECRETARIA MUNICIPAL DE SAÚDE DE MARABÁ"
    c.drawString(CentralizarTexto(text,10,c), 810, text)
    
    c.setFont("Helvetica-Bold", 8)
    text = "TRATAMENTO FORA DE COMICÍLIO - TFD"
    c.drawString(CentralizarTexto(text,8,c), 800, text)
    
    c.setFont("Helvetica", 7.5)
    text = "AGRÓPOLIS DO INCRA, SN - AMAPÁ MARABA/PA"
    c.drawString(CentralizarTexto(text,7.5,c), 790, text)
    
    c.setFont("Helvetica", 7.5)
    text = "CNPJ: 11.111.111/0001-11  INSC. EST:ISENTO"
    c.drawString(CentralizarTexto(text,7.5,c), 780, text)

#DADOS GERAIS
    # Label Principal
    c.saveState()  # Salva o estado atual do canvas
    c.setFillColorRGB(0.8, 0.8, 0.8)
    c.roundRect(155, 740, 280, rect_height, rect_corner_radius, stroke=1, fill=1)
    c.restoreState()  # Restaura o estado anterior do canvas
    c.setFont("Helvetica-Bold", 12)
    text = "PRONTO ATENDIMENTO"
    c.drawString(CentralizarTexto(text,12,c), 745, text)
    
    # Nome Paciente
    c.roundRect(30, 700, 330, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(35, 722, "Nome Paciente")
    c.setFont("Helvetica", 10)
    c.drawString(35, 707, str(dados['IdPaciente']['NomePaciente']))
    
    # Sexo
    c.roundRect(365, 700, 80, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(370, 722, "Sexo")
    c.setFont("Helvetica", 10)
    c.drawString(370, 707, str(dados['IdPaciente']['Sexo']))
    
    # Data de Nascimento
    c.roundRect(450, 700, 80, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(455, 722, "Data Nascimento")
    c.setFont("Helvetica", 10)
    c.drawString(455, 707, str(dados['IdPaciente']['DataNascimento']))
    
    # Idade
    c.roundRect(535, 700, 35, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(540, 722, "Idade")
    c.setFont("Helvetica", 10)
    c.drawString(540, 707, str(dados['IdPaciente']['Idade']))

    # Nome do Pai / Responsavel / Tutor(a)
    c.roundRect(30, 665, 270, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 687, "Nome do Pai / Responsavel / Tutor(a)")
    c.setFont("Helvetica", 10)
    c.drawString(35, 672, str(dados['IdPaciente']['NomePaiouResponsavel']))

    # Nome da Mãe
    c.roundRect(305, 665, 265, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(310, 687, "Nome da Mãe")
    c.setFont("Helvetica", 10)
    c.drawString(310, 672, str(dados['IdPaciente']['NomeMae']))
    
    # Endereço 
    c.roundRect(30, 630, 300, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 652, "Endereço")
    c.setFont("Helvetica", 10)
    c.drawString(35, 637, str(dados['IdPaciente']['Endereco']))
    
    # Nome da Mãe
    c.roundRect(335, 630, 235, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(340, 652, "Bairro")
    c.setFont("Helvetica", 10)
    c.drawString(340, 637, str(dados['IdPaciente']['Bairro']))
    
    # Município
    c.roundRect(30, 595, 150, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 617, "Município")
    c.setFont("Helvetica", 10)
    c.drawString(35, 602, str(dados['IdPaciente']['Cidade']))
    
    # UF
    c.roundRect(185, 595, 30, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(190, 617, "UF")
    c.setFont("Helvetica", 10)
    c.drawString(190, 602, str(dados['IdPaciente']['UF']))     
    
    # Telefone 1
    c.roundRect(220, 595, 100, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(225, 617, "Telefone 1")
    c.setFont("Helvetica", 10)
    c.drawString(225, 602, str(dados['IdPaciente']['Celular'][0]['Numero']))     

    # Telefone 2
    c.roundRect(325, 595, 100, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(330, 617, "Telefone 2")
    c.setFont("Helvetica", 10)
    c.drawString(330, 602, str(dados['IdPaciente']['Celular'][0]['Numero']))    
    
    # Cartão SUS
    c.roundRect(430, 595, 140, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(435, 617, "Cartão SUS")
    c.setFont("Helvetica", 10)
    c.drawString(435, 602, str(dados['IdPaciente']['NumeroCartaoSUS']))
    
    # Referencia
    c.roundRect(30, 560, 540, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 582, "Referência")
    c.setFont("Helvetica", 10)
    c.drawString(35, 567, str(dados['IdPaciente']['Referencia']))    
    
    # Observação
    c.roundRect(30, 505, 540, 40, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 547, "Observação")
    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str(dados['ObsAtendimento']), 120)
    y=534
    for linha in texto:
        c.drawString(35, y, str(linha))
        y -= 10
    
    #Label
    c.setFont("Helvetica-Bold", 9)
    c.drawString(35, 490,"Identificação do Profissional")
    
    # Motivo
    c.roundRect(30, 435, 540, 40, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 477, "Motivo(Principais Queixas)")
    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str(dados['ObsAtendimento']), 120)
    y=464
    for linha in texto:
        c.drawString(35, y, str(linha))
        y -= 10
 
    # diagnostico
    c.roundRect(30, 380, 540, 40, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 422, "Diagnóstico")
    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str(dados['ObsAtendimento']), 120)
    y=409
    for linha in texto:
        c.drawString(35, y, str(linha))
        y -= 10
    
    # diagnostico
    c.roundRect(30, 345, 370, 20, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 367, "Médico")
    c.setFont("Helvetica", 10)
    c.drawString(35, 352, str(dados['IdMedico']['NomeCompleto']))
    
    # diagnostico
    c.roundRect(405, 345, 165, 20, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(410, 367, "Especialidade")
    c.setFont("Helvetica", 10)
    c.drawString(410, 352, str(dados['IdMedico']['Especialidades'][0]['Nome']))
    
    # Fechar o arquivo PDF
    c.save()

#espaço entre os campos 35
#espaço entre os label e dados pequeno 15
#espaço entre os label e retangulo pequenos 22

#espaço entre os campos 42
#espaço entre os label e dados grande 18
#espaço entre os label e retangulo grande 22


# Ler os dados passados como argumento de linha de comando
print('PDF Gerado')

gerar_relatorio_pdf(dados_paciente)

