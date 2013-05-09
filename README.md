jira2moztrap
============

Convert the ``.xls`` file to ``.csv``
-------------------------------------

I do this conversion with LibreOffice.  I have found this to handle
extended (international) characters better.  Load the ``.xls`` file
and then ``save as...`` to CSV format.

   * Character set: ``Unicode (UTF-8)``
   * Field delimiter: ``,``
   * Text delimiter: ``"``
   * Save cell content as shown: ``True``
   * Quote all text cells: ``False``
   * Fixed column width: ``False``

Convert to JSON
---------------

    python jira2moztrap <filename.csv>

This will create a ``.json`` version of that file ready to import to MozTrap.

Import to MozTrap
-----------------

The command to import to a local instance is:

    ./manage.py import <product name> <version name> <file name>

However, to import a file on Mozilla MozTrap production environment, you'll
need to submit a bug report.  Here's an example: https://bugzilla.mozilla.org/show_bug.cgi?id=870595

The command line on MozTrap production will look like this:

    ./vendor-manage.py import -f "Firefox OS" "v1.1.0" ../SMS.json

