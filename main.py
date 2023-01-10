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
a =float(input("Hey user enter the bill amount"))
print("This is the amaount", a)
b= input("Hey user enter the period")
the_bill =Bill(amount=a, period= b)
name1 =input("Hey user put the name of the first flatmate")
days_house1 =float(input("Hey user put the days of the first flatmate"))
flat1 =Flatmate(name=name1, days_in_house=days_house1)
name2 =input("Hey user put the name of the second flatmate")
days_house2 =float(input("Hey user put the days of the second flatmate"))
flat2=Flatmate(name=name2, days_in_house=days_house2)
print("John pays", flat1.pays(bill=the_bill, flatemate2=flat2))
print("Marry pays", flat2.pays(bill=the_bill, flatemate2=flat1))
pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatemate1=flat1, flatemate2= flat2, bill=the_bill)