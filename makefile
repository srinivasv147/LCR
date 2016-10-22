generatePDF:
	cp ./source/lcr.jpg ./
	python ./source/main.py
	pdflatex ./source/130010033.tex
	cp ./130010033.aux ./source/
	cp ./source/sources.bib ./
	bibtex ./source/130010033
	pdflatex ./source/130010033
	cp ./source/130010033.bbl ./
	pdflatex ./source/130010033
	pdflatex ./source/130010033
	mkdir output
	mv ./130010033.pdf ./output/
	mv "plots130010033_eta=0.5.mp4" ./output/
	rm 130010033.*
	rm lcr.jpg
	rm plots.png
	rm sources.bib
test:
	python ./source/test.py
clean:
	rm -r output
