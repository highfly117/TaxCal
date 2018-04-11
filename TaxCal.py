#!/user
# -*- coding: utf-8 -*-
import locale
import Tkinter as Tk

locale.setlocale(locale.LC_ALL, '')
root = Tk.Tk()
root.title("My Tax Calculator")
root.geometry("700x200")


def callback():
    GetGrossTax = GrossTaxIn.get()
    GrossYear = int(GetGrossTax)
    GrossMonth = GrossYear/12
    GrossWeek = GrossYear/52
    GrossDay = GrossYear/365
    Yearli = Tk.Label(RightFrame, text='£{:,.2f}'.format(GrossYear))
    Yearli.grid(row=1, column=1)
    Monthli = Tk.Label(RightFrame, text='£{:,.2f}'.format(GrossMonth))
    Monthli.grid(row=1, column=2)
    Weekli = Tk.Label(RightFrame, text='£{:,.2f}'.format(GrossWeek))
    Weekli.grid(row=1, column=3)
    Dayli = Tk.Label(RightFrame, text='£{:,.2f}'.format(GrossDay))
    Dayli.grid(row=1, column=4)


LeftFrame = Tk.Frame(root, bg="blue", width=300, height=200, pady=3)
RightFrame = Tk.Frame(root, bg="red", width=400, height=200, pady=3)

LeftFrame.grid(sticky="n", row=0,column=0)
RightFrame.grid(sticky="n", row=0, column=1)

TaxYearOp = Tk.StringVar()
TaxYearOp.set("2018/2019") # default value

StudentLoanOp = Tk.StringVar()
StudentLoanOp.set("No")

TaxYear = Tk.Label(LeftFrame, text="Select tax year")
TaxYear.grid(row=1, column=0)

Placeholder = Tk.Label(LeftFrame, text="")
Placeholder.grid(row=1, column=1)

TaxYearLi = Tk.OptionMenu(Placeholder, TaxYearOp, "2018/2019")
TaxYearLi.grid(row=1, column=1)

StudentLoan = Tk.Label(LeftFrame, text="Repay Student Loan?")
StudentLoan.grid(row=2, column=0)

Placeholder2 = Tk.Label(LeftFrame, text="")
Placeholder2.grid(row=2, column=1)

StudentLoanLi = Tk.OptionMenu(Placeholder2, StudentLoanOp, "No","Plan 1","Plan 2")
StudentLoanLi.grid(row=2,column=1)

Pension = Tk.Label(LeftFrame, text="Pension contributions (£ or %)")
Pension.grid(row=3, column=0)

PensionEn = Tk.Entry(LeftFrame)
PensionEn.grid(row=3, column=1)

GrossTaxLa = Tk.Label(LeftFrame, text="Pre-Tax earnings here! >")
GrossTaxLa.grid(row=4, column=0)

GrossTaxIn = Tk.Entry(LeftFrame)
GrossTaxIn.grid(row=4, column=1)

TaxCalGo = Tk.Button(LeftFrame, text="Calculate My Wage", command=callback)
TaxCalGo.grid(row=5, column=1)

Summary = Tk.Label(RightFrame,text="Salary Summary", width=15)
Summary.grid(row=0, column=0)
Yearly = Tk.Label(RightFrame,text="Year", width=10)
Yearly.grid(row=0, column=1)
Monthly = Tk.Label(RightFrame,text="Monthly", width=10)
Monthly.grid(row=0, column=2)
Weekly = Tk.Label(RightFrame,text="Weekly", width=10)
Weekly.grid(row=0, column=3)
Daily = Tk.Label(RightFrame,text="Daily",  width=10)
Daily.grid(row=0, column=4)


Summary = Tk.Label(RightFrame,text="Salary Summary", width=15)
Summary.grid(row=0, column=0)
GrossPay = Tk.Label(RightFrame, text="Gross Pay", width=15)
GrossPay.grid(row=1, column=0)
TaxFree = Tk.Label(RightFrame, text="Tax Free Allowance", width=15)
TaxFree.grid(row=2, column=0)
TotalTaxable =Tk.Label(RightFrame, text="Total Taxable", width=15)
TotalTaxable.grid(row=3, column=0)
Tax20 = Tk.Label(RightFrame, text="20% rate", width=15)
Tax20.grid(row=4, column= 0)
Tax40 = Tk.Label(RightFrame, text="40% rate", width=15)
Tax40.grid(row=5, column= 0)
Tax45 = Tk.Label(RightFrame, text="45% rate", width=15)
Tax45.grid(row=6, column= 0)
StudentTax = Tk.Label(RightFrame, text="Student Loan", width=15)
StudentTax.grid(row=7, column= 0)
NI = Tk.Label(RightFrame, text="National Insurance", width=15)
NI.grid(row=8, column= 0)
NetWage = Tk.Label(RightFrame, text="Net Wage", width=15)
NetWage.grid(row=9, column= 0)



Tk.mainloop()


