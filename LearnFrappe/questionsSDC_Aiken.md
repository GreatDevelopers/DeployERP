```text
'#####' will generate a series, which starts with
A) 001
B) 10000
C) 0001
D) 00001
ANSWER: D
Is doctype a doctype?
A) Yes
B) No
ANSWER: A
Doctype includes: Fields, View settings, Form settings and Naming series.
A) True
B) False
ANSWER: A
All Doctypes are linkable.
A) True
B) False
ANSWER: A
What is the command for dropping site completely in bench?
A) bench drop-site {sitename}
B) bench drop {sitename}
C) bench remove-site {sitename}
D) None of the above
ANSWER: A
`Field:field_name` will auto generate the naming series of doctype.
A) True
B) False
ANSWER: B
After creating Doctype, which files are created in your system?
A) javascript
B) python
C) Both javascript and python
D) None of javascript and python
ANSWER: C
To find Frappe-bench directory which command is used?
A) bench find *
B) bench find .
C) bench find ?
D) None of the rest
ANSWER: B
Form Scripts are client-side javascript code that enhances the (User Experience) UX of your Forms.
A) True
B) False
ANSWER: A
The word Frappe comes from
A) `Fra`mework + `App`lications
B) Frappe the coffee flavour
ANSWER: A
What is the function to generate full name from first name and last name
```
```python

A)

class LibraryMember(Document):
   def before_save(self):
      self.full_name = f'{self.first_name} {self.last_name or ""}'

B)

class LibraryMember(Document):
   def before_save(self):
      self_full_name = f'{self_first_name} {self_last_name or ""}'

C)

class LibraryMember(Document):
   def before-save(self):
      self.full_name = f'{self.first_name} {self.last_name or ""}'

D)

class LibraryMember(Document):
   def before_save(self):
      self.full name = f'{self.first name} {self.last name or ""}'

```
```text
ANSWER: A
Any visitor can have access to a web form even without a Login ID.
A) True
B) false
ANSWER: A
For providing `Has web view` to our doctype, our site has to be in developer mode?
A) True
B) False
ANSWER: A
While creating site it is required to set administrator password?
A) True
B) False
ANSWER: A
For check site in developer mode which file is used?
A) private
B) public
C) site_config.json
D) indexes
ANSWER: C
Controller methods allow you to write _______ during the lifecycle of a document.
A) flow
B) structure
C) coding
D) business logic
ANSWER: D
What is the correct command to create a site with domain library.test?
A) bench new-site library.test
B) bench create-site "library.test"
C) bench new_site library.test
D) bench create new-site library.test
ANSWER: A
What is the command to create an app named Library Management?
A) bench create-app library_management
B) bench create new-app library_management
C) bench new app library_management
D) bench new-app library_management
ANSWER: D
While creating site Database root password is not required?
A) True
B) False
ANSWER: B
While creating new app which details are not filled by default?
A) App Description
B) App Publisher
C) App Email
D) All of the above
E) 1. and 3.
F) 1. and 2.
G) 2. and 3.
ANSWER: D
Command to install app on site?
A) bench --site {sitename} install-app {appname}
B) bench install-app {appname}
C) bench {sitename} install-app {appname}
D) bench --site install-app {appname}
ANSWER: A
Frappe uses ________ by default for it's web pages's look and feel / formatting.
A) python
B) javascript
C) Bootstrap 4
D) css
ANSWER: C
Usually you will want to give limited access to your customers. In case of Libray, we want Library Members to be able to view available books that the book y can be issue. We can achieve this by using.
A) Web view pages.
B) Web templates.
C) Doctype
D) Bench
ANSWER: A
In the website route meta a route can start with a "/".
A) True
B) False
ANSWER: B
Arbitrary meta tags can be added in your web pages using Website Route Meta.
A) true
B) false
ANSWER: A
Which of the following methods runs every time a document is saved?
A) On_submit
B) on_save
C) before_save
D) before_submit
ANSWER: C
The `name` field is required to be filled in manually if it is set to prompt.
A) True
B) false
ANSWER: A
When a new database is created in mysql?
A) While installing frappe
B) While creating a site
C) While installing app
D) All of the rest
ANSWER: B
For creating new doctype, which mode is necessary ?
A) Admin mode
B) Developer mode
C) System Manager mode
ANSWER: B
Page Builder lets you quickly
A) create web pages from pre-configured web templates.
B) create a doctype pre-configured web templates.
C) create a web template pre-configured web forms.
D) write code for the page
ANSWER: A
All DocTypes in Frappe have a primary key called
A) Naming series
B) Name
C) Document type
ANSWER: B
What is the command to remove app from site?
A) bench --site {sitename} uninstall-app
B) bench sitename uninstall-app {appname}
C) bench --site {sitename} uninstall-app {appname}
D) All of the rest
ANSWER: C
Bench command to remove an app?
A) bench uninstall -app
B) bench uninstall {appname}
C) bench uninstall-app {appname}
D) bench remove-app {appname}
ANSWER: D
What is the command to enable server side script?
A) bench –site <your_site> set-config enabled_server_script true
B) bench –site <your_site> set-config server_script_enabled true
C) bench –site set-config <your_site> server_script_enabled true
D) bench –site set-config <your_site> enabled_server_script true
ANSWER: B
What is the command to set default site in frappe?
A) bench use sitename
B) bench update sitename
C) bench get-site sitename
D) bench get-update-current-site sitename
ANSWER: A
Command to change the bench into developer mode?
A) bench set config -g developer_mode true
B) bench set-config -g developer_mode true
C) bench set-config g developer_mode true
D) bench set-configuration -g developer-mode true
ANSWER: B
What is a single doctype?
A) It does not create a new database table.
B) It creates a new database table.
C) It creates multiple database tables.
ANSWER: A
What are the states of a submittable doctype?
A) Draft, Saved, Cancelled
B) Draft, Submitted, Deleted
C) Draft, Submitted, Cancelled
D) Unsaved, Saved, Cancelled
ANSWER: C
After creating the app the doctypes are stored in which directory?
A) App Directory
B) Frappe Directory
C) Any of App and Frapee Directory
D) None of App and Frapee Directory
ANSWER: A
What was the type of field "Full Name" in "Library Member" doctype?
A) Data
B) Data, Hidden
C) Data, Mandatory
D) Data, Read Only
ANSWER: D
What was the type of field "Library Member" in "Library Membership" doctype?
A) Data, Mandatory
B) Link, Mandatory
C) Link, Read Only
D) Data, Read Only
ANSWER: B
How many types of Doctype Naming is provided by Frappe Framework ?
A) 4
B) 5
C) 6
D) 3
ANSWER: B
Before we use bench start it is necessary to go inside frappe directory?
A) True
B) False
ANSWER: A
```
