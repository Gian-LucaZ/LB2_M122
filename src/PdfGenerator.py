from datetime import datetime

from reportlab.pdfgen import canvas


def generate(data: dict):
    title: str = "PlaylistFeed-%s.pdf" % datetime.now().strftime("%Y-%m-%d")

    pdf = canvas.Canvas(title)
    _generate_content(pdf, data)
    pdf.save()


def _generate_content(pdf, data: dict):
    pdf.drawString(100, 750, "Moin Moin")