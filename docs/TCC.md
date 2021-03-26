
# Testing and Consultancy Cell (TCC)
with all data-set which may look as real as possible, like address, GST number.

## Company

1. Search **Company List** in the search bar.
2. Click on New Company.
3. Fill all required fields that are in RED colour and you can also fill optional fields.
- Company Name
- Abbreviation
- Is Group (If we want to make child company under this company then tick this option, otherwise not required to tick this option.)
- Domain (Select option from dropbar according to the company's work.)
- Parent Company (If it is parent company then it is not required to fill this field but if it is a child company then fill this field with parent company name.)
- Default Currency (We can even use INR.)
- We are getting two templates of Chart Of Accounts templates by default (Indian Chart Of Accounts & Standard Chart of Accounts). We can even make our own Chart of accounts according to our need.
- Default Letter Head (You can Select option From dropdown OR you can create a new letter head by clicking on the option of CREATE A NEW LETTER HEAD.)

Rest fields can be filled according to the requirement but not mandatory.

![image](https://user-images.githubusercontent.com/53931644/112584559-122c7a80-8e1e-11eb-90b8-7b4d8ad31e7e.png)

4. Click on Save.

## Customer

1. Search Customer List in Search Bar.
2. Click on New Customer.
3. Fill all the Required details.
![image](https://user-images.githubusercontent.com/53931644/112581850-941ba400-8e1c-11eb-8fcd-23e49bb24bb5.png)

4. Click on save


## Item

1. Search Item List in Search Bar.
2. Click on New Item List.
3. Enter Item Code and Item Name
4. If you need to 

## Set up tax and Chart of Accounts

1. When we create company,there is an option of Chart of accounts which we can fill 
2. Search Chart of Accounts in the Search Bar.
3. 
## Employee setup (Sales person/ Accounts Manager / Accountant etc)
##  Item List

**Naming Series changed from default to "TCC-DOC-YYYY" (DOC refers to
all the Document type.) [Item code will also be in series type. ]
Naming series can be searched in search bar of ERPNext and can be
updated in all the Docs.**

## item group and sub-group, like

1. Material Testing
1.1 Soil
1.2 Brick
1.3 Concrete
2. Design
2.1 Architectural
2.2 Structural
3. Surveying

## Price List
- Territory wise (say for Delhi, rate may be about 10% more than that of Punjab)

**We are exploring how can we do this.**

**Set default Pricing.(Normal person should not be able to change the pricing.)
For fixed price in quotation show that it can't be modified by the
user [go to Accounting--> Pricing Rule --> Price Discount Scheme -->
select Rate]
For discount, [go to Accounting--> Pricing Rule --> Price Discount
Scheme--> select Discount ]**

## A few items / service:

Under group 1.1

1 Soil Investigation [has variant]
1.1 Soil Investigation (up to 10m): 7500/- per bore <br/>
1.2 Soil Investigation (x m, 10 <= x < 20): (7500 + (x -10) * 950 )/- per bore <br/>
1.3 Soil Investigation (x m, 20 <= x < 30): (17000 + (x -20) * 1250 )/- per bore <br/>
1.4 Soil Investigation (x m, 30 <= x < 40): (142000 + (x -20) * 1550 <br/>
)/- per bore

**Without using formula, the list of item variants are very long.
https://erp.gndec.ac.in/desk#List/Item/List
We are trying to figuring out this problem.**

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
6 storeys Lump sum
The above rates are for normal delivery (30 days in Terms and Conditions)
for fast delivery (20 days in Terms and Conditions) 25% more
for super-fast (10 days in Terms and Conditions) delivery 50% more
for Emergency (3 days in Terms and Conditions) delivery 100% more


erpNext can automatically apply SGST and CGST on Intra-State sale, and
IGST on Inter-state sale, if tax and tax rule sets properly.

**We have to manually choose the option of In state and Out state, it is not taking automatically according to the customer address.
We are finding the solution for this.**

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

**Reports and Registers have been explored and documented on github.**

Profit / loss
Budget

Three different types of Chart of Accounts, needed to be set during
installation are almost the same.
**Have maintained hierarchy along separate chart of accounts **


Later, we need to also have custom reports like reports of test
performed or design done.
=======
Generated
- Payment Template 
- Sales and tax template
- letter head
- Set up default price list

### [Chart of Accounts](https://erp.gndec.ac.in/desk#Tree/Account)
![image](https://user-images.githubusercontent.com/53931644/111279311-946bb080-8660-11eb-83d8-32c2aa656f60.png)
### [Department Tree](https://erp.gndec.ac.in/desk#Tree/Department)
### [Item group](https://erp.gndec.ac.in/desk#Tree/Item%20Group)
![image](https://user-images.githubusercontent.com/53931644/111279710-f9270b00-8660-11eb-84e1-f6d9eee70165.png)
### [Item list](https://erp.gndec.ac.in/desk#List/Item/List)
### [Company Tree](https://erp.gndec.ac.in/desk#Tree/Company)
### [Employee Tree](https://erp.gndec.ac.in/desk#Tree/Employee)


