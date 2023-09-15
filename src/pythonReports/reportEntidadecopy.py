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
            "NumeroRG" : "8260336",
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
            "UF":"PA",
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

def ViaDeTransporteX(tipo):
    if tipo == "Rodoviário":
        x = 37
        y = 328
        return x,y
    elif tipo == "Aéreo":
        x = 37
        y = 315
        return x,y
    elif tipo == "Ambulância":
        x = 112
        y = 328
        return x,y
    elif tipo == "Ferroviário":
        x = 112
        y = 315
        return x,y
    elif tipo == "UTI Aérea":
        x = 187
        y = 328
        return x,y
    elif tipo == "UTI Terrestre":
        x = 187
        y = 315
        return x,y
    # elif tipo == 3:
    #     # código para o caso 3
    # else:
    #     # código para casos não tratados

def CentralizarTexto(text,fontSize,c):
    page_width, page_height = c._pagesize
    text_width = c.stringWidth(text, "Helvetica", fontSize)
    return (page_width - text_width) / 2
    
def AjustarTexto(texto, width2):
    texto_ajustado = textwrap.fill(texto, width=width2)
    # Divide o texto ajustado em várias linhas
    linhas = texto_ajustado.split('\n')
    return linhas

# alinha o nome da pessoa a linha de assinatura na parte inferior do documento
def alinharAssinatura(texto,rect_x, rect_width , c):
    text_width = c.stringWidth(texto, "Helvetica-Bold", 6)
    x = rect_x + (rect_width - text_width) / 2
    return x


#Aqui inicia a função que gera dados
def gerar_relatorio_pdf(dados):
    caminho_completo = os.path.join(os.path.dirname(__file__), 'teste.pdf')
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
    #c.saveState()  # Salva o estado atual do canvas
    #c.setFillColorRGB(0.8, 0.8, 0.8)
    c.rect(220, 741, 160, 0.9, stroke=0, fill=1)
    
    #c.restoreState()  # Restaura o estado anterior do canvas
    
    c.setFont("Helvetica-Bold", 12)
    text = "Declaração de Passagem"
    c.drawString(CentralizarTexto(text,12,c), 745, text)
    
    #14 entre paragrafos
    #11 entre linhas
    
    #Declaro que recebi...
    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("              Declaro que recebi da Secretaria Municipal de Saúde de Maraba, passagens abaixo relacionadas,\
 referenrentes ao auxilio para tratamento fora do domicilio. Declaro também, ter ciência que as mesmas somente\
 deverão ser utilizadas de acordo com as normas estabalecidas pelo Programa de de Tratamento Fora de Domicilio-TFD.\
     "), 120)
    y=726
    for linha in texto:
        c.drawString(30, y, str(linha))
        y -= 11
    #negrito Passagem só serão...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(30,693,"As passagens só serão liberadas na agência de viagem, no horário comercial de segunda a sexta-feira.")
    
    #14 entre paragrafos
    #11 entre linhas
    
    #E que n poderei....
    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("              E que não poderei realizar qualquer tipo de exame ou consulta particular mesmo que solicitado por médico da rede SUS,\
 visando pagamento posterior via Secretaria Municipal de Saúde/TFD, pois as normas do TFD não permitem pagamento de tais procedimentos particulares.\
 "), 120)
    y=679
    for linha in texto:
        c.drawString(30, y, str(linha))
        y -= 11
    
    # São vetados...
    c.setFont("Helvetica-Bold",10)
    c.drawString(30, 646, "São VETADOS no tratamento Fora de Domicilio nas seguintes situações:")
    
    #14 entre paragrafos
    #11 entre linhas
    
    #Tipos de regras...
    c.setFont("Helvetica",10)
    c.drawString(55, 632, "- A transferência de passagens para terceiros ou revender;")
    
    c.setFont("Helvetica",10)
    c.drawString(55, 621, "- Receber passagens na agências após a data do atendimento;")
    
    c.setFont("Helvetica",10)
    c.drawString(55, 610, "- Receber passagens nas agências/empresa de transporte fora do horário comercial;")
    c.setFont("Helvetica-Bold",10)
    c.drawString(435, 610, "(APÓS AS 18H, AOS ")
    c.drawString(55,599,"SÁBADOS, DOMINGOS E FERIADOS)")
    c.setFont("Helvetica",10)
    c.drawString(55, 588, "")
    
    #14 entre paragrafos
    #11 entre linhas
    
    # A Permanência da capital sem estar...
    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("- A permanência na capital sem estar realizando consultas e procedimentos médicos\
 previamente autorizados pelo TFD de Maraba-PA, através do SUS, sendo ques as consultas \
 deverão ter as devidas anotações no processo Ficando na responsabilidade do paciente/familia as\
 despesas com estadia e alimentação do paciente/acompanhante."), 110)
    y=588
    for linha in texto:
        c.drawString(55, y, str(linha))
        y -= 11
    
    
    # Dados do Paciente --------------------------------------------------------------------------
    c.saveState()  # Salva o estado atual do canvas
    c.setFillColorRGB(0.8, 0.8, 0.8)
    c.roundRect(30, 532, 540, rect_height, rect_corner_radius, stroke=1, fill=1)
    c.restoreState()  # Restaura o estado anterior do canvas
    c.setFont("Helvetica-Bold", 12)
    c.drawString(CentralizarTexto("Dados do Paciente", 12, c), 535, "Dados do Paciente")

    # Nome Paciente
    c.setLineWidth(0.7)
    c.roundRect(30, 506, 370, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 521, "Nome do Paciente")
    c.setFont("Helvetica", 9)
    c.drawString(35, 510, str(dados['IdPaciente']['NomePaciente']))

    # Numero do Processo TFD
    c.roundRect(405, 506, 165, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(410, 521, "N° do Processo TFD")
    c.setFont("Helvetica-Bold", 9)
    c.drawString(410, 510, str(dados['_id']))

    # N° do RG
    c.roundRect(30, 482, 70, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 497, "N° do RG")
    c.setFont("Helvetica", 9)
    c.drawString(35, 486, str(dados['IdPaciente']['NumeroRG']))

    # Numero CPF
    c.roundRect(105, 482, 110, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(110, 497, "N° do CPF")
    c.setFont("Helvetica", 9)
    c.drawString(110, 486, str(dados['IdPaciente']['NumeroCPF']))

    # Data de Nascimento
    c.roundRect(220, 482, 100, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(225, 497, "Data de Nascimento")
    c.setFont("Helvetica", 9)
    c.drawString(225, 486, str(dados['IdPaciente']['DataNascimento']))

    # N° telefone 1
    c.roundRect(325, 482, 120, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(330, 497, "telefone 1")
    c.setFont("Helvetica", 9)
    c.drawString(330, 486, str(dados['IdPaciente']['Celular'][0]['Numero']))

    # N° telefone 2
    c.roundRect(450, 482, 120, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(455, 497, "telefone 2")
    c.setFont("Helvetica", 9)
    c.drawString(455, 486, str(dados['IdPaciente']['Celular'][0]['Numero']))

    # Volcher paciente
    c.roundRect(30, 458, 320, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 473, "N° Volcher(S) do Paciente")
    c.setFont("Helvetica", 9)
    c.drawString(35, 462, str())

    # Numero do cartão sus
    c.roundRect(355, 458, 215, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(360, 473, "N° Cartão SUS")
    c.setFont("Helvetica-Bold", 9)
    c.drawString(360, 462, str(dados['IdPaciente']['NumeroCartaoSUS']))

    # Nome do acompanhante
    c.roundRect(30, 434, 540, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 449, "Nome do acompanhante")
    c.setFont("Helvetica", 9)
    c.drawString(35, 438, str(dados['IdPaciente']['Acompanhantes'][0]['nomeAcompanhante']))

    # Numero do rg Acomp
    c.roundRect(30, 410, 115, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 425, "Numero RG(Acompanhante)")
    c.setFont("Helvetica", 9)
    c.drawString(35, 414, str(dados['IdPaciente']['Acompanhantes'][0]['NumeroRG']))

    # Numero do CPF Acomp
    c.roundRect(150, 410, 90, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(155, 425, "N° do CPF")
    c.setFont("Helvetica", 9)
    c.drawString(155, 414, str(dados['IdPaciente']['Acompanhantes'][0]['NumeroCPF']))

    # Data Nascimento
    c.roundRect(245, 410, 105, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(250, 425, "Data Nascimento")
    c.setFont("Helvetica", 9)
    c.drawString(250, 414, str(dados['IdPaciente']['Acompanhantes'][0]['NumeroCPF']))

    # Numero do Cartão SUS Acompanhante
    c.roundRect(355, 410, 215, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(360, 425, "N° do Cartão SUS do Acompanhante")
    c.setFont("Helvetica-Bold", 9)
    c.drawString(360, 414, str(dados['IdPaciente']['Acompanhantes'][0]['NumeroCPF']))

    # Numero Volcher acompanhante
    c.roundRect(30, 386, 540, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 401, "N° Volcher(S) Acompanhante")
    c.setFont("Helvetica", 9)
    c.drawString(35, 390, str())

    # Endereço Paciente
    c.roundRect(30, 348, 540, 28, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 377, "Endereço")
    c.setFont("Helvetica", 9)
    texto = AjustarTexto(str(dados['IdPaciente']['Endereco'] + " / CEP: " + dados['IdPaciente']['CEP']), 110)
    y = 366
    for linha in texto:
        c.drawString(35, y, str(linha))
        y -= 11

    # Via de transporte
    c.roundRect(30, 310, 240, 28, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 339, "Via de Transporte")
    
    # Quadrados
    c.roundRect(35, 326, 9, 9, 2, stroke=1, fill=0)
    c.drawString(46, 328, "Rodoviário")
    c.roundRect(35, 313, 9, 9, 2, stroke=1, fill=0)
    c.drawString(46, 315, "Aério")
    
    c.roundRect(110, 326, 9, 9, 2, stroke=1, fill=0)
    c.drawString(121, 328, "Ambulância")
    c.roundRect(110, 313, 9, 9, 2, stroke=1, fill=0)
    c.drawString(121, 315, "Ferroviário")
    
    c.roundRect(185, 326, 9, 9, 2, stroke=1, fill=0)
    c.drawString(196, 328, "UTI Aérea")
    c.roundRect(185, 313, 9, 9, 2, stroke=1, fill=0)
    c.drawString(196, 315, "UTI Terrestre")
    
    # Lógica para o X 
    
    x,y = ViaDeTransporteX(str(dados['TipoDeslocamento']).strip())
    c.setFont("Helvetica-Bold", 8)
    c.drawString(x, y, "X")
    
    # Via de transporte
    c.roundRect(275, 310,295 , 28, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(280, 339, "Empresa de Transporte")
    c.drawString(280, 326, str(dados['EmpresaTransporte']))
    
    # Dados do Processo -----------------------------------------------------------------------------------------
    c.saveState()  # Salva o estado atual do canvas
    c.setFillColorRGB(0.8, 0.8, 0.8)
    c.setLineWidth(1)
    c.roundRect(30, 286, 540, rect_height, rect_corner_radius, stroke=1, fill=1)
    c.restoreState()  # Restaura o estado anterior do canvas
    c.setFont("Helvetica-Bold", 12)
    c.drawString(CentralizarTexto("Dados do Processo", 12, c), 289, "Dados do Processo")

    
    # Tipo de Atendimento / Consulta
    c.setLineWidth(0.7)
    c.roundRect(30, 262, 135, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 277, "Tipo de Atendimento / consulta")
    c.setFont("Helvetica", 9)
    c.drawString(35, 266, str(dados['TipoAtendimento']))
    
    # Especialidade
    c.roundRect(170, 262, 200, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(175, 277, "Especialidade")
    c.setFont("Helvetica", 9)
    c.drawString(175, 266, str(dados['Especialidade']))
    
    # Data do agendamento
    c.roundRect(435, 262, 95, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(440, 277, "Data Agendamento")
    c.setFont("Helvetica", 9)
    c.drawString(440, 266, str(dados['DataAgendamento']))
    
    # Quantidade de passagens
    c.roundRect(30, 224, 135, 28, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 253, "Quantidade de passagens")
    c.setFont("Helvetica", 9)
    c.drawString(35, 242, "("+ str(dados['TotalPassagem']['ida']+dados['TotalPassagem']['volta'])+ ") Passagem(ns)")
    c.drawString(35, 229, "("+ str(dados['TotalPassagem']['ida'])+ ") Idas /")
    c.drawString(70, 229, " ("+ str(dados['TotalPassagem']['volta'])+ ") Voltas")
    
    # Local de Origem
    c.roundRect(170, 238, 200, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(175, 253, "Local de Origem")
    c.setFont("Helvetica", 9)
    c.drawString(175, 242, str(dados['LocalOrigem']))
    
    # Local de Origem
    c.roundRect(375, 238, 195, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(380, 253, "Local de Destino")
    c.setFont("Helvetica", 9)
    c.drawString(380, 242, str(dados['Destino']))
    
    # Local de Atendimento (Unidade de Saúde)
    c.roundRect(170, 214, 400, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(175, 229, "Local de Atendimento (Unidade de Saúde)")
    c.setFont("Helvetica", 9)
    c.drawString(175, 218, str(dados['LocalAtendimento']))    
    
    # Observação
    c.roundRect(30, 162, 540, 40, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(35, 203, str("Observações"))
    
    # Assinaturas
    c.roundRect(30, 97, 540, 60, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 10)
    c.drawString(435, 147, "Mabará, " + str(data_formatada))
    
    texto = str(dados['IdPaciente']['NomePaciente'])+" - N° CPF " + str(dados['IdPaciente']['NumeroCPF'])
    x = alinharAssinatura(texto,50,230, c)
    c.setFont("Helvetica-Bold", 6)
    c.drawString(x, 108, str(dados['IdPaciente']['NomePaciente'])+" - N° CPF " + str(dados['IdPaciente']['NumeroCPF']))
    c.drawString(120, 101, "Assinatura do(a) acompanhante")
    c.rect(50, 115, 230, 0.05, stroke=1, fill=1)

    texto = str(dados['IdPaciente']['Acompanhantes'][0]['nomeAcompanhante'])+" - N° CPF " + str(dados['IdPaciente']['Acompanhantes'][0]['NumeroCPF'])
    x = alinharAssinatura(texto,320,230, c)
    c.setFont("Helvetica-Bold", 6)
    c.drawString(x, 108, str(dados['IdPaciente']['Acompanhantes'][0]['nomeAcompanhante'])+" - N° CPF " + str(dados['IdPaciente']['Acompanhantes'][0]['NumeroCPF']))
    c.drawString(390, 101, "Assinatura do(a) acompanhante")
    c.rect(320, 115, 230, 0.05, stroke=1, fill=1)
    
    
    c.setFont("Helvetica-Bold", 9)
    c.drawString(145, 87, "Telefones de Contato TFD: (094)99134-5052 (VIVO) (094)98114-7837 (TIM)")
    
    
  
    # Dados Atendimento
    c.roundRect(30, 18, 540, 65, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(CentralizarTexto("Dados do Atendimento",12,c), 73, "Dados do Atendimento")

    # Nome funcionario
    c.roundRect(34, 22, 300, 47, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(38, 61, "Nome do funcionário responsável pleo atendimento: ")
    c.setFont("Helvetica", 10)
    c.drawString(38, 25, "Atendente TFD de marabá ")
    
    # Data do atendimento
    c.roundRect(465, 48, 85, rect_height, rect_corner_radius, stroke=1, fill=0)
    c.setFont("Helvetica", 8)
    c.drawString(470, 63, "Data do Atendimento")
    c.setFont("Helvetica", 9)
    c.drawString(470, 52, str(data_formatada_numero))
    
    
    
    # #Nome de acompanhante
    # c.roundRect(30, 421, 120, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(35, 443, "Nome do ")
    # c.setFont("Helvetica", 10)
    # c.drawString(35, 428, str(dados['IdPaciente']['Acompanhantes'][0]['nomeAcompanhante'])) 
    
    # # Nome Paciente
    # c.roundRect(30, 700, 330, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica-Bold", 8)
    # c.drawString(35, 722, "Nome Paciente")
    # c.setFont("Helvetica", 10)
    # c.drawString(35, 707, str(dados['IdPaciente']['NomePaciente']))
    
    # # Sexo
    # c.roundRect(365, 700, 80, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(370, 722, "Sexo")
    # c.setFont("Helvetica", 10)
    # c.drawString(370, 707, str(dados['IdPaciente']['Sexo']))
    
    # # Data de Nascimento
    # c.roundRect(450, 700, 80, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(455, 722, "Data Nascimento")
    # c.setFont("Helvetica", 10)
    # c.drawString(455, 707, str(dados['IdPaciente']['DataNascimento']))
    
    # # Idade
    # c.roundRect(535, 700, 35, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(540, 722, "Idade")
    # c.setFont("Helvetica", 10)
    # c.drawString(540, 707, str(dados['IdPaciente']['Idade']))

    # # Nome do Pai / Responsavel / Tutor(a)
    # c.roundRect(30, 665, 270, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(35, 687, "Nome do Pai / Responsavel / Tutor(a)")
    # c.setFont("Helvetica", 10)
    # c.drawString(35, 672, str(dados['IdPaciente']['NomePaiouResponsavel']))

    # # Nome da Mãe
    # c.roundRect(305, 665, 265, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(310, 687, "Nome da Mãe")
    # c.setFont("Helvetica", 10)
    # c.drawString(310, 672, str(dados['IdPaciente']['NomeMae']))
    
    # # Endereço 
    # c.roundRect(30, 630, 300, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(35, 652, "Endereço")
    # c.setFont("Helvetica", 10)
    # c.drawString(35, 637, str(dados['IdPaciente']['Endereco']))
    
    # # Nome da Mãe
    # c.roundRect(335, 630, 235, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(340, 652, "Bairro")
    # c.setFont("Helvetica", 10)
    # c.drawString(340, 637, str(dados['IdPaciente']['Bairro']))
    
    # # Município
    # c.roundRect(30, 595, 150, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(35, 617, "Município")
    # c.setFont("Helvetica", 10)
    # c.drawString(35, 602, str(dados['IdPaciente']['Cidade']))
    
    # # UF
    # c.roundRect(185, 595, 30, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(190, 617, "UF")
    # c.setFont("Helvetica", 10)
    # c.drawString(190, 602, str(dados['IdPaciente']['UF']))     
    
    # # Telefone 1
    # c.roundRect(220, 595, 100, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(225, 617, "Telefone 1")
    # c.setFont("Helvetica", 10)
    # c.drawString(225, 602, str(dados['IdPaciente']['Celular'][0]['Numero']))     

    # # Telefone 2
    # c.roundRect(325, 595, 100, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(330, 617, "Telefone 2")
    # c.setFont("Helvetica", 10)
    # c.drawString(330, 602, str(dados['IdPaciente']['Celular'][0]['Numero']))    
    
    # # Cartão SUS
    # c.roundRect(430, 595, 140, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(435, 617, "Cartão SUS")
    # c.setFont("Helvetica", 10)
    # c.drawString(435, 602, str(dados['IdPaciente']['NumeroCartaoSUS']))
    
    # # Referencia
    # c.roundRect(30, 560, 540, rect_height, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(35, 582, "Referência")
    # c.setFont("Helvetica", 10)
    # c.drawString(35, 567, str(dados['IdPaciente']['Referencia']))    
    
    # # Observação
    # c.roundRect(30, 505, 540, 40, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(35, 547, "Observação")
    # c.setFont("Helvetica", 10)
    # texto = AjustarTexto(str(dados['ObsAtendimento']), 120)
    # y=534
    # for linha in texto:
    #     c.drawString(35, y, str(linha))
    #     y -= 10
    
    # #Label
    # c.setFont("Helvetica-Bold", 9)
    # c.drawString(35, 490,"Identificação do Profissional")
    
    # # Motivo
    # c.roundRect(30, 435, 540, 40, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(35, 477, "Motivo(Principais Queixas)")
    # c.setFont("Helvetica", 10)
    # texto = AjustarTexto(str(dados['ObsAtendimento']), 120)
    # y=464
    # for linha in texto:
    #     c.drawString(35, y, str(linha))
    #     y -= 10
 
    # # diagnostico
    # c.roundRect(30, 380, 540, 40, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(35, 422, "Diagnóstico")
    # c.setFont("Helvetica", 10)
    # texto = AjustarTexto(str(dados['ObsAtendimento']), 120)
    # y=409
    # for linha in texto:
    #     c.drawString(35, y, str(linha))
    #     y -= 10
    
    # # diagnostico
    # c.roundRect(30, 345, 370, 20, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(35, 367, "Médico")
    # c.setFont("Helvetica", 10)
    # c.drawString(35, 352, str(dados['IdMedico']['NomeCompleto']))
    
    # # diagnostico
    # c.roundRect(405, 345, 165, 20, rect_corner_radius, stroke=1, fill=0)
    # c.setFont("Helvetica", 8)
    # c.drawString(410, 367, "Especialidade")
    # c.setFont("Helvetica", 10)
    # c.drawString(410, 352, str(dados['IdMedico']['Especialidades'][0]['Nome']))
    
    # Fechar o arquivo PDF
    c.save()

# 24 entre quadrados
# 15 entre quadrado e label
# 4 entre dados e quadrado

# 38 para quadrado grande
# 29 entre quadrado e label
# 18 entre dados e quadrado

# tamanho do Quadrado grande 28
# tamanho do Quadrado pequeno 14

# valor xy para:

# Rodoviário = 37, 328
# Aéreo = 37, 315

# Ambulância = 112, 328
# Ferroviário = 112, 315

# UTI Aérea = 187, 328
# UTI Terrestre = 187, 315

# paralvras com 7 de tamanho tem 6 px


# Ler os dados passados como argumento de linha de comando
print('PDF Gerado')

gerar_relatorio_pdf(dados_paciente)

