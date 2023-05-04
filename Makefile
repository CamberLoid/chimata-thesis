target := main

all: xelatex XDUthesis

xelatex: 
	xelatex -shell-escape $(target).tex
	bibtex $(target)
	xelatex -shell-escape $(target).tex
	xelatex -shell-escape $(target).tex

XDUthesis:
	pushd XDUthesis-personal/ && make template && popd

clean:
	rm -v *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.pdf
