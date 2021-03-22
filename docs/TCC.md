---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
marp: true

backgroundImage: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKFcfc3lLfpbn8A5tdeEJ1htvfSaduvEn1Lg&usqp=CAU')

---
# ```ERPNext```

---

# ```Company```

![bg :100% 90%](images/Company.png)

---

# ```Item Group```
![bg :100% 70%](images/ItemGroup.png)

---
# ```Item List```
![bg :100% 70%](images/ItemList.png)

---
# ```Customer List```
![bg :90% 70%](images/CustomerList.png)

----
# ```Price List```
![bg :90% 70%](images/PriceList.png)

----
# ```Quotation```
![bg right :100% 90%](images/Quotation.jpg)

---- 
# ```Sales order```
![bg left :100% 70%](https://user-images.githubusercontent.com/57444962/111754875-7bf8d180-88be-11eb-861c-a32bf699de75.jpg)


---

![bg left :100% 70%](https://user-images.githubusercontent.com/57444962/111754987-9d59bd80-88be-11eb-88ff-a6da118a1219.jpg)


---

# ```Delivery Note```
![bg right :100% 70%](https://user-images.githubusercontent.com/57444962/111756309-13125900-88c0-11eb-9ed4-9691acb2e406.jpg)


----

![bg right :100% 70%](https://user-images.githubusercontent.com/57444962/111756373-232a3880-88c0-11eb-8f84-0bff4bc017df.jpg)


----
# ```Payment Request```
![bg left :100% 70%](images/Payment_Request.jpg)

----
# ```Sales Invoice```
![bg right :100% 70%](images/Sales_Invoice.jpg)

----
# ```Payment Entry```
![bg left :100% 70%](images/Payment_Entry.jpg)

----

# ```Email```
![bg :90% 70%](images/Email.png)

----
# ```Chart of Accounts```
![bg  :100% 70%](images/ChartOfAccounts.png)

----
# ```General Ledger```

![bg :100% 80%](images/GeneralLedger.png)

---
# ```Journal Entry```

![bg :100% 80%](images/JournalEntry.png)

---
# ```Balance Sheet```
![bg :100% 80%](images/BalanceSheet.png)

------

# ```Profit and Loss Statement```

![bg :90% 80%](images/ProfitAndLoss.png)


What we have the tasks?
Can we have a demo / presentation of a sample company, say:

Testing and Consultancy Cell (TCC), with all data-set which may look
as real as possible, like address, GST number.

- Company
. Set up tax and Chart of Accounts
. Employee setup (Sales person/ Accounts Manager / Accountant etc)
- Item List

**Naming Series changed from default to "TCC-DOC-YYYY" (DOC refers to
all the Document type.) [Item code will also be in series type. ]
Naming series can be searched in search bar of ERPNext and can be
updated in all the Docs.**

. item group and sub-group, like

1. Material Testing
1.1 Soil
1.2 Brick
1.3 Concrete
2. Design
2.1 Architectural
2.2 Structural
3. Surveying

- Price List
Territory wise (say for Delhi, rate may be about 10% more than that of Punjab)

> **Set default Pricing.(Normal person should not be able to change the pricing.)
For fixed price in quotation show that it can't be modified by the
user [go to Accounting--> Pricing Rule --> Price Discount Scheme -->
select Rate]
For discount, [go to Accounting--> Pricing Rule --> Price Discount
Scheme--> select Discount ]**

A few items / service:

Under group 1.1

1 Soil Investigation [has variant]
1.1 Soil Investigation (up to 10m): 7500/- per bore
1.2 Soil Investigation (x m, 10 <= x < 20): (7500 + (x -10) * 950 )/- per bore
1.3 Soil Investigation (x m, 20 <= x < 30): (17000 + (x -20) * 1250 )/- per bore
1.4 Soil Investigation (x m, 30 <= x < 40): (142000 + (x -20) * 1550
)/- per bore

Under group 1.2:

1. Compression Test: 300/- per sample
2. Water absorption: 500/- per sample

Under group 2.2

1. OHSR [has variant]
1.1 OHSR up to 450 kl: 15000/-
1.2 OHSR > 450 kl: 20000/-
2. Buildings [has variant]
2.1 Buildings Rate depend on storeys and delivery time:
upto 3 storeys: 2/- per square feet
4 to 6 storeys: 3/- pe square feet
> 6 storeys Lump sum
The above rates are for normal delivery (30 days in Terms and Conditions)
for fast delivery (20 days in Terms and Conditions) 25% more
for super-fast (10 days in Terms and Conditions) delivery 50% more
for Emergency (3 days in Terms and Conditions) delivery 100% more


erpNext can automatically apply SGST and CGST on Intra-State sale, and
IGST on Inter-state sale, if tax and tax rule sets properly.

**We have worked on Out State and Instate and have almost done with the setup and is working fine.
You can check here.
https://erp.gndec.ac.in/desk#List/Tax%20Category/List
But while we are setting instate tax template as a default for a instate tax category and also outstate tax template for outstate tax category, so that everything becomes automated we faced issues.**


-----------------
- Customer
data with each of Type:
1. Individual
2. Organisation

and group as per:

https://github.com/GreatDevelopers/DeployERP/blob/main/Import/CompanyGroup/Simple.csv

- Quotation
- Sales Order
- Delivery note
- Payment Request
- Sales Invoice
- Payment Entry
-----------------
- Report List

Profit / loss
Budget

Three different types of Chart of Accounts, needed to be set during
installation are almost the same.
**Have maintained hierarchy along separate chart of accounts **

Check https://github.com/GreatDevelopers/DeployERP/blob/main/docs/Images/CoA3Options.png
Later, we need to also have custom reports like reports of test
performed or design done.

