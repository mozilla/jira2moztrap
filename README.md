jira2moztrap
============

1. Convert the ``.xls`` file to ``.csv`` using LibreOffice.  I have found this
   to handle extended (international) characters better.

   * Character set: ``Unicode (UTF-8)``
   * Field delimiter: ``,``
   * Text delimiter: ``"``
   * Save cell content as shown: ``True``
   * Quote all text cells: ``False``
   * Fixed column width: ``False``

2. Convert to JSON: ``python jira2moztrap <filename.csv>``
   This will create a ``.json`` version of that file ready to import to moztrap

3.