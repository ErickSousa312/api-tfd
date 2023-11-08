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
def gerar_relatorio_pdf():
    caminho_completo = os.path.join(os.path.dirname(
        __file__), 'Termo de reponsabilidade.pdf')
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
    c.rect(130, 741, 360, 0.9, stroke=0, fill=1)

    # c.restoreState()  # Restaura o estado anterior do canvas

    c.setFont("Helvetica-Bold", 12)
    text = "Obrigações e Direitos dos Pacientes/Acompanhantes do TFD"
    c.drawString(CentralizarTexto(text, 12, c), 745, text)

    # 14 entre paragrafos
    # 11 entre linhas

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 726, "01   Ter domicílio no Município de Marabá,")

    c.setFont("Helvetica", 10)
    c.drawString(
        235, 726, "inclusive zona rural com comprovante de luz, água ou telefone;")

    # 14 entre paragrafos
    # 11 entre linhas

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 712, "02")

    c.setFont("Helvetica", 10)
    c.drawString(
        50, 712, "Não será permitido menor de 18 anos e maior de 60 anos, serem acompanhante;")

    # 14 entre paragrafos
    # 11 entre linhas

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 698, "03")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("O usuário deverá prestar conta dos canhotos das passagens e entrega-los no guichê do serviço de TFD, quando \
  atendimento fora do domicílio sob pena de não receber as passagens da próxima viagem;\
"), 120)
    y = 698
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 673, "04")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("Pedir ao profissional que atendeu o paciente, que faça o registro de todos atendimentos na folha de evolução \
  no processo; no caso de internação registrar a data de admissão e da alta; salientando que não deve haver rasuras,\
  sob pena de não receber a ajuda de custo. \
"), 120)
    y = 673
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 637, "05")

    c.setFont("Helvetica", 10)
    c.drawString(
        50, 637, "A ajuda de custo será feita preferenciamente no nome do paciente, exceto quando o mesmo for menor de idade;")

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 623, "06")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("Caso o profissional para o qual o paciente estava agendado não compareça, é de competência do assistente social \
  prestar as devidas informações na ficha de evolução do paciente, na ausência desse profissional, fica responsável\
  o enfermeiro ou coordenador do setor, caso tenha sido realizado exames laboratoriais, o bioquimico/bimédico poderá \
    fazer a evolução. (Só permitido para profissionais de nivel superior com carimbo e assinatura.) \
"), 120)
    y = 623
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 576, "07")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("A devolução do processo deverá ser agendada no ato do recebimento do mesmo. Caso não fique agendado paciente \
        terá até\
"), 120)
    y = 576
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        90, 565, "05 dias úteis,")

    c.setFont("Helvetica", 10)
    c.drawString(
        155, 565, " para comparecer no serviço de TFD, para realizar o agendamento da devolução.")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("O usuário deverá ser encaminhado ao município de destino, somente após a marcação de consulta, procedimento, \
        exames, liberação de leito, via regulação para garantia do atendimento, bem como, para prestação de contas com a \
        auditoria, salvo em caso de urgência, ressaltando que, as passagens só serão liberadas para o paciente ou acompa- \
        nhante \
"), 120)
    y = 554
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 507, "08")

    c.setFont("Helvetica", 10)
    c.drawString(
        50, 507, "É de obrigação do usuário a remarcação do seu retorno.")

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 493, "09")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("Caso o agendamento tenha sido feito por telefone, apresentar número de telefone e o nome do funcionário que fez \
        o agendamento, para confirmação e quando feito via mensagem/WhatsApp, o mesmo deve trazer a impressão do \
        agendamento. \
"), 120)
    y = 493
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 457, "10")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("O usuário ou responsável deverá manter sempre atualizado seu número de contato, endereço e bem como, os dados \
        do cartão SUS e comprovante de residência anualmente, no mês de aniversário da entrada do Processo. \
"), 120)
    y = 457
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 432, "11")

    c.setFont("Helvetica", 10)
    c.drawString(
        50, 432, "Em caso de troca de acompanhante, apresentar justificativa por escrito;")

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 418, "12")

    c.setFont("Helvetica", 10)
    c.drawString(
        50, 418, "Todo processo só terá")

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        155, 418, "validade de um ano.")

    c.setFont("Helvetica", 10)
    c.drawString(
        260, 418, "Caso o paciente não tenha utilizado neste período, ele será automática-")

    c.setFont("Helvetica", 10)
    c.drawString(
        50, 407, "mente cancelado.")

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 393, "13")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("Obrigatório salientar ao usuário que, em nenhuma hipótese será autorizado procedimentos como: Consultas, exames \
        e outros que existirem no municipio. \
"), 120)
    y = 393
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 368, "14")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("Paciente que faz tratamento fora do município e que foi encaminhado para fora do Estado, o processo só será \
        autorizado se vier com o laudo de CERAC preenchido ; \
"), 120)
    y = 368
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 343, "15")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("Cada especialidade deverá ter um processo específico. Caso o usuário seja encaminhado para outra especialidade, \
        deverá ser aberto um novo processo e o paciente deverá apresentar todos os exames referentes ao tratamento \
        específico, no ato do exame/procedimento \
"), 120)
    y = 343
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

     # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 307, "16")

    c.setFont("Helvetica", 10)
    c.drawString(
        50, 307, "É de responsabilidade do usuário/responsável trazer cópias legíveis.")

    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        360, 307, "Quando devolver: (03) cópias do laudo do")

    c.setFont("Helvetica-Bold", 10)
    texto = AjustarTexto(str("TFD, (01) cópia da evolução médica, (01) cópia do cartão bancário, CPF do beneficiário declarados no \
                    TFD e (01) cópia marcação do seu retorno quando houver. \
                             "), 120)
    y = 296
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 271, "17")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("A Capa do Processo é de uso exclusivo da equipe de TFD de Marabá. É proibido: Amassar, rasurar, rasgar, dobrar \
                    e tirar as folhas da ordem do processo; \
                             "), 120)
    y = 271
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

     # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 246, "18")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("Quando houver óbito do paciente de TFD, a Assistente Social do hospital onde o paciente realizava o tratamento \
                    entrará em contato com TFD para as devidas providências. \
                             "), 120)
    y = 246
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    # negrito...
    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        30, 221, "19")

    c.setFont("Helvetica", 10)
    texto = AjustarTexto(str("""Em caso de pacientes "Internados", na alta do mesmo, faz-se necessário enviar via e-mail com o laudo médico e o \
                    referido meio de transporte adequado ao paciente para o seu retorno ao município de origem. \
                             """), 120)
    y = 221
    for linha in texto:
        c.drawString(50, y, str(linha))
        y -= 11

    c.setFont("Helvetica", 10)
    c.drawString(
        180, 196, "Assino, pois estou ciente das normas descritas acima.")

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

gerar_relatorio_pdf()
