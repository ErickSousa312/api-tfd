import sys
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer

def gerar_relatorio_pdf(dados):
    # Configuração do documento PDF
    c = canvas.Canvas(sys.argv[2], pagesize=letter)

    # Estilos de texto
    styles = getSampleStyleSheet()

    # Cabeçalho

    c.drawString(50, 750, "Oi, integração realizada com sucesso")

    # Fechamento do documento PDF
    c.save()

# Ler os dados passados como argumento de linha de comando
dados = sys.argv[1]
print(dados)

# Gerar o relatório em PDF
gerar_relatorio_pdf(dados)
