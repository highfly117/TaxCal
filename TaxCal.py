#!/user/binpython
# -*- coding: utf-8 -*-

import Tkinter as Tk

root = Tk.Tk()
root.title("My Tax Calculator")
root.geometry("700x200")

LeftFrame = Tk.Frame(root, width=300, pady=3)
RightFrame = Tk.Frame(root, width=400, pady=3)

LeftFrame.grid(row=0, column=0)
RightFrame.grid(row=0, column=1)

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

TaxCalGo = Tk.Button(LeftFrame, text="Calculate My Wage")
TaxCalGo.grid(row=5, column=1)



Tk.mainloop()


