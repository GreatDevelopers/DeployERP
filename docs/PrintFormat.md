# Print Format

## Description
With Print Format, you can set how document types look when printing.  
Every transaction has a default Print Format called 'Standard'.  
You can change Print Formats by:  
   * Using the Print Format form
   * Using Jinja/JS scripting under Print Format
   * Using the Print Format Builder to create print formats with UI
   * Using Customize Form to hide/unhide fields

## Using the Print Format form

**To access Print Format:**  
Home > Settings > Print Format  

**To create a Print Format form:**   
1. Go to the Print Format List, click on New.  
2. Enter a name and select a DocType for which the Print Format is to be used.  
3. Select the module for which it should apply.  
4. You may select either to set standard format as 'yes' or 'no'.
5. Under styling settings, you can change the font, align the labels together on the left or right,  
add headings for sections, etc. Also, it can be edited under the section custom CSS.
7. Save.

## Using Jinja/JS scripting under Print Format
To style the Print Format using custom Jinja/JS, click on Custom Format.  
If you select this option, there'll be a checkbox for raw printing.  
To know more about raw printing,[click here](https://docs.erpnext.com/docs/user/manual/en/setting-up/print/raw-printing).  

## Using the Print Format Builder to create print formats with UI

**To access Print Format Builder:**  
Home > Settings > Print Format Builder  

1. Either select an existing format to edit or create a new format.
2. Here you can drag and drop fields from the sidebar to the page and vice versa.
3. You can add customized text, HTML in your print format, just drag and drop the Custom HTML field (in dark color)</br> 
and add it to the place where you want to add the Custom HTML content.
4. Then click on Edit HTML to edit your content.
5. After making the changes, click on Save.

## Using Customize Form to hide/unhide fields

1. Open the document for which you want to make a Print Format. click on the print icon and then click on the customise button. Note: You must have System Manager permission to do this.
2. Enter a new print format name.
3. Here you can drag and drop fields from the sidebar to the page and vice versa. (same as in Print Format Builder)
4. You can add customized text, HTML in your print format, just drag and drop the Custom HTML field (in dark color) and add it to the place where you want to add the Custom HTML content.
5. Then click on Edit HTML to edit your content.
6. After making the changes, click on Save.


# **What I have done for TCC Project as a Report manager and how?**

- Created Print style [Desired](https://erp.gndec.ac.in/desk#Form/Print%20Style/Desired)

1. Search ```Print Style``` in Search Box.
2. Click on New.
3. Add the CSS script and checked the Standard field.
4. Click on Save.

- Created [Print Format For Quotation](https://erp.gndec.ac.in/desk#print-format-builder/Print%20Format%20for%20Quotation)
- Created [Print Format For Receipt](https://erp.gndec.ac.in/desk#print-format-builder/Print%20Format%20of%20Receipt)
 
1. Search ```Print Format``` in Search Box.
2. Click on New.
3. Fill the Name of Print Format and Doctype.
4. Click on Save.
5. Click on Edit Format.
6. For edit the heading: Click on Edit heading--> Edit html code
7. For change the other settings, just used drag and drop approach.
8. Some fields has table type display like Items(Table), one can remove and add the column in the table by clicking on Select column.
According to the need, one can checked and unchecked the options and Click on Update.

- Edited the [Print Settings](https://erp.gndec.ac.in/desk#Form/Print%20Settings)
1. Search ```Print Settings``` in the Search Box.
2. Unchecked [the Repeat header and Footer in Pdf]().
3. Change the Print Style from default [Modern]() to [Desired]().
4. Other default settings, I have not changed as there is no need of it.
5. Click on Save.

