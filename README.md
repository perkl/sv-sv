sv-sv
=====

About
-----

Creates a Swedish-Swedish dictionary for Kindle, starting with LEXIN from http://spraakbanken.gu.se/

[Kindle Previewer](https://www.amazon.com/gp/feature.html?ie=UTF8&docId=1000765261) is needed for converting the dictionary to a MOBI file.

Usage
-----

To generate the dictionary as HTML, simply run make with no options in this directory. 

    $ make

The HTML file is referenced in `svsv.opf` so now we can create the MOBI file using Kindle Previewer.

Install Kindle Previewer, open it and open the `svsv.opf` file in the Previewer.

Export to MOBI in the menu: `File -> Export` and select MOBI as the file format.

Sideload the dictionary onto the E-reader by putting the dictionary MOBI file in the `Documents` folder of the E-reader.

The dictionary should now be seen in the list of dictionaries on the E-reader: `Settings -> All Settings -> Language and Dictionaries > Dictionaries` and will be used for books in the dictionary language.
