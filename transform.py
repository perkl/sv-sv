import xml.etree.ElementTree as ET
import sys

tree = ET.parse('lexin_utf8.xml')
root = tree.getroot()

sys.stdout.write("""<?xml version="1.0" encoding="utf-8"?>
<html xmlns:idx="www.mobipocket.com" xmlns:mbp="www.mobipocket.com" xmlns:xlink="http://www.w3.org/1999/xlink">
  <body>""")



for lemma in root.iter('lemma-entry'):
    form = lemma.find('form')
    pronunciation = lemma.find('pronunciation')
    inflection = lemma.find('inflection')
    pos = lemma.find('pos')

    sys.stdout.write("<idx:entry>")
    sys.stdout.write("<idx:orth>")
    sys.stdout.write(("<b>"+form.text.replace('~','')+"</b> "))

    if(inflection != None and inflection.text != None and len(inflection.text)!=0):
        sys.stdout.write("<idx:infl>")
        for s in inflection.text.split(' '):
            sys.stdout.write("<idx:iform value=\"")
            sys.stdout.write(s)
            sys.stdout.write("\" />")
        sys.stdout.write("</idx:infl>")

    lexemes = lemma.findall('lexeme')
    makelist = len(lexemes)>1
    if(makelist): sys.stdout.write("<ol>")
    for lexeme in lexemes:
        lexnr = lexeme.find('lexnr')
        definition = lexeme.find('definition')
        usage = lexeme.find('usage')
        comment = lexeme.find('comment')
        valency = lexeme.find('valency')
        grammat_comm = lexeme.find('grammat_comm')
        definition_comm = lexeme.find('definition_comm')
        examples = lexeme.findall('example')
        idioms = lexeme.findall('idiom')
        compounds = lexeme.findall('compound')
        
        if(makelist): sys.stdout.write("<li>")
        if(definition != None):sys.stdout.write(definition.text)
        if(makelist): sys.stdout.write("</li>")
         
    if(makelist): sys.stdout.write("</ol>")
    else: sys.stdout.write("<br>")

    sys.stdout.write("</idx:orth>")
    sys.stdout.write("</idx:entry>")
    
sys.stdout.write(""" </body>
</html>""")

sys.stdout.write("\n")
