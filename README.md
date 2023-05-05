# Bachelor's Thesis of Project Chimata

To compile this thesis, you need the following things installed:

- `Pygments`: `pip install pygments` or use your distribution's package manager
- `TeX Live` or equivalent environment.

## How to compile this work

1. Clone the repositories `git clone --recursive https://github.com/CamberLoid/chimata-thesis`
   1. In case you forgot the submodule, run `git submodule init` and `git submodule update`
2. `make all` in your Linux OS, or
3. Compile the template
   1. `cd XDUthesis-personal`
   2. `xelatex XDUthesis.dtx`
   3. `makeindex -s gind.ist -o XDUthesis.ind XDUthesis.idx`
   4. `makeindex -s gglo.ist -o XDUthesis.gls XDUthesis.glo`
   5. `xelatex XDUthesis.dtx`
   6. `xelatex XDUthesis.dtx`
   7. `cd ..`
4. Compile the thesis
   1. `xelatex -shell-escape main`
   2. `bibtex main`: Generate bibliography
   3. `xelatex -shell-escape main`
   4. `xelatex -shell-escape main`

## Credits

- My supervisor Yunwei Wang
- Members in PLCT Lab @plctlab and AOSC Community @AOSC-Dev
- Stick Cui's awesome works on the template XDUthesis.
