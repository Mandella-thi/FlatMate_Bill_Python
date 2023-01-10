import webbrowser

from fpdf import FPDF
class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """ creates a flatmate person who lives in the
    flat and pays a share of the bill"""
    def __init__(self, name,days_in_house):
        self.name =name
        self.days_in_house =days_in_house

    def pays(self, bill, flatemate2):
        weigth= self.days_in_house/(self.days_in_house +
                                    flatemate2.days_in_house)
        to_pay = bill.amount*weigth
        return to_pay

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


#bill = Bill(120)
#print(bill.amount)
the_bill =Bill(amount=120, period="March 2021")
john =Flatmate(name="John", days_in_house=20)
marry=Flatmate(name="Marry", days_in_house=25)
print("John pays", john.pays(bill=the_bill, flatemate2=marry))
print("Marry pays", marry.pays(bill=the_bill, flatemate2=john))
pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatemate1=john, flatemate2= marry, bill=the_bill)