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

    def pays(selfself, bill):
        pass


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