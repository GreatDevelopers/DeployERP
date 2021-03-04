# Print Format

## Description
With Print Format, you can set how document types look when printing.</br>
Every transaction has a default Print Format called 'Standard'. </br>
You can change Print Formats by: </br>
   * Using the Print Format form
   * Using Jinja/JS scripting under Print Format
   * Using the Print Format Builder to create print formats with UI
   * Using Customize Form to hide/unhide fields

## Using the Print Format form

**To access Print Format:** </br>
Home > Settings > Print Format</br>

**To create a Print Format form:**</br>
1. Go to the Print Format List, click on New.</br>
2. Enter a name and select a DocType for which the Print Format is to be used.</br>
3. Select the module for which it should apply.</br>
4. You may select either to set standard format as 'yes' or 'no'.
5. Under styling settings, you can change the font, align the labels together on the left or right,</br> 
add headings for sections, etc. Also, it can be edited under the section custom CSS.
7. Save.

## Using Jinja/JS scripting under Print Format
To style the Print Format using custom Jinja/JS, click on Custom Format. </br>
If you select this option, there'll be a checkbox for raw printing. </br>
To know more about raw printing,[click here](https://docs.erpnext.com/docs/user/manual/en/setting-up/print/raw-printing).</br>

## Using the Print Format Builder to create print formats with UI

**To access Print Format Builder: **</br>
Home > Settings > Print Format Builder</br>

1. Either select an existing format to edit or create a new format.
2. Here you can drag and drop fields from the sidebar to the page and vice versa.
3. You can add customized text, HTML in your print format, just drag and drop the Custom HTML field (in dark color)</br> 
and add it to the place where you want to add the Custom HTML content.
4. Then click on Edit HTML to edit your content.
5. After making the changes, click on Save.

## Using Customize Form to hide/unhide fields

1. Open the document for which you want to make a Print Format. click on the print icon and then</br> 
click on the customise button. Note: You must have System Manager permission to do this.
2. Enter a new print format name.
3. Here you can drag and drop fields from the sidebar to the page and vice versa. (same as in Print Format Builder)
4. You can add customized text, HTML in your print format, just drag and drop the Custom HTML field (in dark color)</br> 
and add it to the place where you want to add the Custom HTML content.
5. Then click on Edit HTML to edit your content.
6. After making the changes, click on Save.
