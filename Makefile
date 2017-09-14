
all: svsv.mobi

svsv.mobi: svsv.html svsv.opf
	kindlegen svsv.opf

svsv.html: lexin_utf8.xml
	python transform.py > svsv.html

lexin_utf8.xml: LEXIN.xml
	iconv -f LATIN1 -t UTF-8 LEXIN.xml | sed s/ISO-8859-1/utf-8/ > lexin_utf8.xml

LEXIN.xml: LEXIN.zip
	unzip LEXIN.zip
	touch LEXIN.xml

LEXIN.zip:
	curl -O https://spraakbanken.gu.se/pub/reskit/LEXIN.zip
