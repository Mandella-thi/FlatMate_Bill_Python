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

    def pays(self, bill, flatmate2):
        weigth= self.days_in_house/(self.days_in_house+
                                     flatmate2.days_in_house)
        to_pay = bill.amount*weigth
        return to_pay

class PdfReport:
    """creates a Pdf file that contais data
    about the flatmates such as their names,
    their amount and the period of the bill."""

    def __init__(self, filename):
        self.filename =filename

    def generate(selfself,flatemate1,flatmate2, bill):
        pass
#bill = Bill(120)
#print(bill.amount)
the_bill =Bill(amount=120, period="March 2021")
john =Flatmate(name="John", days_in_house=20)
marry=Flatmate(name="Marry", days_in_house=25)
print("John pays",john.pays(bill=the_bill,flatmate2=marry))
print("Marry pays",marry.pays(bill=the_bill,flatmate2=john))