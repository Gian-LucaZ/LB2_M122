from reportlab.pdfgen import canvas

pdf = canvas.Canvas("Report.pdf")
pdf.drawString(100, 750, "Moin Moin")
pdf.save()