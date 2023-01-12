import webbrowser

from fpdf import FPDF


class PdfReport:
    """creates a Pdf file that contais data
    about the flatmates such as their names,
    their amount and the period of the bill."""

    def __init__(self, filename):
        self.filename =filename

    def generate(self,flatemate1,flatemate2, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.image("house.jpg", w=30,h=30)

        # add some text
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=88, txt="Flatemates Bill", border=1, align='C', ln=1)
        pdf.cell(w=150, h=40, txt="Period", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)
        pdf.cell(w=150, h=40, txt= flatemate1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatemate1.pays(bill, flatemate2))), border=1, ln=1)
        pdf.cell(w=150, h=40, txt=flatemate2.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatemate2.pays(bill,flatemate1))), border=1)
        pdf.output(self.filename)

        webbrowser.open(self.filename)
