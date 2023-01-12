from Flat import Bill, Flatmate
from Report import PdfReport

#bill = Bill(120)
#print(bill.amount)
amount =float(input("Hey user enter the bill amount"))
print("This is the amaount", amount)
b= input("Hey user enter the period")
the_bill = Bill(amount=amount, period= b)
name1 =input("Hey user put the name of the first flatmate")
days_house1 =float(input(f"Hey user put the days {name1} staied in the house"))
flat1 = Flatmate(name=name1, days_in_house=days_house1)
name2 =input("Hey user put the name of the second flatmate")
days_house2 =float(input(f"Hey user put the days of {name2} staied in the house."))
flat2= Flatmate(name=name2, days_in_house=days_house2)
print(f"{name1} pays", flat1.pays(bill=the_bill, flatemate2=flat2))
print(f"{name2} pays", flat2.pays(bill=the_bill, flatemate2=flat1))
pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatemate1=flat1, flatemate2= flat2, bill=the_bill)